import argparse
from cpprunner import runCpp
from pythonRunner import runPython
from javaRunner import runJava

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