import socket
import errno
import threading
import time


EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello world <h1>czg home</h1>-from {thread_name}'''
response_params = [
        'HTTP/1.0 200 OK',
        'Date: Sun, 27 may 2018 01:01:01 GMT',
        'Content-Type: text/html; charset=utf-8',
        'Content-Length: {length}\r\n',
        body,
]
response = '\r\n'.join(response_params)

def handle_connection(conn, addr):
    print("handle_connection ",conn, addr)
    time.sleep(10)
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    current_thread = threading.currentThread()
    content_length = len(body.format(thread_name=current_thread.name).encode())
    print(current_thread.name)
    conn.send(response.format(thread_name=current_thread.name, length=content_length).encode())
    conn.close()

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(10)
    print('http://127.0.0.1:8000')
    serversocket.setblocking(0)
              

    try:
        i = 0
        while True:
            #print("i = ", i)
            try:
                conn, address= serversocket.accept()
            except socket.error as e:
                #print("erro happen ", e.args[0])
                if e.args[0] != errno.EAGAIN:
                    pass
                    #print("raise error")
                    #raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target=handle_connection, args=(conn, address), name='thread-%s' % i)
            t.start()
    finally:
        serversocket.close()

if __name__ == '__main__':
    main()
