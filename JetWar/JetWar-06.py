# 发射子弹
import tkinter as tk, time, threading
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
def fly_control(event):
    x, y = 0, 0
    speed = 2
    if event.char == "a":
        x = -1 * speed
    if event.char == "d":
        x = 1 * speed
    if event.char == "w":
        y = -1 * speed
    if event.char == "s":
        y = +1 * speed
    if event.char == "j":
        shoot()

    # pimg_hero = ImageTk.PhotoImage(img_hero)
    canvas.move(hero, x, y)


# 设置键盘监听
entry = tk.Frame(window)
entry.bind('<Key>', fly_control)
entry.focus_set()
entry.pack()


img_b = Image.open("Images/bullet1.png")
# 重制图片大小
img_b = img_b.resize((5, 11), Image.ANTIALIAS)
# 创建相框
pimg_b = ImageTk.PhotoImage(img_b)
# 用画布，将pimg_bg画出来
# 100，100是pimg_gb绘制时中心点位置
b_list = []
for i in range(10):
    #将创建的子弹添加到b_list里
    b_list.append([canvas.create_image(480 / 2, -200, image=pimg_b), -200])


# -------- #
def do_action():
    global b_list
    while True:
        time.sleep(0.1)
        for b in b_list:
            if b[-1] > -199:
                canvas.move(b[0], 0, -10)
                b[-1] += -10


# 启动线程
t = threading.Thread(target=do_action)
t.start()

# 射击
def shoot():
    global b_list
    for b in b_list:
        if b[-1] < -150:
            canvas.move(b[0], 0, +800)
            b[-1] += 800
            break
# -------- #

window.mainloop()
