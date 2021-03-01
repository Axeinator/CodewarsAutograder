import os
from formatters import zeroFill, formatInFile
from helpers import printCaseHeader

def runPython(problem):
      problem = zeroFill(problem)
      formatInFile(problem)
      for i in range(1, 4):
        printCaseHeader(i)
        os.system(f"python3 prob{problem}.py < tmp/tmp{i}-in.txt > tmp/your-prob{problem}-{i}-out.txt")
        code = os.system(f'diff -B -w --color tmp/your-prob{problem}-{i}-out.txt student_datasets/prob{problem}-{i}-out.txt')
        if code == 0: # files identical
          print("Suceeded!")
        else:
          print(f"Case {i} Failed :(")

