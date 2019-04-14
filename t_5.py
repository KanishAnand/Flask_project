import json

def bintodec(n):
    return int(n,2)

def dectobin(n):
    return "{0:b}".format(n)

def two_comp(lst):
	val=0
	val -= lst[4]*16
	for i in range(4):
		val += lst[i]*pow(2,i)
	return val

def one_comp(lst):
	val=0
	val -= lst[4]*16

	if lst[4] == 1:
		val += 1
	for i in range(4):
		val += lst[i]*pow(2,i)
	return val

def signed(lst):
	val=0
	for i in range(4):
		val += lst[i]*pow(2,i)
	if lst[4] == 1:
		val = -val
	return val

#MAIN
#a,b=input().split()
def fun_5bit(a,b):
	binary_sum = bintodec(a) + bintodec(b)
	val_a = int(a)
	val_b = int(b)
	i=0
	arr_a=[]
	arr_b=[]

	while i < 5: #loop to convert a and b into binary arrays
		arr_a.insert(i,val_a % 10)
		arr_b.insert(i,val_b % 10)
		val_a //= 10
		val_b //= 10
		i += 1

	result=[]
	carry=0
	i=0
	print(arr_a)
	print(arr_b)
	for i in range(5): #loop to do binary addition
		v = arr_a[i]^arr_b[i]
		c1 = arr_a[i]&arr_b[i]
		result.insert(i,v^carry)
		carry = c1^(v&carry)

	binary_val=dectobin(binary_sum)

	result_binary = binary_val
	result_unsigned = binary_sum
	print(carry)
	if carry == 1:
		result_binary = "overflow(" + str(binary_val) + ")"
	answer_binary = result_binary

	result_unsigned = binary_sum
	if binary_sum > 31:
		result_unsigned = "overflow (" + str(binary_sum) + ")"
	answer_unsigned = result_unsigned

	a_signed = signed(arr_a)
	b_signed = signed(arr_b)
	result_signed = a_signed + b_signed
	answer_signed = result_signed
	
	if(answer_signed == 0):
	 	answer_signed = '+' + str(answer_signed)

	if result_signed < -15 or result_signed > 15:
		answer_signed = "overflow (" + str(result_signed) + ")"

	a_two_comp=two_comp(arr_a)
	b_two_comp=two_comp(arr_b)
	result_two_comp=a_two_comp+b_two_comp
	answer_two_comp=result_two_comp

	a_one_comp=one_comp(arr_a)
	b_one_comp=one_comp(arr_b)
	result_one_comp=a_one_comp+b_one_comp
	answer_one_comp= result_one_comp

	if(result_two_comp < -16 or result_two_comp > 15 ):
		answer_two_comp="overflow (" + str(result_two_comp) + ")"

	if(result_one_comp < -15 or result_one_comp > 15 ):
		answer_one_comp="overflow (" + str(result_one_comp) + ")"

	while (len(answer_binary)<5):
		answer_binary='0'+answer_binary

	print("binary representation:" ,answer_binary)
	print("unsigned value:" ,answer_unsigned)
	print("signed value:" ,answer_signed)
	print("two complement value:" ,answer_two_comp)
	print("one complement value:" ,answer_one_comp)
	obj = {																#ANSWERS are being sent in the JSONified form
	'Binary Representation':answer_binary,
	'Unsigned Value':answer_unsigned,
	'Signed Value':answer_signed,
	'Signed Value':answer_signed,
	'Two Complement':answer_two_comp,
	'One Complement':answer_one_comp
	}
	jsonstr = json.dumps(obj);
	#print(jsonstr)
	return jsonstr
