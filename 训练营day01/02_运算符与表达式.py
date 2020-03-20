# python语言支持使用一些符号来表示特定的运算逻辑，这些符号被称为运算符，运算符和变量、常量
# 共同组成了表达式

# 算术运算符
print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 ** 5)
print(3 / 5)
print(3 // 5)
print(3 % 5)

# 关系运算符
print(3 > 5, 3 < 5, 3 >= 5, 3 <= 5, 3 == 5, 3 != 5)

# 赋值运算符
a = 4
a += 3
print(a)

# 逻辑运算符
print(3 < 5 and 3 != 5)
print(3 < 5 or 3 != 5)
print(not 3 < 5, not 3 != 5)

# 运算符优先级
# ** 大于 * / % // 大于 > < >= <= 大于 == ！= 大于 = %= /= //= -= += *= **= 大于 not 大于 and 大于 or