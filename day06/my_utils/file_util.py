def print_file_info(path):
    """
    读取文件内容
    :param path:
    :return:
    """
    file = None
    try:
        file = open(path, 'r', encoding='utf-8')
        print(file.read())
    except FileNotFoundError as e:
        print(e)
    finally:
        if file:
            file.close()

def append_to_file(path,data):
    """
    将数据追加写入到文件中
    :param path:
    :param data:
    :return:
    """
    file =None
    try:
        file = open(path, 'w')
        file.write(data)
    except FileNotFoundError as e:
        print(e)
    finally:
        if file:
            file.close()
