from my_utils import str_util, file_util

if __name__ == '__main__':
    str1 = str_util.str_reverse('dlrow olleh')
    print(str1)

    str2 = str_util.substr('hello world', 0,5)
    print(str2)

    file = file_util.print_file_info('test.txt')
    print(file)

    file_util.append_to_file('test.txt','hello world')
