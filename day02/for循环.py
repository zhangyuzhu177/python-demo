str = 'itheima is a brand of itcast'
sum = 0

for i in str:
    if i == 'a':
        sum += 1

print(sum)

# range() 用于生成一个不可变的整数序列（范围）
# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j * i}\t", end=" ")
    print()