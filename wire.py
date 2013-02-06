
import sys
import Image, ImageDraw

def drawCircle(px, pxsrc, sNum, pxCount):
  offset = (100 - sNum) / 2
  for t in range(sNum):
    if pxCount >= 10000:
      break
    px[offset + t, offset] = pxsrc[pxCount, 0]
    pxCount += 1
  for r in range(sNum - 1):
    if pxCount >= 10000:
      break
    px[99 - offset, offset + 1 + r] = pxsrc[pxCount, 0]
    pxCount += 1
  for b in range(sNum - 1):
    if pxCount >= 10000:
      break
    px[99 - offset - b, 99 - offset] = pxsrc[pxCount, 0]
    pxCount += 1
  for l in range(sNum - 2):
    if pxCount >= 10000:
      break
    px[offset, 99 - offset - l] = pxsrc[pxCount, 0]
    pxCount += 1
  
  return pxCount

def main():
  filename = sys.argv[1]
  im = Image.open(filename)
  new = Image.new('RGB', (100, 100))
  
  pix = im.load()
  newpix = new.load()
  pxCount = 0
  sNum = 100
  while pxCount < 10000:
    pxCount = drawCircle(newpix, pix, sNum, pxCount)
    sNum -= 2
  
  #for i in range(im.size[0]):
    #newpix[i % 100, int(i / 100)] = pix[i, 0]
    
  name = filename.split('.')[-2]
  ext = filename.split('.')[-1]
  new.save(name + 'Done3' + '.' + ext)
  
    
if __name__ == '__main__':
  main()
  
"""
16

01,02,03,04
12,13,14,05
11,16,15,06
10,09,08,07

1 = 0,0
2 = 1,0
3 = 2,0
4 = 3,0
5 = 3,1

100 + 99 + 99 + 98
98 + 97 + 97 + 96

4 + 3 + 3 + 2
2 + 1 + 1 + 0

draw 100
draw 99 
draw 99
draw 98

"""