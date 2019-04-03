def two_comp(lst):
	val=0
	val -= lst[3]*8
	for i in range(3):
		val += lst[i]*pow(2,i)
	return val

def one_comp(lst):
	val=0
	val -= lst[3]*8 

	if lst[3] == 1:
		val += 1
	for i in range(3):
		val += lst[i]*pow(2,i)
	return val

def signed(lst):
	val=0
	for i in range(3):
		val += lst[i]*pow(2,i)
	if lst[3] == 1:
		val = -val
	return val

a,b=input().split()

c = int(a,2) + int(b,2)
a=int(a)
b=int(b)
val_a = a
val_b = b
i=0
arr_a=[]
arr_b=[]

while i < 4:
	arr_a.insert(i,val_a % 10)
	arr_b.insert(i,val_b % 10)
	val_a //= 10
	val_b //= 10
	i += 1

result=[]
carry=0
i=0

for i in range(4):
 	result.insert(i,arr_a[i]^arr_b[i]^carry)
 	carry = arr_a[i]&arr_b[i]

result_binary=""

# for i in result:
# 	s = str(i)
# 	print(s)
# 	result_binary  = int("".join(s))
# 	print(result_binary)
# print(result)
# result_binary = result_binary.join(result)

result_unsigned = c

if carry == 1:
	result_binary = "overflow"
if c > 15:
	result_unsigned = "overflow"

a_signed = signed(arr_a)
b_signed = signed(arr_b)
result_signed = a_signed + b_signed

if result_signed < -7 or result_signed > 7:
	result_signed = "overflow"

a_two_comp=two_comp(arr_a)
b_two_comp=two_comp(arr_b)
result_two_comp=a_two_comp+b_two_comp

a_one_comp=one_comp(arr_a)
b_one_comp=one_comp(arr_b)
result_one_comp=a_one_comp+b_one_comp

if(result_two_comp < -8 or result_two_comp > 7 ):
	result_two_comp="overflow"

if(result_one_comp < -7 or result_one_comp > 7 ):
	result_one_comp="overflow"

#print("binary value:" ,result_binary)
print("unsigned value:" ,result_unsigned)
print("signed value:" ,result_signed)
print("two complement value:" ,result_two_comp)
print("one complement value:" ,result_one_comp)
