import os
from formatters import zeroFill, formatInFile

# looks like C++ didn't have the
# same formatting problems as python
# with newlines and carriage returns
# but still am using formatInFile to 
# prevent errors


def runCpp(problem):
  problem = zeroFill(problem)
  formatInFile(problem)
  os.system(f"g++ -o tmp/prob{problem}.out prob{problem}.cpp")
  for i in range(1, 4):
        os.system(f"./tmp/prob{problem}.out < tmp/tmp{i}-in.txt > tmp/your-prob{problem}-{i}-out.txt")
        code = os.system(f'diff -B -w --color tmp/your-prob{problem}-{i}-out.txt student_datasets/prob{problem}-{i}-out.txt')
        if code == 0: # files identical
          print("Suceeded!")
        else:
          print("Failed :(")
  os.system(f"rm tmp/prob{problem}.out")
