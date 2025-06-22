# 单继承
class Phone:
    IMEI = 1
    producer = 'ZYZ'

    def call_by_4g(self):
        print('4g通话')

class Phone2025(Phone):
    face_id = '10001'

    def call_by_5g(self):
        print(f'{self.IMEI}、{self.producer}5g通话')

phone =Phone2025()

phone.call_by_5g()

# 多继承
class NFCReader:
    nfc_type = '第五代读卡器'

    def nfc_control(self):
        print('第五代读卡器')

class RemoteControl:
    remote_type = '红外遥控器'

    def remote_control(self):
        print('红外遥控开启了')

class MyPhone(Phone,NFCReader,RemoteControl):
    # 确保类定义不会因为缺少内容而引发语法错误 ，表示无内容。空的意思
    # pass
    def call_by_5g(self):  # 重写 父类的方法
        # super() 可以读取父类的方法或属性
        super().call_by_4g() # 调用父类的方法
    # type = 'iphone15'
    # def info(self):
    #     print(f'IMEI:{self.IMEI}\nproducer:{self.producer}\nnfc_type:{self.nfc_type}\nremote_type:{self.remote_type}')

my_phone = MyPhone()
my_phone.remote_control()