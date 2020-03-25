import tkinter as tk
from PIL import Image,ImageTk

# 创建窗口
window = tk.Tk()
# 设置标题
window.title("hello python")
# 设置大小
window.geometry("800x600")

# 设置文字变量
label_text = tk.StringVar()
# 创建标签对象，配置背景色，宽度和高度
# label = tk.Label(textvar=label_text,bg="bull",width=30,height=2)
label = tk.Label(textvar=label_text, bg="red", width=30, height=2)
# 将标签添加到窗口
label.pack()
# 添加文字标签
label_text.set("这是一个文字标签")
# 创建一个函数
on = False
def button_on_click():
    global on # 在函数里面，获取函数外面的变量
    if on == False:
        label_text.set("python棒棒哒")
        on = True
    else:
        label_text.set("我学习，我骄傲")
        on = False

# 创建一个button
button = tk.Button(text="touch me", width=20, height=3, command=button_on_click)
button.pack()
# 创建画布
canvas = tk.Canvas(window,width=800,height=600)
canvas.pack()
# 绘制三种色彩的矩形
canvas.create_rectangle(100,50,300,150,fill='red')
canvas.create_rectangle(150,100,350,200, fill='blue')
canvas.create_rectangle(200,150,400,250, fill='green')

# 创建图片
img = Image.open('tu1.png')
img = img.resize((300, 300), Image.ANTIALIAS)
pimg = ImageTk.PhotoImage(img)
canvas.create_image(600, 200, image=pimg)
# 显示窗口
window.mainloop()