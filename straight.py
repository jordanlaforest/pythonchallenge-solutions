
import sys
import Image, ImageDraw

def translateLine(y, amount, src, out, width):
  for i in range(width):
    if y == 1:
      print amount, out[i, y]
    out[i, y] = src[(i - amount) % width, y]
    if y == 1:
      print out[i, y]
  

def main():
  imgname = sys.argv[1]
  outname = sys.argv[2]
  
  im = Image.open(imgname).convert('RGB')
  pix = im.load()
  
  out = Image.new('RGB', im.size)
  outpix = out.load()
  
  for y in range(im.size[1]):
    for x in range(im.size[0]):
      if y == 1:
        print pix[x, y]
      if pix[x, y] == (255, 0, 255):
        print '=='
        translateLine(y, 1-x, pix, outpix, im.size[0])
      
  out.save(outname)
    
if __name__ == '__main__':
  main()