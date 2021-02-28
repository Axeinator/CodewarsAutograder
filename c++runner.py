import os
from formatters import zeroFill

# looks like C++ didn't have the
# same formatting problems as python
# with newlines and carriage returns
# so this does not use the 
# formatInFile function

def runCpp(problem):
  problem = zeroFill(problem)
  os.system(f"g++ -o tmp/prob{problem}.out prob{problem}.cpp")
  for i in range(1, 4):
        os.system(f"./tmp/prob{problem}.out < tmp/tmp{i}.txt > tmp/your-prob{problem}-{i}-out.txt")
        code = os.system(f'diff -w -B -I "\n" tmp/your-prob{problem}-{i}-out.txt student_datasets/prob{problem}-{i}-out.txt')
        if code == 0: # files identical
          print("Suceeded!")
        else:
          print("Failed :(")

runCpp(3)