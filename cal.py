
import sys
import calendar

def main():
  cal = calendar.Calendar()
  year = 1006
  while year <= 1996:
    if calendar.isleap(year):
      it = cal.itermonthdays2(year, 1)
      for i in it:
        if i[0] == 26 and i[1] == 0:
          print i, year
    year += 10
  
    
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