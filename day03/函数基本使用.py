
str1 = 'python'
count = 0
def my_len(val):
    """
    检查字符串长度
    :param val: 检查的字符串
    :return: 长度
    """
    global count # 全局变量
    count = 0
    for i in val:
        count += 1
    return count
my_len(str1)
print(count)