# open打开文件 'w' 模式下如果文件不存在会帮你创建文件
# w模式会清空覆盖文件

# 1.打开文件
file = open('word.txt','w')

# 2.写入文件
file.write('hello world')

# 3.内容刷新
file.flush()