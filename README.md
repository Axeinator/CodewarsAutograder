# Codewars Autograder
These python scripts can verify solutions for CodeWars programs written in Python, Java, and C++. The version of this program in the oneFile directory is recommended.
## Usage
To check a solution, run the `checkProb.py` file and add parameters in this way:

    usage: checkProb.py [-h] language problem
    
    Check CodeWars Solutions
    
    positional arguments:
      language    python, java, c++
      problem     number of problem to be checked
    
    optional arguments:
      -h, --help  show this help message and exit

For example, to check a Java solution to problem 5, run this:

    python3 checkProb.py java 5

Your source files must be named `prob<number>.<language>` for this program to work. For example, a C++ solution to problem 7: 

    prob07.cpp
Or a python solution to problem 12:

    prob12.py

## C++ Compiler
This program uses the g++ compiler for c++, therefore your command to invoke g++ must be `g++`. If it is different (such as `g++-10`), edit the cppRunner.py file and change the line that compiles your code (underneath the "compile step" comment). If you are using the one file version, edit the same line there as well.

## Directory Strucutre
When using the oneFile version of the program, your directory structure should look something like this, make sure to keep your source files in the same directory as the `checkProb.py` file. Also, make sure you have an empty directory named `tmp` in the same directory as the `checkProb.py` file, this is used to store your program output (and also formatted input) and compare with expected output.

    ├── checkProb.py
	├── prob01.py
	├── prob02.py
	├── prob03.py
	├── prob04.py
	├── prob05.py
	├── prob06.py
	├── prob07.py
	└── student_datasets
		├── prob00-1-in.txt
		├── prob00-1-out.txt
		├── prob01-1-in.txt
		...
	└── tmp
