"""
练习案例：分割字符串
给定一个字符串："itheimaitcastboxuegu"
"""

str1 = 'itheima itcast boxuegu'

# 计字符串内有多少个"it"字符
print(str1.count('it'))

# 将字符串内的空格，全部替换为字符："|"
str1 = str1.replace(' ', '|')
print(str1)

# 按照进行字符串分割，得到列表
arr = str1.split('|')
print(arr)