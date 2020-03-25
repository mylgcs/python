# Boom!!
import tkinter as tk, time, threading, random
from PIL import Image, ImageTk

window = tk.Tk()
window.title('飞机大战')

# 创建一张画布
canvas = tk.Canvas(window, width=480, height=800)
canvas.pack()

# 创建一个图片对象
img_bg = Image.open("Images/background.png")
# 重制图片大小
img_bg = img_bg.resize((480, 852), Image.ANTIALIAS)
# 创建相框
pimg_bg = ImageTk.PhotoImage(img_bg)
# 用画布，将pimg_bg画出来
# 100，100是pimg_gb绘制时中心点位置
canvas.create_image(480 / 2, 852 / 2, image=pimg_bg)

# 创建飞机
# 创建一个图片对象
img_hero = Image.open("Images/hero1.png")
# 重制图片大小
img_hero = img_hero.resize((102, 126), Image.ANTIALIAS)
# 创建相框
pimg_hero = ImageTk.PhotoImage(img_hero)
# 用画布，将pimg_bg画出来
# 100，100是pimg_gb绘制时中心点位置
hero = canvas.create_image(480 / 2, 852 - 200, image=pimg_hero)

# 飞行控制
jet_x = 480 / 2
def fly_control(event):
    global jet_x
    x, y = 0, 0
    speed = 4
    if event.char == "a":
        x = -1 * speed
    if event.char == "d":
        x = 1 * speed
    jet_x += x

    # pimg_hero = ImageTk.PhotoImage(img_hero)
    canvas.move(hero, x, y)


# 设置键盘监听
entry = tk.Frame(window)
entry.bind('<Key>', fly_control)
entry.focus_set()
entry.pack()


img_b = Image.open("Images/bullet1.png")
# 重制图片大小
img_b = img_b.resize((10, 22), Image.ANTIALIAS)
# 创建相框
pimg_b = ImageTk.PhotoImage(img_b)
# 用画布，将pimg_bg画出来
# 100，100是pimg_gb绘制时中心点位置
b_list = []
for i in range(10):
    #将创建的子弹添加到b_list里
    b_list.append([canvas.create_image(480 / 2, -200, image=pimg_b), 480 / 2, -200])


img_e = Image.open("Images/enemy1.png")
# 重制图片大小
img_e = img_e.resize((57, 43), Image.ANTIALIAS)
# 创建相框
pimg_e = ImageTk.PhotoImage(img_e)
# 用画布，将pimg_bg画出来
# 100，100是pimg_gb绘制时中心点位置
e_list = []
for i in range(10):
    #将创建的子弹添加到b_list里
    e_list.append([canvas.create_image(480 / 2, 1000, image=pimg_e), 480 / 2, 1000])


img_boom = Image.open("Images/Boom.png")
# 重制图片大小
img_boom = img_boom.resize((57, 51), Image.ANTIALIAS)
# 创建相框
pimg_boom = ImageTk.PhotoImage(img_boom)
# 用画布，将pimg_bg画出来
# 100，100是pimg_gb绘制时中心点位置
boom_list = []
for i in range(10):
    #将创建的子弹添加到b_list里
    boom_list.append([canvas.create_image(480 / 2, 1000, image=pimg_boom), 480 / 2, 1000, 0])

num = 0
def do_action():
    global b_list, num
    while True:
        time.sleep(0.1)
        num += 1
        if num % 5 == 0:
            shoot()
        if num % 20 == 0:
            attack()

        for b in b_list:
            if b[-1] > -199:
                canvas.move(b[0], 0, -40)
                b[-1] += -40

        for e in e_list:
            if e[-1] < 999:
                canvas.move(e[0], 0, 10)
                e[-1] += 10

        attack_check()

        # -------- #
        for boom in boom_list:
            if boom[-1] > 0:
                boom[-1] -= 1
                if boom[-1] == 0:
                    canvas.move(boom[0], 0, 1000)
                    boom[-2] += 1000
        # -------- #



# 启动线程
t = threading.Thread(target=do_action)
t.start()

# 射击
def shoot():
    global b_list
    for b in b_list:
        if b[-1] < -100:
            canvas.move(b[0], jet_x - b[1],  600 - b[-1])
            b[-1] = 600
            b[1] = jet_x
            break

def attack():
    global e_list
    for e in e_list:
        if e[-1] > 900:
            x = random.randint(20, 480-20)
            canvas.move(e[0], x - e[1],  -200 - e[-1])
            e[-1] = -200
            e[1] = x
            break

# -------- #
# 爆炸
def boom(x, y):
    for boom in boom_list:
        if boom[-1] == 0:
            canvas.move(boom[0], x - boom[1], y - boom[2])
            boom[1] = x
            boom[2] = y
            boom[-1] = 3
            break
# -------- #

# 受创检测：
def attack_check():
    global e_list, b_list
    for e in e_list:
        if e[-1] < 10:
            continue
        for b in b_list:
            if -30 < e[1] - b[1] < 30 and -20 < e[-1] - b[-1] < 20:
                boom(e[1], e[2])
                canvas.move(e[0], 0, 1000)
                e[-1] += 1000
                canvas.move(b[0], 0, -1000)
                b[-1] -= 1000

# -------- #

window.mainloop()
