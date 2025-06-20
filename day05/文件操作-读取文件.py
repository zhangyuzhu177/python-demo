import time

# 打开文件
file =  open('text.txt','r',encoding='utf-8')

# 读取文件内容
# print(file.read())
# 读取文件的全部行，封装到列表中
# print(file.readlines())

# for循环读取文件

for line in file:
    print(line)

# 文件关闭
file.close()

# with open 语法操作文件 执行完毕会自动关闭文件
with open('text.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)

# 统计文件中 itheima 出现次数
count = 0
with open('word.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.find('itheima') != -1 :
            count += 1

print(count)