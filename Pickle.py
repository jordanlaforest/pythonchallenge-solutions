
import sys
import re
import pickle

def main():
  filename = sys.argv[1]
  f = open(filename, 'rU')
  obj = pickle.load(f)
  print obj
  """
  for element in obj:
    line = ''
    #test = 0
    for tup in element:
      #if test > 5:
        line += tup[0] * tup[1]
      #test += 1
      
    print line
   """
if __name__ == '__main__':
  main()