from my_module1 import func1

func = func1(1,2)
print(func)

print(__name__)

# 导入自己的packages包
import my_package.module1
import my_package.module2

func1 = my_package.module1.func1(1,2)
func2 = my_package.module2.func2(1,2)

if __name__ == '__main__':
    print(func1)
    print(func2)
