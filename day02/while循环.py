import random

# 猜数字
# print('猜数字游戏开始!')
# random_number = random.randint(1, 100)
# print(random_number)
# num = int(input('请输入一个数：'))

# while num != random_number:
#     if num > random_number:
#         print('猜大了')
#     elif num < random_number:
#         print('猜小了')
#
#     num = int(input('请输入一个数：'))
#
# print('猜对了！\n游戏结束！')

# 求 1-100 的和
# i = 1
# sum = 0
#
# while i <= 100:
#     sum += i
#     i = i + 1
#
# print(sum)

# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}\t", end=" ")
        j += 1

    i += 1
    print("")
