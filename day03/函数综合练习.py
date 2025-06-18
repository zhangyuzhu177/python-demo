"""
黑马ATM
- 定义一个全局变量：money用来记录银行卡余额（默认5000000）
- 定义一个全局变量：name用来记录客户姓名（启动程序时输入）
- 定义如下的函数：
    - 询余额函数
    - 存款函数
    - 存款函数
    - 菜单函数
- 要求：
- 程序启动后要求输入客户姓名
- 查询余额、存款、取款后都会返回主菜单
- 存款、取款后，都应显示一下当前余额
- 客户选择退出或输入错误，程序会退出，否则一直运行
"""

money = 5000000
name = input("请输入您的姓名：")

def main() :
    print(f"""
---------------- 主菜单 ----------------
{name}，您好，欢迎来到黑马银行ATM，请选择操作：
查询余额 \t【1】
存款 \t【2】
取款 \t【3】
退出 \t【4】
    """)

def query_money(flag) :
    if flag :
     print("------------- 查询余额 -------------")
    print(f"{name},您好，您的余额剩余：{money}元")

def get_money() :
    print("------------- 取款 -------------")
    global money
    money -= float(input('请输入取款金额:'))
    query_money(False)

def set_money() :
    print("------------- 存款 -------------")
    global money
    money += float(input('请输入存款金额:'))
    query_money(False)

while True:
    main()
    num = input("请输入您的选择:")
    if num == '1':
        query_money(True)
        continue
    elif num == '2':
        set_money()
        continue
    elif num == '3':
        get_money()
        continue
    else :
        print("期待下次使用")
        break


