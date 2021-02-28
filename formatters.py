import glob
import os

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
    with open(files[file], 'r') as f:
      lines = f.readlines()
    with open(f'tmp/tmp{i}-in.txt', 'w') as f:
      f.writelines(lines)