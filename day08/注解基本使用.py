from typing import Union


class MyClass:
    my_list: list[int] = [1,2,3]
    my_tuple: tuple[int] = (1,2,3)
    my_set: set[int] = {1,2,3}
    my_dict: dict[str,str] = {"name":'zs'}
    my_str: str = 'zs'

my_class = MyClass()


# Union 联合类型
obj: dict[str,Union[str,int]] = {
    'name':'zs',
    'age': 28
}