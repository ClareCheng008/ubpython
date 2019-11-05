import socket

def handle_connection(conn, addr):
    print(conn)
    print('client addr',addr)
    print('ready to read msg')
    LightSensorCount = 0
    LightData = [0 for i in range(6 * 6 * 4)]
    while True:
        client_msg=conn.recv(1024) #收消息
        if not client_msg: break
        print('client msg: %s' %client_msg)
        array = str(client_msg, encoding="utf-8").split(':')
        print(array)
        LightSensorCount = int(array[2])
        for i in range(3, 3 + LightSensorCount):
            LightData[i - 3] =  int(array[i])
        print(LightData)
        conn.send(client_msg.upper()) #发消息

    conn.close()



phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.bind(('192.168.137.1',6999)) #插电话卡
phone.listen(5) #开机，backlog

while True:
    print('starting....')
    conn,addr=phone.accept() #接电话
    handle_connection(conn, addr)
phone.close()
