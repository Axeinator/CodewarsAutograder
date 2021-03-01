import os
from formatters import zeroFill, formatInFile
from helpers import printCaseHeader, differ

def runPython(problem):
      problem = zeroFill(problem)
      formatInFile(problem)
      for i in range(1, 4):
        printCaseHeader(i)
        os.system(f"python3 prob{problem}.py < tmp/tmp{i}-in.txt > tmp/your-prob{problem}-{i}-out.txt")
        filesDiffer = differ(f'tmp/your-prob{problem}-{i}-out.txt', f'student_datasets/prob{problem}-{i}-out.txt')
        if not filesDiffer: # files identical
          print("Suceeded!")
        else:
          print(f"Case {i} Failed :(")

