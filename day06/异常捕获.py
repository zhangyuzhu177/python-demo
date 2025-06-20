# 基本捕获错误 捕获所有异常 Exception 顶级异常
try :
    file=open('aaaa.txt','r',encoding='utf-8')
except Exception as e:
    print(e)
else :
    print('没有异常')
finally:
    print('有无异常最后都会执行')

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print(e)


