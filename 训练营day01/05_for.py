# 打印5个"我也很帅"
for i in range(5):
    print("我也很帅")

# 从1 打印到 20
for i in range(1, 21):
    print(i)

# 从20打到1
for i in range(20, 0, -1):
    print(i)


# break和continue
for i in range(1, 21):
    if i == 15:
        break
    print(i)