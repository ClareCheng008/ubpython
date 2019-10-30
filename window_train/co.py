from tkinter import *

tk=Tk()
var=IntVar()

#标签控件，显示文本和位图，展示在第一行
Label(tk,text="First").grid(row=0,sticky=E)#靠右
Label(tk,text="Second").grid(row=1,sticky=W)#第二行，靠左

#输入控件
Entry(tk).grid(row=0,column=1)
Entry(tk).grid(row=1,column=1)

button=Checkbutton(tk,text="Precerve aspect",variable=var)
button.grid(columnspan=2,sticky=W)

#主事件循环
mainloop()
