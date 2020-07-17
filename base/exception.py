try:
    b = [13, 15, 20]
    # c = b.method_a()
    # a = b[4]
    # a = 10 / 0
except ZeroDivisionError as e:  # 少し重い
    import traceback

    traceback.print_exc()
    # print(e, type(e))
    pass
except IndexError as e:
    print("IndexError発生")
except Exception as e:
    print("Exeption", e, type(e))
else:
    print("else処理")  # try とelseで処理を分ける。重い処理はelseを使う
finally:
    print("finally処理")
print("処理が完了されました")
