import os
from formatters import zeroFill

def runJava(problem):
  problem = zeroFill(problem)
  os.system(f"javac prob{problem}.java")
  for i in range(1, 4):
        os.system(f"java prob{problem} < tmp/tmp{i}.txt > tmp/your-prob{problem}-{i}-out.txt")
        code = os.system(f'diff -w -B -I "\n" tmp/your-prob{problem}-{i}-out.txt student_datasets/prob{problem}-{i}-out.txt')
        if code == 0: # files identical
          print("Suceeded!")
        else:
          print("Failed :(")

runJava(1)