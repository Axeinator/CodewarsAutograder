def printCaseHeader(caseNum):
  print("====================")
  print(f"Case {caseNum}")

def differ(file1, file2):
  # note that this means you must print new lines, as
  # to simplify the verification newlines characters are removed
  with open(file1, 'r') as f:
    f1 = f.read().replace('\n', '')
  with open(file2, 'r') as f:
    f2 = f.read().replace('\n', '')
  return f1 != f2
  