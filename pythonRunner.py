import os
from formatters import zeroFill, formatInFile

def runPython(problem):
      problem = zeroFill(problem)
      formatInFile(problem)
      for i in range(1, 4):
        os.system(f"python3 prob{problem}.py < tmp/tmp{i}.txt > tmp/your-prob{problem}-{i}-out.txt")
        code = os.system(f'diff -w -B tmp/your-prob{problem}-{i}-out.txt student_datasets/prob{problem}-{i}-out.txt')
        if code == 0: # files identical
          print("Suceeded!")
        else:
          print("Failed :(")

