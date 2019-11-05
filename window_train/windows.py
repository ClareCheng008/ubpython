import tkinter as tk
import tkinter.font as tkFont
from tkinter import*
import socket
import threading

Correcting = True
LightCleanData = [0 for i in range(6 * 6 * 4)]

rows = 6
cols = 6
array_frame = [ [tk.Frame] * rows for i in range(cols) ]
array_canvas = [ [tk.Canvas] * rows for i in range(cols) ]

def uppdate_canvas(LightData, LightCleanData, LightSensorCount):
    #print('---------------------------------------------')
    for i in range(LightSensorCount):
        a = LightCleanData[i]
        b = LightData[i]
        #print('a=', a, end=' ')
        #print('b=', b, end=' ')
        if a < b:
            cf = 0
        else:
            cf = (a - b) * 255 / a
        #print('cf=', cf, end=' ')
        c = 255 - int(cf)
        #print('c=',c)
        oval_color = "#{:0>2X}{:0>2X}{:0>2X}".format(c,c,c)
        #print("{}:".format(i) + oval_color)
        x = (i//4) // 6
        y = (i//4) % 6
        array_canvas[x][y].itemconfig("point{}".format(i%4), fill=oval_color)
    
    pass
def handle_connection(conn, addr):
    print(conn, addr)
    #print('client addr',addr)
    #print('ready to read msg')
    global Correcting
    LightSensorCount = 0
    LightData = [0 for i in range(6 * 6 * 4)]
    while True:
        client_msg=conn.recv(1024) #收消息
        if not client_msg: break
        #print('client msg: %s' %client_msg)
        array = str(client_msg, encoding="utf-8").split(':')
        #print(array)
        LightSensorCount = int(array[2])
        for i in range(3, 3 + LightSensorCount):
            LightData[i - 3] =  int(array[i])
        #print(LightData)
        #print('Correcting ' , Correcting)    
        if Correcting == True:
            print("try jiao zheng")
            Correcting = False
            LightCleanData = LightData.copy()
        '''
        print('LightData:')
        for i in range(LightSensorCount):
            print(LightData[i], end=' ')
        print('')
        print('LightCleanData:')
        for i in range(LightSensorCount):
            print(LightCleanData[i], end=' ')
        print('')
        '''
        uppdate_canvas(LightData, LightCleanData, LightSensorCount)
        
        conn.send(client_msg.upper()) #发消息
    conn.close()
def server_thread():
    phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
    phone.bind(('192.168.137.1',6999)) #插电话卡
    phone.listen(5) #开机，backlog

    while True:
        print('starting....')
        conn,addr=phone.accept() #接电话
        handle_connection(conn, addr)
    phone.close()

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
t = threading.Thread(target=server_thread)
def RunCmd():
    global on_hit
    if on_hit == False:
        on_hit = True
        strBtn.set('停止')
        t.start();
    else:
        on_hit = False
        strBtn.set('运行')
        #t.stop();


def CorrectCmd():
    global Correcting
    Correcting = True
    print('CorrectCmd Correcting ' , Correcting)
    '''
    a = 1500
    b = 1000
    if a < b:
        cf = 0
    else:
        cf = (a - b) * 255 / a
    c = 255 - int(cf)
    print('c=',c)
    print("point{}".format(5%4))
    s = "point{}".format(5%4)
    oval_color = "#{:0>2X}{:0>2X}{:0>2X}".format(c,c,c)
    array_canvas[1][2].itemconfig(s, fill=oval_color)
    '''
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
        oval0 = canvas.create_oval(x0-cw, y0-cw, x0+cw, y0+cw, fill='#FFFFFF', outline="", tags="point0")
        oval1 = canvas.create_oval(x1-cw, y1-cw, x1+cw, y1+cw, fill='#FFFFFF', outline="", tags="point1")
        oval2 = canvas.create_oval(x2-cw, y2-cw, x2+cw, y2+cw, fill='#FFFFFF', outline="", tags="point2")
        oval3 = canvas.create_oval(x3-cw, y3-cw, x3+cw, y3+cw, fill='#FFFFFF', outline="", tags="point3")
        
        array_canvas[i][j] = canvas



strLog = tk.StringVar()
edit_Port = tk.Text(window, bg='#ECECEC', font=('Arial', 5), height=15 , width=100)  # 显示成明文形式
edit_Port.grid(row=2 , columnspan=6, sticky=W, padx=10 , pady=5)



window.mainloop()





