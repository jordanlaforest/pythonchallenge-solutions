
import sys
import Image, ImageDraw

def connectPoints(listOfPoints, im):
  if not im:
    im = Image.new("RGB", (512, 512), (128, 128, 128))
  draw = ImageDraw.Draw(im)
  draw.line(listOfPoints, width=2)
  #draw.line([(10,20), (20,10)])
  del draw
  return im

def main():
  
  outname = sys.argv[1]
  inputnames = sys.argv[2:]
  
  img = None
  
  for inputname in inputnames:
    f = open(inputname, 'rU')
    text = f.read()
    f.close()
    data = text.split(',')
    
    
    i = 0
    length = len(data)
    
    posList = []
    while i < length:
      posList.append((int(data[i]), int(data[i+1])))
      i += 2
    img = connectPoints(posList, img)
    #print posList
    
  
  img.save(outname)
    
    
    
if __name__ == '__main__':
  main()