
# name,age,major,address
# sam,20,AI,seoul
# robin,25,Data Science,incheon
# hong,23,web development,busan

# urllib module -> request module -> urlopen() function 

from urllib import request

# At the target server, the data file exists. 
# the data format is UTF-8 instead of ANSI
address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ddd.csv'  

url = request.urlopen(address)
data = url.read()
print(data.decode('UTF-8'))
print(type(data)) # <class 'bytes'>
data = data.decode('UTF-8')
print(type(data)) # <class 'bytes'>

data = data.split('\n')
