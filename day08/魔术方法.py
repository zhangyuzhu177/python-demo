class Student:
    name = None
    age = None

    def __init__(self,name,gender):
        self.name = name
        self.age = gender

    # __str__ 魔术方法 返回类的信息
    def __str__(self):
        return f'{self.name},{self.age}'

    # __lt__ 魔术方法 < 或 >符号比较
    def __lt__(self,other):
        return self.age < other.age

    # __le__ 魔术方法 <= 或 >=比较
    def __le__(self,other):
        return self.age <= other.age

    # __eq__ 魔术方法 == 比较
    def __eq__(self, other):
        return self.age == other.age

    def hai(self):
        print(f'hi大家好，我是{self}')

stu = Student('zs',18)
print(stu)