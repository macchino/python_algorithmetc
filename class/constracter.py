class SampleClass:
    def __init__(self, msg, name=None):
        print("コンストラクタが呼ばれました")
        self.msg = msg
        self.name = name
        # デストラクタ

    def __del__(self):
        print("デスタラクタが実行されました")
        print("name={}".format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)


var_1 = SampleClass("Hello", "Taro")
var_1.print_msg()
var_1.print_name()
del var_1
