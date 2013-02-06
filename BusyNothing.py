
import sys
import re
import urllib
import bz2

def readNothing(nothing, url):
  global resultstr
  uf = urllib.urlopen(url + str(nothing))
  text = uf.read()
  cookie = uf.info().getheader('Set-Cookie')
  cookmatch = re.search('info=(\S+);', cookie)#[a-zA-Z%\+]
  #if cookmatch.group(1) != '%00':
    #if cookmatch.group(1) == '%C5':
    #  trace(' ')
    #  print 'space'
    #  resultstr += ' '
    #else:
  trace(cookmatch.group(1))
    #if cookmatch.group(1) == '"':
    #  resultstr += '\\"'
    #else:
  resultstr += cookmatch.group(1)
  print cookmatch.group(1)
  uf.close()
  
  match = re.search('and\sthe\snext\sbusynothing\sis\s(\d+)', text)
  
  if match:
    num = int(match.group(1))
  elif re.search('Divide by two', text):
    num = nothing / 2
  else:
    raise NameError('Unexpected text syntax')
  #trace(text)
  
  
  return num
  
filestr = 'None'
resultstr = ''

def trace(text):
  global filestr
  if filestr == 'None':
    print text
  else:
    filestr += str(text) + '\n'

def main():
  global filestr
  url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
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
  final = urllib.unquote_plus(resultstr)
  
  f = open(tofile, 'w')
  f.write(final)
  f.close()
  print bz2.decompress(final)


if __name__ == '__main__':
  main()