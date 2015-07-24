projectinspire
==============
[Philip Kuperberg](github.com/lostclawz)



Launches a file randomly (of a certain extension) from given directories.
Originally created to provoke inspiration by choosing a random idea from a directory of music projects.



Options (in configuration.cfg)
------------------------------
### extensions
	default: [".mxprj", ".als"]
	A list of file extensions to find.
### directories
	default: ["~/Documents/Projects/"]
	*	A list of directores to search. The ~ expands to the user's home directory.
### print_file_data
	default: False
	print file data (creation date, etc.)
### run_file
	default: True
	If true, the chosen file will be launched using the default system application.
### take_last
	1.0
	Sorts discovered files by modification date, and chooses randomly from a percentage of the most recent files.
	*	where 1.0 = 100% of all files found, and 0.25 = last 25% of files found.



License
-------

The MIT License (MIT) Copyright (c) 2015, Philip Kuperberg.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
