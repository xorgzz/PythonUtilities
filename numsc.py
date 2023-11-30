#/usr/bin/python3
import sys

def hex2nums(hexval):
	decval = int(hexval, 16)
	print (f"dec:\t{decval}")
	print (f"oct:\t{oct(decval)}")
	print (f"bin:\t{bin(decval)}")

def oct2nums(octval):
	decval = int(octval, 8)
	print (f"dec:\t{decval}")
	print (f"hex:\t{hex(decval)}")
	print (f"bin:\t{bin(decval)}")

def bin2nums(binval):
	decval = int(binval, 2)
	print (f"dec:\t{decval}")
	print (f"oct:\t{oct(decval)}")
	print (f"hex:\t{hex(decval)}")

def dec2nums(decval):
	print (f"oct:\t{oct(decval)}")
	print (f"hex:\t{hex(decval)}")
	print (f"bin:\t{bin(decval)}")


def main():
	if len(sys.argv) == 3:
		try:
			if (sys.argv[1] == "hex"):
				hex2nums(sys.argv[2])
			elif (sys.argv[1] == "oct"):
				oct2nums(sys.argv[2])
			elif (sys.argv[1] == "dec"):
				dec2nums(int(sys.argv[2]))
			elif (sys.argv[1] == "bin"):
				bin2nums(sys.argv[2])
			else: print ("[!] invalid value of first argument [!]\n\tallowed argmunets:\n\t--->\tdec - decimal\n\t--->\t"+
						 "hex - hexadecimal\n\t--->\toct - octal\n\t--->\tbin - binary")
		except ValueError:
			print ("[!] invalid number value [!]\n\tallowed argmunets:\n\t--->\tdec - [0-9]\n\t--->\t"+
					"hex - [0-f]\n\t--->\toct - [0-7]\n\t--->\tbin - [0-1]")
	else: print ("[!] invalid amount of arguments [!]\n\teg. numsc (bin/oct/dec/hex) number")

if __name__ == '__main__':
	main()
