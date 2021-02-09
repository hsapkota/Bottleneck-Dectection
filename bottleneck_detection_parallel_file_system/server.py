import socket
import threading
import time
import sys, traceback

serversock = socket.socket()
host = sys.argv[1] 
port = int(sys.argv[2]) 
BUFFER_SIZE = 128 * 1024
serversock.bind((host, port))

serversock.listen(10)
print("Waiting for a connection.....")


def reader(client):
    with client,client.makefile('rb') as clientfile:
        while True:
            raw = clientfile.readline()
            if not raw: break
            filename = raw.strip().decode()
            length = int(clientfile.readline())
            # print(f'Downloading {filename}...\n  Expecting {length:,} bytes...',end='',flush=True)
            with open("received_files/"+filename,'wb') as f:
                while length:
                    chunk = min(length,BUFFER_SIZE)
                    data = clientfile.read(BUFFER_SIZE)
                    if not data: break
                    f.write(data)
                    length -= len(data)
                else: # only runs if while doesn't break and length==0
                    print('Complete')
                    continue
            # socket was closed early.
            # print('Incomplete')
            break 
    client.close()


while True:
    client, addr = serversock.accept()
    print("Got a connection from %s" % str(addr))
    client_serve_thread = threading.Thread(target=reader, args=tuple((client,)))
    client_serve_thread.start()
    time.sleep(0.001)

serversock.close()