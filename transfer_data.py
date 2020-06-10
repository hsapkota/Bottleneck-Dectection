#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 01:59:11 2019

@author: masudulhasanmasudb
"""
import time
import glob,random
import datetime
import os
import subprocess
import shlex
import gc
from subprocess import PIPE,Popen
##import iperf3
#
##iperf3 -P 20 -c 134.197.42.229
#for x in range(128):
#    dest_ip = "134.197.42.229"
#    proc = Popen(['bash', 'my_script.sh', '40'], universal_newlines=True, stdout=PIPE)
#    res = proc.communicate()[0]
#    print(res)
    

import threading
import time
from subprocess import PIPE,Popen

exitFlag = 0
class myThread (threading.Thread):
   def __init__(self, stream_number):
      threading.Thread.__init__(self)
      self.stream_number = stream_number
   def run(self):
      #output_file = open("output_"+str(self.stream_number)+".txt","a+")
      print("\nStarting " + str(self.stream_number)+" "+str(time.ctime())+"\n")
      #output_file.write("\nStarting " + str(self.stream_number)+" "+str(time.ctime())+"\n")
      dest_ip = "134.197.42.229"
      proc = Popen(['bash', 'n_script.sh', str(self.stream_number)], universal_newlines=True, stdout=PIPE)
      res = proc.communicate()[0]
      #output_file.write(res)


start_time = time.time()
for j in range(20):
    jobs = []
    thread1 = myThread(j+1)
    thread1.start()
    jobs.append(thread1)
    for t in jobs:
        t.join()

  
    
    
    

#import iperf3
#
#client = iperf3.Client()
#client.duration = 10
#client.server_hostname = '134.197.42.229'
#client.port = 5201
#client.num_streams = 12
#
#print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
#result = client.run()
#
#if result.error:
#    print(result.error)
#else:
##    print(result)
#    print('')
#    print('Test completed:')
#    print('  started at         {0}'.format(result.time))
#    print('  bytes transmitted  {0}'.format(result.sent_bytes))
#    print('  retransmits        {0}'.format(result.retransmits))
#    print('  avg cpu load       {0}%\n'.format(result.local_cpu_total))
#
#    print('Average transmitted data in all sorts of networky formats:')
#    print('  bits per second      (bps)   {0}'.format(result.sent_bps))
#    print('  Kilobits per second  (kbps)  {0}'.format(result.sent_kbps))
#    print('  Megabits per second  (Mbps)  {0}'.format(result.sent_Mbps))
#    print('  KiloBytes per second (kB/s)  {0}'.format(result.sent_kB_s))
#print('  MegaBytes per second (MB/s)  {0}'.format(result.sent_MB_s))

#client = iperf3.Client()
#client.duration = 1
##client.bind_address = '10.0.0.1'
##client.server_hostname = '10.10.10.10'
#client.server_hostname = '134.197.42.229'
#client.port = 5202
#client.blksize = 1234
#client.num_streams = 10
#client.zerocopy =True
#client.verbose =False
#client.reverse =True
#client.run()



#client.json_output =False
#result = client.run()
#print(result)
