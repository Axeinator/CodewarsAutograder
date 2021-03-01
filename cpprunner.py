import os
from formatters import zeroFill, formatInFile
from helpers import printCaseHeader

# looks like C++ didn't have the
# same formatting problems as python
# with newlines and carriage returns
# but still am using formatInFile to 
# prevent errors


def runCpp(problem):
  problem = zeroFill(problem)
  formatInFile(problem)
  print("Compiling, please wait")
  os.system(f"g++ -o tmp/prob{problem}.out prob{problem}.cpp")
  for i in range(1, 4):
        printCaseHeader(i)
        os.system(f"./tmp/prob{problem}.out < tmp/tmp{i}-in.txt > tmp/your-prob{problem}-{i}-out.txt")
        code = os.system(f'diff -B -w --color tmp/your-prob{problem}-{i}-out.txt student_datasets/prob{problem}-{i}-out.txt')
        if code == 0: # files identical
          print("Suceeded!")
        else:
          print(f"Case {i} Failed :(")
  os.system(f"rm tmp/prob{problem}.out")
