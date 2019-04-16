import json
import requests
# headers = {
# 	'Content-Type': 'application/json',
# }
URL = "http://localhost:5000/calculate"
no_1="1000"
no_2="1010"
PARAMS = {"var_1":no_1,"var_2":no_2}
#print(PARAMS)
#PARAMS = json.dumps(PARAMS)
#print(PARAMS)
r = requests.get(url = URL,json = PARAMS)
data=r.json()
#print(data['Binary Representation'])
print("#1 Test Case : 1000 1010")
if data['Binary Representation'] == "overflow (10010)" and data['Unsigned Value'] == "overflow (18)" and data['Signed Value'] == -2 and data['Two Complement'] == "overflow (-14)" and data['One Complement'] == "overflow (-12)":
	print('#1 Test Case Passed')
else:
	print('#1 Test Case Failed')
