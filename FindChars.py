
import sys
import re

def main():
  filename = sys.argv[1]
  f = open(filename, 'rU')
  text = f.read()
  f.close()
  list = re.findall('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', text)
  for char in list:
    print char,


if __name__ == '__main__':
  main()