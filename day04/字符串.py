my_str = 'itheima and itcast'

# index() 查找指定字符串的起始下标
print(my_str.index('and')) # ==> 8

# replace() 替换指定字符串，返回新的字符串
str2=my_str.replace('it','ab')
print(str2) # ==> abheima and abcast

# split() 将字符串在指定位置进行分割，并返回一个列表
str3 =my_str.split('and')
print(str3) # ==> ['itheima ', ' itcast']

# strip() 字符串规整操作
# 1. 去除前后空格
str4 = '  itheima and itcast  '
print(str4.strip()) # ==> itheima and itcast
# 2. 去除前后指定字符串
str5 = 'abitheima and itcastab'
print(str5.strip('ab')) # ==> itheima and itcast