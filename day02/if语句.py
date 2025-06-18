import random

# age=input('请输入你的年龄：')

# if int(age)<18:
#     print("您还未成年")
# else:
#     print("您已经成年了")

# 猜数字
num = random.randint(1,10) # 生成一个 1~10 的随机数
print(num)
guess_num = int(input("请输入数字："))

if guess_num != num:
    if guess_num > num:
        print("大了")
    elif guess_num < num:
        print("小了")

else:
    print("猜对了")