def func1():
    print('func1开始')
    num = 1/0
    print('func1结束')

def func2():
    print('func2开始')
    func1()
    print('func2结束')

# 在main函数中进行异常捕获
def main():
    try:
       func2()
    except Exception as e:
        print(e)


main()