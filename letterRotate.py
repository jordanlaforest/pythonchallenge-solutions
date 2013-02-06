
import sys

def main():
  rotationVal = int(sys.argv[1])
  filename = sys.argv[2]
  
  f = open(filename, 'rU')
  text = f.read()
  f.close()
  newText = ''
  for i in range(len(text)):
    if ord(text[i]) >= 65 and ord(text[i]) <= 90:
      newText += chr((ord(text[i])-65 + rotationVal) % 26 + 65)
    elif ord(text[i]) >= 97 and ord(text[i]) <= 122:
      newText += chr((ord(text[i])-97 + rotationVal) % 26 + 97)
    else:
      newText += text[i]
  print newText
    
    
if __name__ == '__main__':
  main()