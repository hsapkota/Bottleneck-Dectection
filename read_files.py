#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:28:03 2019

@author: masudulhasanmasudb
"""

import threading
import time
from subprocess import PIPE, Popen
import subprocess

exitFlag = 0


# out_file = open("time_stat_for_2_process", "a+")
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("\nStarting " + self.name)
        run_command(self.name)
        print("\nExiting " + self.name)


def run_command(index):
    s = ""
#    for piece in read_file('temp_files/tmp_file_'+index+'.txt'):
##        process_piece(piece)
#        print("\n\n")
#    while True:
    present_time = time.time()
    read_so_far = 0
    with open('temp_files/tmp_file_'+index+'.txt', 'rb') as f: 
        while True: 
            piece = f.read(1024) 
#            print(str(index) +" "+str(read_so_far))
            read_so_far+=1024
            now_time = time.time()
            if(int(now_time - present_time)>=10):
                print(str(index) +" "+ str(read_so_far/(1024*1024)))
#                print(piece)
                present_time = now_time
#                    read_so_far = 0
            if not piece: 
                break    
        



#    with open('tmp_file_'+index+'.txt') as FileObj:
#        for lines in FileObj:
#            s+=str(lines)
#            print(s)
#    print(s)


#def read_file(path, block_size=1024): 
#    with open(path, 'rb') as f: 
#        while True: 
#            piece = f.read(block_size) 
#            print(piece)
#            if piece: 
#                yield piece 
#            else: 
#                return
                    
                
class networkThread(threading.Thread):
    def __init__(self,stream_number):
        threading.Thread.__init__(self)
        self.stream_number = stream_number
        
    def run(self):
        run_network_command(self.stream_number)
                      

def run_network_command(stream_number):
    comm_ss = ['globus-url-copy','-vb', '-p', str(stream_number),'file:///dev/zero', 'gsiftp://br033.dmz.bridges.psc.edu:2811/dev/null']
    proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE)
    print(proc.communicate())       


counter = 5
i = 1
first_start_time = time.time()

for y in range(1,33):
#    thread2 = networkThread(33-y)
#    thread2.start()
    jobs = []
    for x in range(33-y):
        thread1 = myThread(i, str(x), 10)
        thread1.start()
        jobs.append(thread1)
    for t in jobs:
        t.join()
#    thread2._Thread__stop()
#    comm_ss = ['killall','globus-url-copy',]
#    proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE)
#    proc.communicate()      
        
        
        
        