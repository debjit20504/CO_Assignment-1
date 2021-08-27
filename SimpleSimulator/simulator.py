import matplotlib.pyplot
import sys

Reg = ["0000000000000000", "0000000000000000", "0000000000000000", "0000000000000000", "0000000000000000",
		"0000000000000000", "0000000000000000", "0000000000000000"]

def s_bit_converter(b):
	a = int(b)
	bnr = bin(a).replace('0b', '')
	x = bnr[::-1]
	while len(x) < 16:
		x += '0'
	bnr = x[::-1]
	return bnr


def e_bit_converter(b):
	a = int(b)
	bnr = bin(a).replace('0b', '')
	x = bnr[::-1]
	while len(x) < 8:
		x += '0'
	bnr = x[::-1]
	return bnr

def add(s,PC,c,ptr,cycles):
	if int(Reg[int(s[10:13], 2)], 2) + int(Reg[int(s[13:16], 2)], 2) > 65535:
		Reg[7] = "0000000000001000"
	else:
		Reg[7] = "0000000000000000"
		Reg[int(s[7:10], 2)] = s_bit_converter(int(Reg[int(s[10:13], 2)], 2) + int(Reg[int(s[13:16], 2)], 2))
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def sub(s,PC,c,ptr,cycles):
	if int(Reg[int(s[10:13], 2)], 2) - int(Reg[int(s[13:16], 2)], 2) < 0:
		Reg[7] = "0000000000001000"
	else:
		Reg[7] = "0000000000000000"
		Reg[int(s[7:10], 2)] = s_bit_converter(int(Reg[int(s[10:13], 2)], 2) - int(Reg[int(s[13:16], 2)], 2))
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def mul(s,PC,c,ptr,cycles):
	if int(Reg[int(s[10:13], 2)], 2) * int(Reg[int(s[13:16], 2)], 2) > 65535:
		Reg[7] = "0000000000001000"
	else:
		Reg[7] = "0000000000000000"
		Reg[int(s[7:10], 2)] = s_bit_converter(int(Reg[int(s[10:13], 2)], 2) * int(Reg[int(s[13:16], 2)], 2))
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def xor(s,PC,c,ptr,cycles):
	Reg[7] = "0000000000000000"
	Reg[int(s[7:10], 2)] = s_bit_converter(int(Reg[int(s[10:13], 2)], 2) ^ int(Reg[int(s[13:16], 2)], 2))
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def Or(s,PC,c,ptr,cycles):
	Reg[7] = "0000000000000000"
	Reg[int(s[7:10], 2)] = s_bit_converter(int(Reg[int(s[10:13], 2)], 2) | int(Reg[int(s[13:16], 2)], 2))
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def And():
	Reg[7] = "0000000000000000"
	Reg[int(s[7:10], 2)] = s_bit_converter(int(Reg[int(s[10:13], 2)], 2) & int(Reg[int(s[13:16], 2)], 2))
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def div(s,PC,c,ptr,cycles):
	if int(Reg[int(s[13:16], 2)], 2) == 0:
		Reg[7] = "0000000000000000"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)

	else:
		Reg[0] = s_bit_converter(int(Reg[int(s[10:13], 2)], 2) // int(Reg[int(s[13:16], 2)], 2))
		Reg[1] = s_bit_converter(int(Reg[int(s[10:13], 2)], 2) % int(Reg[int(s[13:16], 2)], 2))
		Reg[7] = "0000000000000000"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)

def Not(s,PC,c,ptr,cycles):
	Reg[7] = "0000000000000000"
	Reg[int(s[10:13], 2)] = s_bit_converter(~ int(Reg[int(s[13:16], 2)], 2))
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def cmp(s,PC,c,ptr,cycles):
	if int(Reg[int(s[10:13], 2)], 2) > int(Reg[int(s[13:16], 2)], 2):
		Reg[7] = "0000000000000010"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)

	elif int(Reg[int(s[10:13], 2)], 2) < int(Reg[int(s[13:16], 2)], 2):
		Reg[7] = "0000000000000100"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)

	else:
		Reg[7] = "0000000000000001"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)

def mov(s,PC,c,ptr,cycles):
	Reg[int(s[10:13], 2)] = Reg[int(s[13:16], 2)]
	Reg[7] = "0000000000000000"
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def mov1(s,PC,c,ptr,cycles):
	Reg[int(s[5:8], 2)] = s_bit_converter(int(s[8:16], 2))
	Reg[7] = "0000000000000000"
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def rs(s,PC,c,ptr,cycles):
	Reg[int(s[5:8], 2)] = s_bit_converter(int(Reg[int(s[5:8], 2)], 2) >> int(s[8:16], 2))
	Reg[7] = "0000000000000000"
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def ls(s,PC,c,ptr,cycles):
	Reg[int(s[5:8], 2)] = s_bit_converter(int(Reg[int(s[5:8], 2)], 2) << int(s[8:16], 2))
	Reg[7] = "0000000000000000"
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def st(s,PC,c,ptr,cycles,inp):
	inp[int(s[8:16], 2)] = Reg[int(s[5:8], 2)]
	Reg[7] = "0000000000000000"
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def ld(s,PC,c,ptr,cycles,inp):
	Reg[int(s[5:8], 2)] = inp[int(s[8:16], 2)]
	Reg[7] = "0000000000000000"
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def jmp(s,PC,c,ptr,cycles):
	Reg[7] = "0000000000000000"
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)

