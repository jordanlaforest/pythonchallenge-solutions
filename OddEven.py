import sys
import Image, ImageDraw

def main():
  filename = sys.argv[1]
  newname = sys.argv[2]
  
  im = Image.open(filename)
  pix = im.load()
  out = [[None, None], [None, None]]
  outpix = [[None, None], [None, None]]
  
  for b in range(2):
    for a in range(2):
      out[b][a] = Image.new('RGB', (im.size[0] / 2, im.size[1] / 2))
      outpix[b][a] = out[b][a].load()
  
  y = 0
  x = 0
  for y in range(im.size[1]):
    for x in range(im.size[0]):
      outpix[x % 2][y % 2][int(x / 2), int(y / 2)] = pix[x, y]
      #pix[x, y] = pix[x, y * 2]
      #pix[x, y * 2] = (0, 20, 0)
  
  for b in range(2):
    for a in range(2):
      outname = newname.split('.')[-2]
      outext = newname.split('.')[-1]
      
      out[b][a].save(outname + '-' + str(a) + str(b) + '.' + outext)




if __name__ == '__main__':
  main()