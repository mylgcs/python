# while循环
# 打印5个 "大潘老师真帅"
a = 0
while a < 5:
    print(a)
    a += 1

# 从1 打印到 20
a = 1
while a < 20:
    print(a)
    a += 1

# 从20打到1
a = 20
while a >= 1:
    print(a)
    a -= 1

# break 和 continue
a = 1
while a < 20:
    if a == 15:
        break
    print(a)
    a += 1