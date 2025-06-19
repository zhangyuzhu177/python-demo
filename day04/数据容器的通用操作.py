my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = 'abcde'
my_set = {1, 2, 3, 4, 5}
my_dict = {'key1':1, 'key2':2,'key3':3,'key4':4,'key5':5,}

# len 元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

# max 最大元素
print(f"列表 最大元素是：{max(my_list)}")
print(f"元组 最大元素是：{max(my_tuple)}")
print(f"字符串 最大元素是：{max(my_str)}")
print(f"集合 最大元素是：{max(my_set)}")
print(f"字典 最大元素是：{max(my_dict)}")

# min 最小元素
print(f"列表 最小元素是：{min(my_list)}")
print(f"元组 最小元素是：{min(my_tuple)}")
print(f"字符串 最小元素是：{min(my_str)}")
print(f"集合 最小元素是：{min(my_set)}")
print(f"字典 最小元素是：{min(my_dict)}")

# 类型转换：容器列表
print(f"列表 转列表的结果是：{list(my_list)}")
print(f"元组 转列表的结果是：{list(my_tuple)}")
print(f"字符串 转列表的结果是：{list(my_str)}")
print(f"集合 转列表的结果是：{list(my_set)}")
print(f"字典 转列表的结果是：{list(my_dict)}")

# 类型转换：容器转元组
print(f"列表 转元组的结果是：{tuple(my_list)}")
print(f"元组 转元组的结果是：{tuple(my_tuple)}")
print(f"字符串 转元组的结果是：{tuple(my_str)}")
print(f"集合 转元组的结果是：{tuple(my_set)}")
print(f"字典 转元组的结果是：{tuple(my_dict)}")

# 类型转换：容器转字符串
print(f"列表 转字符串的结果是：{str(my_list)}")
print(f"元组 转字符串的结果是：{str(my_tuple)}")
print(f"字符串 转字符串的结果是：{str(my_str)}")
print(f"集合 转字符串的结果是：{str(my_set)}")
print(f"字典 转字符串的结果是：{str(my_dict)}")

# 类型转换：容器转集合
print(f"列表 转集合的结果是：{set(my_list)}")
print(f"元组 转集合的结果是：{set(my_tuple)}")
print(f"字符串 转集合的结果是：{set(my_str)}")
print(f"集合 转集合的结果是：{set(my_set)}")
print(f"字典 转集合的结果是：{set(my_dict)}")

# sorted排序 排序结果会变成列表对象 reverse=True 表示降序排序
my_list = [5, 1, 4, 2, 3]
my_tuple = (5, 1, 4, 2, 3)
my_str = 'djshafds'
my_set = {5, 1, 4, 2, 3}
my_dict = {'key1':1, 'key5':5, 'key3':3,'key2':2,'key4':4,}

print(f"列表 对象排序的结果是：{sorted(my_list)}")
print(f"元组 对象排序的结果是：{sorted(my_tuple)}")
print(f"字符串 对象排序的结果是：{sorted(my_str)}")
print(f"集合 对象排序的结果是：{sorted(my_set)}")
print(f"字典 对象排序的结果是：{sorted(my_dict)}")

