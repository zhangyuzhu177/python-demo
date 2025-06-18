arr = ['java','python','js','golang']

# 1. index() 查找指定元素在列表的下标
print("arr.index('python') ==>",arr.index('python')) # ==> 1

# 2. 修改指定下标的值
arr[2] = 'ts'
print(arr) # ==> ['java', 'python', 'ts', 'golang']

# 3. insert() 在指定的下标位置，插入指定的元素
arr.insert(1,'html')
print(arr) # ==> ['java', 'html', 'python', 'ts', 'golang']

# 4. append() 将元素插入到列表尾部
arr.append('css')
print(arr) # ==> ['java', 'html', 'python', 'ts', 'golang', 'css']

# 5. extend() 在列表的尾部追加 '一批' 新元素
arr.extend(['a', 'b', 'c'])
print(arr) # ==> ['java', 'html', 'python', 'ts', 'golang', 'css', 'a', 'b', 'c'

# 6. 删除指定下标索引的元素
arr = ['java','python','js','golang']
# 6.1 del 列表[下标]
del arr[2]
print(arr) # ==> ['java', 'python', 'golang']
# 6.2 列表.pop(下标) 会返回取出的元素
res = arr.pop(2)
print(res) # ==> golang
print(arr) # ==> ['java', 'python']
# 6.3 列表.remove(元素) 删除某元素在列表中的第一个匹配项
arr = ['java','python','js','golang','python']
arr.remove('python')
print(arr) # ==> ['java', 'js', 'golang', 'python']

# 7. clear() 清空列表
arr.clear()
print(arr) # ==> []

# 8. count 统计列表内某个元素的数量
arr = ['java','python','js','golang','python']
count = arr.count('python')
print(count) # ==> 2
