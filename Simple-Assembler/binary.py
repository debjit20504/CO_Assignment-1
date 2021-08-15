dic ={"add" : "00000", "sub" : "00001", "mov" : "00010",
	  "mov" : "00011", "ld" : "00100", "st" :"00101", "mul" : "00110",
	  "div" : "00111", "rs" : "01000", "ls" : "01001", "xor" : "01010",
	  "or" : "01011", "and" : "01100", "not" : "01101", "cmp" :"01110" , "jmp" : "01111",
	  "jlt" : "10000", "jgt" : "10001",
	  "je" : "10010", "hlt" : "10011"}

reg_dict = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}


def int_convert(a):
	n = bin(a).replace('0b','')
	x = n[::-1] 
	while len(x) < 8:
		x += '0'
	n = x[::-1]
	return n

def type_A(input_lst):
	if len(input_lst) == 4:
		for i in dic:
			if input_lst[0] == i:
				res = dic[i]
				res += '00'
				res += reg_dict[input_lst[1]]
				res += reg_dict[input_lst[2]]
				res += reg_dict[input_lst[3]]
				return res
	else:
		return('ERROR', input_lst)

def type_B(input_lst):
	if input_lst[0] == 'mov':
		res = '00010'
		res += reg_dict[input_lst[1]]
		res += int_convert(int(input_lst[2][1:]))
		return res
	else:
		for i in dic:
			if input_lst[0] == i: 
				res = dic[i]
				res += reg_dict[input_lst[1]]
				res += int_convert(int(input_lst[2][1:]))
				return res

def type_C(input_lst):
	if input_lst[0] == 'mov':
		res = '00011'
		res += '00000'
		res += reg_dict[input_lst[1]]
		res += reg_dict[input_lst[2]]
		return res
	else:	
		for i in dic:
			if input_lst[0] == i:
				res = dic[i]
				res += '00000'
				res += reg_dict[input_lst[1]]
				res += reg_dict[input_lst[2]]
				return res

def type_D(input_lst):
	for i in dic:
		if input_lst[0] == i: 
			res = dic[i]
			res += reg_dict[input_lst[1]]
			res += input_lst[2]
			return res

def type_E(input_lst):
	for i in dic:
		if input_lst[0] == i:
			res = dic[i]
			res += '000'
			res += input_lst[1]
			return res

def type_F(input_lst):
	res = '10011'
	res += '00000000000'
	return res
	

def main():
	f = open(r"C:\Users\Debjit\sublime\CO_M21_Assignment-main\automatedTesting\tests\assembly\errorGen\test1", "r")
	l = []
	temp = 0
	l = f.readlines()
	for i in l:
		str = ''
		for j in i:
			str += j
		input_lst = str.split()
		temp += 1

		if input_lst[0] == 'var':
				pass

		if (len(input_lst) < 2 or len(input_lst) > 5) and input_lst[0] != 'var':
			print('ERROR', input_lst)
		else:
			if input_lst[0] not in dic:
				input_lst.remove(input_lst[0])

			if input_lst[0] == 'add' or input_lst[0] == 'sub' or input_lst[0] == 'mul' or input_lst[0] == 'xor' or input_lst[0] == 'or' or input_lst[0] == 'and':
				print(type_A(input_lst))

			if input_lst[0] == 'mov':
					if input_lst[2] in reg_dict:
						print(type_C(input_lst))
					else:
						print(type_B(input_lst))

			if input_lst[0] == 'rs' or input_lst[0] == 'ls':
				print(type_B(input_lst))
		
			if input_lst[0] == 'div' or input_lst[0] == 'not' or input_lst[0] == 'cmp':
				print(type_C(input_lst))
		
			if input_lst[0] == 'ld' or input_lst[0] == 'st':
				if len(input_lst[2]) != 8:
					x = int_convert(temp)
					input_lst[2] = x
					print(type_D(input_lst))
				else:	
					print(type_D(input_lst))
		
			if input_lst[0] == 'jmp' or input_lst[0] == 'jlt' or input_lst[0] == 'jgt' or input_lst[0] == 'je':
				if len(input_lst[1]) != 8:
					x = int_convert(temp)
					input_lst[1] = x
					print(type_E(input_lst))
				else:
					print(type_E(input_lst))
		
			if input_lst[0] == 'hlt':
				print(type_F(input_lst))
				

if __name__ == '__main__':
	main()


