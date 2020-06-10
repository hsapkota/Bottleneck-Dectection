#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 00:32:55 2019

@author: masudulhasanmasudb
"""

import threading
import time
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
        run_command(self.threadID, self.counter)
        print("\nExiting " + self.name)


def run_command(index, delay):
    comm_ss = ['python','globus_test.py','large_file_5']
    proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE)
    proc.communicate()


counter = 5
i = 1
first_start_time = time.time()
while(True):
    jobs = []
    thread1 = myThread(i, 1, 10)
    thread1.start()
    jobs.append(thread1)
    for t in jobs:
        t.join()
        
