import socket
import threading
import time
import queue

q=queue.Queue()

ip='192.168.0.110'
port=1351
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
rep=s.connect_ex((ip,port))

def portscan():
    while not q.empty():
        ip = '192.168.0.110'
        port = q.get()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        rep = s.connect_ex((ip, port))
        if rep == 0:
            file=open('open.txt','a+')
            file.write(str(port)+"\n")
            file.close()
        else:
            print(str(port)+"| close" + "\n")
            time.sleep(0.2)
        s.close()

if __name__ == '__main__':
    for port in range(1,65536):
        q.put(port)
    for i in range(20):
        sl=threading.Thread(target=portscan)
        sl.start()




















