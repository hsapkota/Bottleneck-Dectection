import socket
import threading
import os
import time
import sys, traceback
total_transferred_data=0
last_transfered = 0
transfer_done = False
class MonitorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        global total_transferred_data, last_transfered, transfer_done
        while(1):
            if transfer_done:
                break
            thrput = (total_transferred_data-last_transfered)/(1024)
            last_transfered = total_transferred_data
            print(time.ctime()," ",thrput)
            time.sleep(1)

class TransferThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        global HOST, PORT, BUFFER_SIZE, total_transferred_data
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        for file_ in directory:
            try:
                filename = os.path.join(src_path, file_)
                filesize = os.path.getsize(filename)
                with open(filename,'rb') as f:
                    s.sendall(file_.encode() + b'\n')
                    s.sendall(str(filesize).encode() + b'\n')
                    while True:
                        data = f.read(BUFFER_SIZE)
                        if not data: break
                        s.sendall(data)
                        total_transferred_data+=BUFFER_SIZE
            except:
                pass

        s.close()




HOST = sys.argv[1] 
PORT = int(sys.argv[2])
src_path= sys.argv[3] 
BUFFER_SIZE = 4096
time_length = 3600 #one hour data
directory = os.listdir(src_path)
monitorThread = MonitorThread()
monitorThread.start()

start_time = time.time()

transferThread = TransferThread()
transferThread.start()
transferThread.join()
transfer_done = True
print(int(time.time()-start_time))

