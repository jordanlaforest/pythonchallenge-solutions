
import sys


def main():
  filename = sys.argv[1]
  f = open(filename, 'rb')
  data = f.read()
  f.close()
  piles = ['', '', '', '', '']
  for i in range(len(data)):
    piles[i % 5] += data[i]
    
  for j in range(len(piles)):
    f = open(filename + str(j), 'wb')
    f.write(piles[j])
    f.close()
    
if __name__ == '__main__':
  main()