import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.bind(('192.168.137.1',6999)) #插电话卡

phone.listen(5) #开机，backlog

print('starting....')
conn,addr=phone.accept() #接电话
print(conn)
print('client addr',addr)
print('ready to read msg')
while True:
    client_msg=conn.recv(1024) #收消息
    print('client msg: %s' %client_msg)
    conn.send(client_msg.upper()) #发消息

conn.close()
phone.close()
