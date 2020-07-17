def generator(max):
    print("ジェネレーター作成")
    for n in range(max):
        try:
            x = yield n
            print("x={}".format(x))
            print("Yield実行")
        except ValueError as e:
            print("throwを実行しました")


gen = generator(10)
next(gen)
gen.send(100)
# gen.throw(ValueError("Invalid Value"))
# gen.close()
next(gen)
# next()で実行
# n = next(gen)
# print("n={}".format(n))
# n = next(gen)
# print("n={}".format(n))

# for文でgenerator実行
# for x in gen:
#     print("x={}".format(x))
