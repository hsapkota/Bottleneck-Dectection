#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 07:00:28 2019

@author: masudulhasanmasudb
"""
import subprocess,time

output_file = open("tcp_metrics.txt","a+")

src_ip = "134.197.40.134"
dst_ip = "192.231.243.54"
comm_ss = ['ss', '-t', '-i', 'state', 'ESTABLISHED', 'dst', dst_ip]
while(1):
    ss_proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE)
    line_in_ss = str(ss_proc.stdout.read())
#    print (line_in_ss)
    #print(time.ctime() + "\n")
    output_file.write(time.ctime() + "\n")
    output_file.write(str(line_in_ss)+"\n\n")
    output_file.flush()
    
#    line_in_ss = re.sub('\A.+\n','',line_in_ss)
#    line_in_ss = re.sub('\n','',line_in_ss)
#    connections = line_in_ss.splitlines()
#    print(connections)
#    for connection in connections:
#        # print connection
#        ips, ports, tcp, rto, rtt, ato, mss, maxcwnd, ssthresh, send, pace, unacked = parseconnection(connection)
#        para_list = [ips, ports, tcp, rto, rtt, ato, mss, maxcwnd, ssthresh, send, pace, unacked]
#        list.append(para_list)
#        print (ips, ports, mss, rtt, wscaleavg, maxcwnd, unacked, retrans, lost, tcp, send)
    time.sleep(1)
