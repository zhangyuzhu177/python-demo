"""
读取bill.txt文件
将文件写出到bill.bak.txt文件作为备份
同时，将文件内标记为测试的数据行丢弃
"""

file_bak = open('bill.bak.txt','w',encoding='utf-8')

with open('bill.txt','r',encoding='utf-8') as f:
    for line in f:
        if line.find('测试') != -1 :
            continue

        file_bak.write(line)

file_bak.close()