
import sys
import re
import urllib

def readNothing(nothing, url):
  uf = urllib.urlopen(url + str(nothing))
  text = uf.read()
  uf.close()
  match = re.search('and\sthe\snext\snothing\sis\s(\d+)', text)
  if match:
    num = int(match.group(1))
  elif re.search('Divide by two', text):
    num = nothing / 2
  else:
    raise NameError('Unexpected text syntax')
  trace(text),
  
  return num
  
filestr = 'None'

def trace(text):
  global filestr
  if filestr == 'None':
    print text
  else:
    filestr += str(text) + '\n'

def main():
  global filestr
  url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
  if sys.argv[1] == '--tofile':
    tofile = sys.argv[2]
    filestr = ''
    del sys.argv[1]
    del sys.argv[1]
  else:
    tofile = None
    
  
  iterations = int(sys.argv[1])
  nothing = sys.argv[2] #12345
  trace(nothing)
  for i in range(iterations):
    if i % 100 == 0:
      print i
    try:
      nothing = readNothing(nothing, url)
      #trace(nothing)
    except NameError:
      print 'Unexpected text syntax', 'Nothing = ' + str(nothing)
      break
      
  f = open(tofile, 'w')
  f.write(filestr)
  f.close()


if __name__ == '__main__':
  main()