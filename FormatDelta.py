import sys
import re

def main():
  filename = sys.argv[1]
  leftside = ''
  rightside = ''
  
  leftdone = False
  
  texts = []
  
  f = open(filename, 'rU')
  lines = f.readlines()
  for line in lines:
    if not leftdone:
      match = re.search('([\w\s]+\w)(\s*\s\s\s)([\w\s]+\w)', line)
      if match:
        leftside += match.group(1) + '\n'
        rightside += match.group(3) + '\n'
        if(len(match.group(2)) != 3):
          texts.append(leftside)
          leftside = ''
        if len(match.group(3)) < 53:
          texts.append(rightside)
          rightside = ''
      else:
        leftdone = True
        match = re.search('\s*([\w\s]+\w)', line)
        if match:
          rightside += match.group(1) + '\n'
          if len(match.group(1)) < 53:
            texts.append(rightside)
            rightside = ''
    else:
      match = re.search('\s*([\w\s]+\w)', line)
      if match:
        rightside += match.group(1) + '\n'
        if len(match.group(1)) < 53:
          texts.append(rightside)
          rightside = ''
  texts.append(rightside)
  for i, text in enumerate(texts):
    fname = filename.split('.')[-2]
    fext = filename.split('.')[-1]
    f = open(fname + str(i) + '.' + fext, 'w')
    f.write(text)
    f.close()
    ##print text
  




if __name__ == '__main__':
  main()