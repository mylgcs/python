# 将一个常用的功能封装为一个单独的代码片段，用一个单词来表示，通过这个单词，只需极简结的代码，即可实现这个功能，
# 这样的代码片段，称为"函数"！
# 比如print 和 input就是函数


# 函数
def print_poetry():
    print("春眠不觉晓，处处蚊子咬，夜来嗡嗡声，叮的包不少。")


# 函数调用
print_poetry()


# 函数的参数与返回值
# 通过参数将数据传递给函数，通过返回值将运算的结果回传
def add(a, b):
    return a + b


# 运算结果可以赋值给另一个变量，也可以直接使用
c = add(1, 2)
print(c)

# 调用函数的式子，也是有值的，返回值就是函数调用表达式的值
print(add(3, 5) + 4)


# 传参可以带标签
def p_pow(num, power):
    return num ** power


print(p_pow(num=10, power=2))

