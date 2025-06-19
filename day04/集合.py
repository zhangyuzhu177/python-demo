# 集合是无序的并且不能重复会去重

# 定义集合
my_set1 = {'java','python','javascript','python'}
my_set2 = set()
print(my_set1)

# 添加新元素
my_set1.add('html')
print(my_set1)

# 移除新元素
my_set1.remove('python')
print(my_set1)

# 随机取出一个元素
# print(my_set1.pop())

# 清空集合
# my_set1.clear()

# 取2个集合的差集
my_set3 = my_set1.difference(my_set2)
print(my_set1)
# 消除2个集合的差集
my_set2.difference_update(my_set1)

# 2个集合合并为1个
my_set5 = my_set1.union(my_set2)
print(my_set5)
# 统计集合元素的数量
# len()
# 集合的遍历
for item in my_set1:
    print(item)

