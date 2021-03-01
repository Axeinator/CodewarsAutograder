import os
import glob
import argparse

def zeroFill(problem):
  if int(problem) < 10: return str(problem).zfill(2)
  else: return str(problem)

def formatInFile(problem):
  problem = zeroFill(problem)
  files = {}
  
  for i in range(1, 4):
    file = glob.glob(f"./student_datasets/prob{problem}-{i}-in.txt")
    files[i] = file[0]  
  
  for file, i in zip(files, range(1, 4)):
    # in case input file formatting is required, add here, right now
    # it is just rewriting the input into a temp file
    with open(files[file], 'r') as f:
      lines = f.readlines()
    with open(f'tmp/tmp{i}-in.txt', 'w') as f:
      f.writelines(lines)
  
def printCaseHeader(caseNum):
  print("====================")
  print(f"Case {caseNum}")

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

def runJava(problem):
  problem = zeroFill(problem)
  formatInFile(problem)
  print("Compiling, please wait")
  os.system(f"javac prob{problem}.java")
  for i in range(1, 4):
        printCaseHeader(i)
        os.system(f"java prob{problem} < tmp/tmp{i}-in.txt > tmp/your-prob{problem}-{i}-out.txt")
        code = os.system(f'diff -B -w --color tmp/your-prob{problem}-{i}-out.txt student_datasets/prob{problem}-{i}-out.txt')
        if code == 0: # files identical
          print("Suceeded!")
        else:
          print(f"Case {i} Failed :(")
  os.system(f"rm prob{problem}.class")

def runCpp(problem):
  problem = zeroFill(problem)
  formatInFile(problem)
  print("Compiling, please wait")
  # compile step (change the next line if you are using clang or your g++ invocation is different)
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

parser = argparse.ArgumentParser(description="Check CodeWars Solutions")
parser.add_argument("language", type=str, help='python, java, c++')
parser.add_argument("problem", type=int, help='number of problem to be checked')

args = parser.parse_args()

if args.language == 'python' or args.language == 'python3':
  runPython(args.problem)
elif args.language == 'java':
  runJava(args.problem)
elif args.language == 'c++' or args.language == 'cpp':
  runCpp(args.problem)
else:
  print("Invalid language. Run -h for help on parameters.")