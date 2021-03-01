import os
from formatters import zeroFill, formatInFile
from helpers import printCaseHeader

def runJava(problem):
  problem = zeroFill(problem)
  formatInFile(problem)
  print("Compiling, please wait")
  os.system(f"javac prob{problem}.java")
  for i in range(1, 4):
        printCaseHeader(i)
        os.system(f"java prob{problem} < tmp/tmp{i}-in.txt > tmp/your-prob{problem}-{i}-out.txt")
        code = os.system(f'diff -B -w tmp/your-prob{problem}-{i}-out.txt student_datasets/prob{problem}-{i}-out.txt')
        if code == 0: # files identical
          print("Suceeded!")
        else:
          print(f"Case {i} Failed :(")
  os.system(f"rm prob{problem}.class")
  