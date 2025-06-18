"""
有一个列表，内容是：[21，25，21，23，22，20]，记录的是一批学生的年龄
请通过列表的功能（方法），对其进行
"""

# 1.定义这个列表，并用变量接收它
ages = [21, 25, 21, 23, 22, 20]

# 2.追加一个数字31，到列表的尾部
ages.append(31)
print(ages)

# 3.追加一个新列表[29，33，30]，到列表的尾部
ages.extend([29, 33, 30])
print(ages)

# 4.取出第一个元素（应是：21）
print(ages[0])

# 5.取出最后一个元素（应是：30）
print(ages[-1])

# 6.查找元素31，在列表中的下标位置
print(ages.index(31))


"""
定义一个列表，内容是：[1,2,3,4,5,6,7,8,9,10]
- 历列表，取出列表内的偶数，并存入一个新的列表对象中
- 使用while循环和for循环各操作一次
"""
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = []
arr3 = []
index = 0
# 使用while循环获取偶数
while index < len(arr1):
    if arr1[index] % 2 == 0:
        arr2.append(arr1[index])
    index += 1

print(arr2)

# 使用 for 循环
for i in arr1:
    if i % 2 == 0 :
        arr3.append(i)

print(arr3)