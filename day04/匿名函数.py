def test(compute) :
    res = compute(1,2)
    print(res)

# 通过lambda匿名函数形式，将匿名函数作为参数传入
test(lambda a,b: a+b)