# 传入不可变参数
# pass: 表示占位符，没有任何实际意义，防止程序报错
# 里面的参数不可以在函数外部使用
def cook(food):
    # 改变传入的参数的数据
    food += '油菜'
    print(food)
# 定义需要传入的参数
vege = '香菇'
# 传入参数
cook(vege)
# 在函数外面打印传入的参数
# 如果传入的参数是不可变参数
# 函数里面的形参做出改变 不会影响到外面的实参
print(vege)





