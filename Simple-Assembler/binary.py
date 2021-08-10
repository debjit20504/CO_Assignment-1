def addition():
	reg2 = int(input())
	reg3 = int(input())
	reg1 = reg2 + reg3
	print('00000'+'00'+bin(reg1)+bin(reg2)+bin(reg3))
def main():
	addition()

if __name__ == '__main__':
	main()
