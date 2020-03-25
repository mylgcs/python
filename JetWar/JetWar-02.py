# 创建背景图
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('480x852')
window.title('飞机大战')

# -------- #

# 创建一张画布
canvas = tk.Canvas(window, width=480, height=852)
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

# -------- #

window.mainloop()