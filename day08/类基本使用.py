# 设计一个类
class Student:
    name = None
    gender = None

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def hai(self):
        print(f'hi大家好，我是{self}')



# 创建了类
stu1 = Student('zs','男')
stu1.name = 'zs'
stu1.gender = '男'
stu1.hai()

# 定义一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import os
        os.system('afplay /System/Library/Sounds/Ping.aiff',)

clock1 = Clock()
clock1.id = 1
clock1.price = 19.99

# clock1.ring()
