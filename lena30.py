
import sys


def getNext(strNum):
  count = 1
  curChr = ''
  rString = ''
  for i in range(len(strNum)):
    if i == 0:
      curChr = strNum[0]
      continue
    
    if strNum[i] == strNum[i-1]:
      count += 1
    else:
      rString += str(count) + curChr
      count = 1
      curChr = strNum[i]
  rString += str(count) + curChr
  return rString

def main():
  num = int(sys.argv[1])   
  
  a = ['1']
  for i in range(num):
    a.append(getNext(a[i]))
    
  print 'a[' + str(num) + '] = ' + str(a[num])
  print a
  print 'len(a[' + str(num) + ']) = ' + str(len(a[num]))
  
    
if __name__ == '__main__':
  main()