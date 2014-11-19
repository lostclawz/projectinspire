#!/usr/bin/python
import os, sys, math, random, time, json
import ConfigParser, json
from os.path import expanduser
from datetime import datetime

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configuration.cfg")
config = ConfigParser.ConfigParser()
config.read(config_file)

extensions       = json.loads(config.get('OPTIONS', 'extensions'))
directories      = json.loads(config.get('OPTIONS', 'directories'))
print_file_data  = (config.get('OPTIONS', 'print_file_data') == "True")
print_json_data  = (config.get('OPTIONS', 'print_json_data') == "True")
run_file         = (config.get('OPTIONS', 'run_file') == "True")
take_last        = float(config.get('OPTIONS', 'take_last'))

# Replace instances of the ~ symbol with user's home directory
for d in directories:
    directories[directories.index(d)] = d.replace("~", expanduser("~"))

def main(args):
    results = []
    for directory in directories:
        for path, subdirs, files in os.walk(directory):
            for filename in files:
                f = os.path.join(path, filename)
                for extension in extensions:
                    if f.endswith(extension):
                        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(f)
                        thisobj = { 'filename':     filename,
                                    'directory':    path,
                                    'full_path':    f, 
                                    'mode':         mode,               # protection bits
                                    'ino':          ino,                # invode number
                                    'dev':          dev,                # device
                                    'nlink':        nlink,              # number of hard links
                                    'uid':          uid,                # user id of owner
                                    'gid':          gid,                # group id of owner
                                    'size':         size,               # size of file in bytes
                                    'mtime':        datetime.fromtimestamp(mtime),  # time of most recent modification
                                    'atime':        datetime.fromtimestamp(atime),  # time of most recent access
                                    'ctime':        datetime.fromtimestamp(ctime)   # time of most recent metadata change (unix) or creation (windows)     
                                   }
                        results.append(thisobj)
                        if print_file_data: print(str(thisobj['ctime']))

    results = sorted(results, key=lambda fl: fl['mtime'])
    print("total files found: " + str(len(results)))
    number_of_results = int(len(results) * take_last)
    results = results[-number_of_results:]
    print("taking a random file from the last " + str(number_of_results) + " results.")
    random_file = results[random.randrange(0,len(results)-1)]
    print(random_file['full_path'])
    if print_file_data:                            
        for fname in results: print(fname)
        print("random: " + random_file['full_path'])
    if print_json_data:
        print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
        magic(results)
    if run_file: os.system("open \"" + random_file['full_path'] + "\"") # open the file with default program

if __name__ == '__main__':
    main(sys.argv[1:]);