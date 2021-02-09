import socket
import time
import os
from threading import Thread
import sys, traceback
import glob

BUFFER_SIZE = 1024
src_path="/fsx/files/"

class ReadThread(Thread):

    def __init__(self, filename):
        Thread.__init__(self)
        self.filename = filename
    def run(self):

        parent_folder_name = src_path+self.filename+"/"
        folder_list=glob.glob(parent_folder_name+"*")
        while True:
            for file_ in folder_list:
                with open(file_, 'rb') as f:
                    while True:
                        bytes_read = f.read(BUFFER_SIZE)
                        #print(bytes_read)
                        if not bytes_read:
                            break
                print("done",self.filename)


thread_number = int(sys.argv[1])
start_time = time.time()
threads = []
for x in range(thread_number):
    newthread = ReadThread(str(x%5))
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()

print("\n--- %s seconds ---" % (time.time() - start_time))

