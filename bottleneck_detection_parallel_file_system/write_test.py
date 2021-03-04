import subprocess
import time,sys
import shlex
from subprocess import PIPE,Popen
from threading import Thread
import sys, traceback

class WriteThread(Thread):

    def __init__(self, filename):
        Thread.__init__(self)
        self.filename = filename
    def run(self):
        while True:
            proc = Popen(['touch','/home/ubuntu/fsx/rcv/'+self.filename])
            proc.communicate()
            proc2 = Popen(['rm','/home/ubuntu/fsx/rcv/'+self.filename])
            proc2.communicate()


thread_number = int(sys.argv[1])
start_time = time.time()
threads = []
for x in range(thread_number):
    newthread = WriteThread(str(50 + (x%thread_number)))
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()

print("\n--- %s seconds ---" % (time.time() - start_time))

