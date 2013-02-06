import sys

def main():
	num = sys.argv[1]
	sum = 0
	calcCheckSum = False
	if num == "-c":
		calcCheckSum = True
		num = sys.argv[2]
	length = len(num)
	for i in range(1, length + 1):
		c = 1
		if ((i % 2 == 0) and not calcCheckSum) or (( i % 2 == 1) and calcCheckSum):
			c = 2
		val = c * int(num[length - i])
		sum += (val % 10) + int(val / 10)
	if calcCheckSum:
		print (10 - sum % 10) % 10
	else:
		if sum % 10 == 0:
			print "Valid"
		else:
			print "Invalid"

    
if __name__ == '__main__':
  main()