def jlt(s,PC,c,ptr,cycles):
	if Reg[7] == "0000000000000100":
		Reg[7] = "0000000000000000"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)
	else:
		Reg[7] = "0000000000000000"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)

def jgt(s,PC,c,ptr,cycles):
	if Reg[7] == "0000000000000010":
		Reg[7] = "0000000000000000"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)
	else:
		Reg[7] = "0000000000000000"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)

def je(s,PC,c,ptr,cycles):
	if Reg[7] == "0000000000000001":
		Reg[7] = "0000000000000000"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)
	else:
		Reg[7] = "0000000000000000"
		PC.append(e_bit_converter(ptr))
		print(
			PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[
				5] + " " +
			Reg[6] + " " + Reg[7] + "\n")
		cycles.append(c)

def hlt(s,PC,c,ptr,cycles):
	Reg[7] = "0000000000000000"
	PC.append(e_bit_converter(ptr))
	print(
		PC[c] + " " + Reg[0] + " " + Reg[1] + " " + Reg[2] + " " + Reg[3] + " " + Reg[4] + " " + Reg[5] + " " +
		Reg[6] + " " + Reg[7] + "\n")
	cycles.append(c)


def main():
	inp = []
	inp = inp[:256]
	PC = []
	cycles = []
	c = 0
	ptr = 0
	for i in range(256):
		inp.append("0000000000000000")
	ctr = 0
	f = sys.stdin.read()
	line = f.splitlines()
	for i in line:
		inp[ctr] = i
		ctr += 1
	while True:
		if ptr < ctr:
			s = inp[ptr]
			l = str(s[:5])
			if l == "00000":
				add(s,PC,c,ptr,cycles)
			elif l == "00001":
				sub(s,PC,c,ptr,cycles)
			elif l == "00010":
				mov1(s,PC,c,ptr,cycles)
			elif l == "00011":
				mov(s,PC,c,ptr,cycles)
			elif l == "00100":
				ld(s,PC,c,ptr,cycles,inp)
			elif l == "00101":
				st(s,PC,c,ptr,cycles,inp)
			elif l == "00110":
				mul(s,PC,c,ptr,cycles)
			elif l == "01000":
				rs(s,PC,c,ptr,cycles)
			elif l == "01001":
				ls(s,PC,c,ptr,cycles)
			elif l == "01010":
				xor(s,PC,c,ptr,cycles)
			elif l == "01011":
				Or(s,PC,c,ptr,cycles)
			elif l == "01100":
				And(s,PC,c,ptr,cycles)
			elif l == "00111":
				div(s,PC,c,ptr,cycles)
			elif l == "01101":
				Not(s,PC,c,ptr,cycles)
			elif l == "01110":
				cmp(s,PC,c,ptr,cycles)
			elif l == "01111":
				jmp(s,PC,c,ptr,cycles)
			elif l == "10000":
				jlt(s,PC,c,ptr,cycles)
			elif l == "10001":
				jgt(s,PC,c,ptr,cycles)
			elif l == "10010":
				je(s,PC,c,ptr,cycles)
			elif l == "10011":
				hlt(s,PC,c,ptr,cycles)
			if l == "01111" or l == "10000" or l == "10001" or l == "10010":
				if l == "01111":
					c += 1
					ptr = int(s[8:16], 2)
				else:
					if Reg[7] == "0000000000000100":
						c += 1
						ptr = int(s[8:16], 2)
					if Reg[7] == "0000000000000010":
						c += 1
						ptr = int(s[8:16], 2)
					if Reg[7] == "0000000000000001":
						c += 1
						ptr = int(s[8:16], 2)
					else:
						c += 1
						ptr += 1
			else:
				c += 1
				ptr += 1
		else:
			break

	for i in range(256):
	  print(inp[i])

	pc_2 = []
	for i in PC:
		pc_2.append(int(i, 2))

	matplotlib.pyplot.scatter(cycles, pc_2)
	matplotlib.pyplot.title('Mem_Address vs Cycles')
	matplotlib.pyplot.xlabel('Cycles')
	matplotlib.pyplot.ylabel('Mem_Address')
	matplotlib.pyplot.savefig('graph.png')
	matplotlib.pyplot.show()


if __name__ == "__main__":
	main()