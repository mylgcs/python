# 创建窗口
import tkinter as tk,time,threading
from PIL import Image,ImageTk

window = tk.Tk()

# window.geometry("480x852")
window.title("飞机大战")

# 创建背景画布
canvas = tk.Canvas(window,width=480,height=852)
canvas.pack()
# 创建一个图片对象
img_bg = Image.open("Images/background.png")
# 重置图片大小
img_bg = img_bg.resize((480,852),Image.ANTIALIAS)
# 创建相框
img_bg = ImageTk.PhotoImage(img_bg)
# 用画布，将pimg_bg画出来
# 100，100是pimg_gb绘制时中心点位置
canvas.create_image(480/2,852/2,image=img_bg)


# 创建一个图片对象
img_hero = Image.open("Images/hero1.png")
# 重置图片大小
img_hero = img_hero.resize((102,126),Image.ANTIALIAS)
# 创建相框
img_hero = ImageTk.PhotoImage(img_hero)
# 用画布，将pimg_bg画出来
# 100，100是pimg_gb绘制时中心点位置
hero = canvas.create_image(480/2,800 - 100,image=img_hero)

# 飞行控制
jjet_x = 480 / 2
def fly_control(event):
    global jet_x
    x, y = 0, 0
    speed = 2
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


# -------- #
num = 0
def do_action():
    global b_list, num
    while True:
        time.sleep(0.1)
        num += 1
        if num % 10 == 0:
            shoot()
        for b in b_list:
            if b[-1] > -199:
                canvas.move(b[0], 0, -20)
                b[-1] += -20


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
# -------- #


window.mainloop()
