# Codewars Autograder
These python scripts can verify solutions for CodeWars programs written in Python, Java, and C++.
## Usage
To check a solution, run the checkProb.py file and add parameters in this way:

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
