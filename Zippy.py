
import sys
import re
import urllib
import zipfile

def readNothing(nothing, zf):
  f = zf.open(str(nothing) + '.txt')
  text = f.read()
  f.close()
  match = re.search('Next\snothing\sis\s(\d+)', text)
  if match:
    num = int(match.group(1))
  elif re.search('Divide by two', text):
    num = nothing / 2
  else:
    raise NameError('Unexpected text syntax')
  
  return num

def main():
  iterations = int(sys.argv[1])
  nothing = sys.argv[2] #12345
  zippy = sys.argv[3]
  zf = zipfile.ZipFile(zippy)
  #print nothing
  f = open('zippyOut.txt', 'w')
  for i in range(iterations):
    try:
      nothing = readNothing(nothing, zf)
      info = zf.getinfo(str(nothing) + '.txt')
      print info.comment
      f.write(info.comment)
      #print nothing
    except NameError:
      print 'Unexpected text syntax'
  f.close()

if __name__ == '__main__':
  main()