# 创建移动
import tkinter as tk
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


# -------- #
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

    # pimg_hero = ImageTk.PhotoImage(img_hero)
    canvas.move(hero, x, y)


# 设置键盘监听
entry = tk.Frame(window)
entry.bind('<Key>', fly_control)
entry.focus_set()
entry.pack()
# -------- #

window.mainloop()
