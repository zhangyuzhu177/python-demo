# 将数字类型转换成字符串
num = 1024
num_str = str(num)
print(type(num_str), num_str) # ==> <class 'str'> 1024

# 将字符串转换为数字
string = '1024'
num_int = int(string)
print(type(num_int), num_int) # ==> <class 'int'> 1024

# 将字符串转为浮点数
num2 = '10.24'
num2_float = float(num2)
print(type(num2_float), num2_float) # ==> <class 'float'> 10.24
