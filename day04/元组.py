"""
练习案例：元组的基本操作
定义一个元组，内容是：（周杰轮，11,[football，'music]），记录的是一个学生的信息（姓名、年龄、爱好）
请通过元组的功能（方法），对其进行
"""

# 元组内容不能修改，如何元组内嵌套了数组列表，可以修改这个数组列表

arr = ('周杰伦', 11, ['football', 'music'])

# 1．查询其年龄所在的下标位置
print(arr[1])
# 2.查询学生的姓名
print(arr[0])
# 3.删除学生爱好中的football
arr[2].pop(0)
print(arr)
# 4.增加爱好：coding到爱好list内
arr[2].append('coding')
print(arr)
