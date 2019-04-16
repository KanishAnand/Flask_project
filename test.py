import json
import requests

URL = "http://localhost:5000/calculate"
no_1="1000"
no_2="1010"
PARAMS = {"var_1":no_1,"var_2":no_2}

r = requests.get(url = URL,json = PARAMS)
data=r.json()

#TESTCASES-4bit
print("#1 Test Case : 1000 1010")
if data['Binary Representation'] == "overflow (10010)" and data['Unsigned Value'] == "overflow (18)" and data['Signed Value'] == -2 and data['Two Complement'] == "overflow (-14)" and data['One Complement'] == "overflow (-12)":
	print('#1 Test Case Passed')
else:
	print('#1 Test Case Failed')
#------------------------------------------------------
no_1="0010"
no_2="0100"
PARAMS = {"var_1":no_1,"var_2":no_2}

r = requests.get(url = URL,json = PARAMS)
data=r.json()

print("#2 Test Case : 0010 0100")
if data['Binary Representation'] == '0110' and data['Unsigned Value'] == 6 and data['Signed Value'] == 6 and data['Two Complement'] == 6 and data['One Complement'] == 6:
	print('#2 Test Case Passed')
else:
	print('#2 Test Case Failed')
#-------------------------------------------------------
no_1="1110"
no_2="1111"
PARAMS = {"var_1":no_1,"var_2":no_2}

r = requests.get(url = URL,json = PARAMS)
data=r.json()
print("#3 Test Case : 1110 1111")
if data['Binary Representation'] == "overflow (11101)" and data['Unsigned Value'] == "overflow (29)" and data['Signed Value'] == "overflow (-13)" and data['Two Complement'] == -3 and data['One Complement'] == -1:
	print('#3 Test Case Passed')
else:
	print('#3 Test Case Failed')

#TESTCASES-5BIT
URL = "http://localhost:5000/calculate_5bit"
no_1="10010"
no_2="11110"
PARAMS = {"var_1":no_1,"var_2":no_2}

r = requests.get(url = URL,json = PARAMS)
data=r.json()

print("#4 Test Case : 10010 11110")
if data['Binary Representation'] == 'overflow (110000)' and data['Unsigned Value'] == "overflow (48)" and data['Signed Value'] == "overflow (-16)" and data['Two Complement'] == -16 and data['One Complement'] == -14:
	print('#4 Test Case Passed')
else:
	print('#4 Test Case Failed')
#----------------------------
no_1="00001"
no_2="11101"
PARAMS = {"var_1":no_1,"var_2":no_2}

r = requests.get(url = URL,json = PARAMS)
data=r.json()

print("#5 Test Case : 00001 11101")
if data['Binary Representation'] == '11110' and data['Unsigned Value'] == 30 and data['Signed Value'] == -12 and data['Two Complement'] == -2 and data['One Complement'] == -1:
	print('#5 Test Case Passed')
else:
	print('#5 Test Case Failed')
