"""
某公司，账户余额有1W元，给20名员工发工资。
- 员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
- 领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
- 如果工资发完了，结束发工资。
"""

import random

money = 10000

for i in range(0, 20):
    random_num = random.randint(1,10)
    if random_num < 5 :
        print(f"员工{i},绩效{random_num},低于5，不发工资，下一位。")
        continue
    if money <= 0:
        print("工资发完了，下个月领取吧。")
        break
    money -= 1000
    print(f"员工{i}，绩效{random_num}，发放工资1000元，账户余额{money}")

print(money)