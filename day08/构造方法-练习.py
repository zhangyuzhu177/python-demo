"""
开学了有一批学生信息需要录入系统，请设计一个类，记录学生的：
姓名、年龄、地址，这3类信息
请实现：
通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
输入完成后，中使用print语句，完成信息的输出
"""

class Students:

    # 构造方法
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def notify(self,index):
        print(f'学生{index}信息录入完成，信息为：【姓名:{self.name},年龄:{self.age},地址:{self.address}】')


for i in range(1,4):
    print(f'当前录入第{i}位学生信息，总共需录入3位学生信息')
    name = input('请输入学生姓名：')
    age = input('请输入学生年龄：')
    address = input('请输入学生地址：')
    stu = Students(name,age,address)
    stu.notify(i)