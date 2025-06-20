import json

obj = [
    {
        "name": "张三",
        "age": 18,
    },
    {
        "name": "ls",
        "age": 19,
    },
    {
        "name": "ww",
        "age": 20,
    }
]
# 将列表转为json数据 ensure_ascii=False 确保中文可以成功转换
print(json.dumps(obj, ensure_ascii=False))

# 将json数据转为python数据类型
s = '[{"name": "张三", "age": 18}, {"name": "ls", "age": 19}, {"name": "ww", "age": 20}]'
print(json.loads(s))

