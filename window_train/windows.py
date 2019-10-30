import tkinter as tk
import tkinter.font as tkFont
from tkinter import*

window = tk.Tk()

window.title('Free Runner')

window.geometry('650x800')

ft = tkFont.Font(family='Arial', size=14 , weight=tkFont.BOLD)
strBtn = tk.StringVar()
strBtn.set('运行')
lbl_IP = tk.Label(window, text='IP:', font=ft, width=3)
edit_IP = tk.Entry(window, show=None, font=ft , width=15)  # 显示成明文形式
lbl_Port = tk.Label(window, text='Port:', font=ft)
edit_Port = tk.Entry(window, show=None, font=ft, width=5)  # 显示成明文形式

on_hit = False
def RunCmd():
    global on_hit
    if on_hit == False:
        on_hit = True
        strBtn.set('停止')
    else:
        on_hit = False
        strBtn.set('运行')


def CorrectCmd():
    pass
 
# 第5步，在窗口界面设置放置Button按键
cntBtn = tk.Button(window, textvariable=strBtn, font=ft, command=RunCmd, width=10, height=1)
cliBtn = tk.Button(window, text='矫正', font=ft, command=CorrectCmd, width=10, height=1)

lbl_IP.grid(row=0, column=0, sticky=E, pady=10)
edit_IP.grid(row=0, column=1, sticky=W, pady=10)
lbl_Port.grid(row=0, column=2, sticky=E, pady=10)
edit_Port.grid(row=0, column=3, sticky=W, pady=10)
cntBtn.grid(row=0, column=4, sticky=E, padx=5)
cliBtn.grid(row=0, column=5, sticky=E)

framshow = tk.Frame(window, width=620, height=700)
framshow.grid(row=1 , columnspan=6, padx=13, pady=5)

rows = 6
cols = 6
array_frame = [ [tk.Frame] * rows for i in range(cols) ]
array_canvas = [ [tk.Canvas] * rows for i in range(cols) ]
for i in range(0, rows):
    for j in range(0, cols):
        frame = tk.Frame(framshow, width=100, height=100)
        frame.grid(row=i, column=j)
        array_frame[i][j] = frame
        #pass        

x0=50    #圆心横坐标
y0=25    #圆心纵坐标

x1=75    #圆心横坐标
y1=50    #圆心纵坐标

x2=50    #圆心横坐标
y2=75    #圆心纵坐标

x3=25    #圆心横坐标
y3=50    #圆心纵坐标

cw=7
for i in range(0, rows):
    for j in range(0, cols):
        canvas = tk.Canvas(array_frame[i][j], bg='#87CEFA', width=100, height=100)
        canvas.pack()
        oval0 = canvas.create_oval(x0-cw, y0-cw, x0+cw, y0+cw, fill='#111111', outline="")
        oval1 = canvas.create_oval(x1-cw, y1-cw, x1+cw, y1+cw, fill='#555555', outline="")
        oval2 = canvas.create_oval(x2-cw, y2-cw, x2+cw, y2+cw, fill='#999999', outline="")
        oval3 = canvas.create_oval(x3-cw, y3-cw, x3+cw, y3+cw, fill='#DDDDDD', outline="")
        
        array_canvas[i][j] = canvas



strLog = tk.StringVar()
edit_Port = tk.Text(window, bg='#ECECEC', font=('Arial', 5), height=15 , width=100)  # 显示成明文形式
edit_Port.grid(row=2 , columnspan=6, sticky=W, padx=10 , pady=5)

window.mainloop()
