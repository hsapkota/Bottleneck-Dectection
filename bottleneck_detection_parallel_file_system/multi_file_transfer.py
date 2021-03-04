import threading
import time
from subprocess import PIPE, Popen
import subprocess
import sys, traceback
import os
from subprocess import check_output
import time
import glob,random
import datetime
import os
import subprocess
import shlex
import gc
import collections
import math
import gc

src_ip = "172.31.28.232"
dst_ip = "172.31.16.143"
port_number = "50505"
time_length = 3600  #one hour data
drive_name = "sdq"
log_folder = "./logs/"

label_value = int(sys.argv[1])
# src_path="/data/masud/STransfer1/to/"
# dst_path = "/data/masud/STransfer/received_files/"
src_path="/home/ubuntu/fsx/send/"
dst_path = "/home/ubuntu/fsx/rcv/"
start_time_global = time.time()
should_run = True

# pid = 0
is_transfer_done = False
mdt_parent_path = '/proc/fs/lustre/mdc/'

class fileTransferThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        print("\nStarting " + self.name)
        transfer_file(self.name)
        print("\nExiting " + self.name)

def transfer_file(i):
    # global pid
    # output_file = open("file_transfer_stat.txt","a+")
    strings = ""
    for i in range(2):
        comm_ss = "java SimpleSender1 "+str(dst_ip)+" "+str(port_number)+" "+str(src_path)+str(i)+"/"+" "+str(1000)
        proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE,shell=True)
        # time.sleep(2)
        # pid = check_output(['pidof', '-s', '-o', '29292', 'java', 'SimpleSender1'])
        # print(pid)
        time.sleep(1)
    
    while(True):
        line = str(proc.stdout.readline()).replace("\r", "\n")
        strings+= line
        if not line.decode("utf-8"):
            break
        strings.replace("\r", "\n")

def collect_file_path_info(pid):
    proc = Popen(['ls', '-l', '/proc/'+str(pid).strip()+'/fd/'], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    # print(res)
    res_parts = res.split("\n")
    for line in res_parts:
        if len(line.strip())>0:
            if src_path in line:
                slash_index = line.rfind(">")
                file_name = line[slash_index+1:].strip()
                proc = Popen(['lfs', 'getstripe', file_name], universal_newlines=True, stdout=PIPE)
                res1 = proc.communicate()[0]
                res_parts1 = res1.split("\n")
                for x in range (len(res_parts1)):
                    if "obdidx" in res_parts1[x] or "l_ost_idx" in res_parts1[x]:
                        ost_number = 0
                        if "obdidx" in res_parts1[x]:
                            parts = res_parts1[x+1].strip().split("\t")
                            # print(parts)
                            # print(parts[0])
                            ost_number=int(parts[0].strip())
                        else:
                            parts = res_parts1[x+1].strip().split("l_ost_idx: ")[1].split(",")
                            ost_number=int(parts[0].strip())
                        proc = Popen(['ls', '-l', '/proc/fs/lustre/osc'], universal_newlines=True, stdout=PIPE)
                        res = proc.communicate()[0]
                        parts = res.split("\n")
                        for x in range(1, len(parts)):
                            ost_name_parts = parts[x].split(" ")
                            for part in ost_name_parts:
                                if "OST" in part:
                                    first_dash_index = part.find("-")
                                    sencond_dash_index = part.find("-", first_dash_index)

                                    firstpart = part[:first_dash_index]
                                    secondpart = part[first_dash_index+sencond_dash_index:]

                                    ost_str = "-OST"+'{0:04d}'.format(ost_number)

                                    ost_path = '/proc/fs/lustre/osc/' + firstpart+ost_str+secondpart

                                    # print(ost_path)
                                    return ost_path

                            break

def process_ost_stat(ost_path):
    value_list=[]
    proc = Popen(['cat', ost_path+"/stats"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for metric_line in res_parts:
        if len(metric_line.strip())>0 and "snapshot_time" not in metric_line:
            tokens = str(metric_line).split(" ")
            value_list.append(tokens[0])
            value = float(tokens[len(tokens)-2])
            value_list.append(value)

    proc = Popen(['cat', ost_path+"/rpc_stats"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for metric_line in res_parts:
        if "pending read pages" in metric_line:
            index = metric_line.find(":")
            value = float(metric_line[index+1:])
            value_list.append(value)

        if "read RPCs in flight" in metric_line:
            index = metric_line.find(":")
            value = float(metric_line[index+1:])
            value_list.append(value)
    return value_list 

def process_mds_rpc(mdt_path):
    proc = Popen(['cat', mdt_path+"/import"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    value_list=[]
    for metric_line in res_parts:
        if "avg_waittime:" in metric_line:
            s_index = metric_line.find(":")
            e_index = metric_line.find("usec")
            avg_waittime = float(metric_line[s_index+1:e_index].strip())
            value_list.append(avg_waittime)
            
        if "inflight:" in metric_line:
            s_index = metric_line.find(":")
            inflight = float(metric_line[s_index+1:].strip())
            value_list.append(inflight)
      
        if "unregistering:" in metric_line:
            s_index = metric_line.find(":")
            unregistering = float(metric_line[s_index+1:].strip())
            value_list.append(unregistering)

        if "timeouts:" in metric_line:
            s_index = metric_line.find(":")
            timeouts = float(metric_line[s_index+1:].strip())
            value_list.append(timeouts)

    return value_list

def process_mdt_stat(mdt_path):
    value_list=[]
    proc = Popen(['cat', mdt_path+"/stats"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for metric_line in res_parts:
        if len(metric_line.strip())>0 and "snapshot_time" not in metric_line:
            tokens = str(metric_line).split(" ")
            value_list.append(tokens[0])
            value = float(tokens[len(tokens)-2])
            value_list.append(value)

    proc = Popen(['cat', mdt_path+"/md_stats"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for metric_line in res_parts:
        if len(metric_line.strip())>0 and "snapshot_time" not in metric_line:
            tokens = str(metric_line).split(" ")
            value_list.append(tokens[0])
            value = float(tokens[len(tokens)-3])
            value_list.append(value)
    return value_list                       

def get_mdt_stat(mdt_paths):
    global mdt_parent_path
    value_list=[]
    for path in mdt_paths:
        value_list+= process_mds_rpc(mdt_parent_path+path)
        value_list+=process_mdt_stat(mdt_parent_path+path)
    return value_list


def collect_system_metrics(pid):
    proc = Popen(['cat', '/proc/'+str(pid).strip()+'/io'], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    value_list = []
    for line in res_parts:
        if len(line.strip())>0:
#            print(line)
            index= line.rfind(":")
            value = int(line[index+1:].strip())
#            print(value)
            value_list.append(value)
    
    proc = Popen(['cat', '/proc/'+str(pid).strip()+'/stat'], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split(" ")
    for line in res_parts:
        if len(line.strip())>0:
            # print(line)
            try:
                value = int(line.strip())
                value_list.append(value)
            except:
                pass
                # traceback.print_exc()
#    print(value_list)
    proc = Popen(['ps','-p', str(pid).strip(), '-o',  '%cpu,%mem'], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for line in res_parts:
        if len(line.strip())>0:
            if "%CPU" not in line:
                parts = line.split(" ")
#                print(parts)
                for x in parts:
                    if len(x.strip())>0:
                        value_list.append(float(x))
                        
    return value_list

def get_buffer_value():
    value_list=[]
    proc = Popen(['cat','/proc/sys/net/ipv4/tcp_rmem'], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\t")
    for line in res_parts:
        if len(line.strip())>0:
            value = int(line.strip())
            value_list.append(value)
#    print(value_list)
    
    proc = Popen(['cat','/proc/sys/net/ipv4/tcp_wmem'], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\t")
    for line in res_parts:
        if len(line.strip())>0:
            value = int(line.strip())
            value_list.append(value)
   # print(value_list)
    return value_list


def get_disk_stat():
    global drive_name
    proc = Popen(['iostat','-x',drive_name], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    parts = res.split("\n")

    for part in parts:
        # print(part)
        if len(part.strip())>0 and drive_name in part:
            lst = part.split(" ")
            lst_without_space=[]
            for element in lst:
                if len(element)>0:
                    lst_without_space.append(element)
            # print(lst_without_space)
            
            read_req = lst_without_space[1]
            write_req = lst_without_space[2]
            rkB = lst_without_space[3]
            wkB = lst_without_space[4]
            rrqm = lst_without_space[5]
            wrqm = lst_without_space[6]
            rrqm_perc = lst_without_space[7]
            wrqm_perc = lst_without_space[8]
            r_await = lst_without_space[9]
            w_await = lst_without_space[10]
            areq_sz = lst_without_space[11]
            rareq_sz = lst_without_space[12]
            wareq_sz = lst_without_space[13]
            svctm = lst_without_space[14]
            util = lst_without_space[15]

    # print(read_req," ",write_req," ",rkB," ",wkB," ",rrqm," ",wrqm," ",rrqm_perc," ",wrqm_perc," ",r_await," ",w_await," ",areq_sz," ",rareq_sz," ",wareq_sz," ",svctm," ",util)
    return read_req,write_req,rkB,wkB,rrqm,wrqm,rrqm_perc,wrqm_perc,r_await,w_await,areq_sz,rareq_sz,wareq_sz,svctm,util




def collect_stat():
    isparallel_file_system=False
    proc = Popen(['ls', '-l', '/proc/fs/'], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    parts = res.split("\n")

    for x in parts:
        if "lustre" in x:
            isparallel_file_system=True

    if isparallel_file_system:

        mdt_paths =[]
        proc = Popen(['ls', '-l',mdt_parent_path], universal_newlines=True, stdout=PIPE)
        res = proc.communicate()[0]
        res_parts = res.split("\n")
        for line in res_parts:
            if len(line.strip())>0:
                if "total" not in line:
                    parts = line.split(" ")
                    # print(parts)
                    mdt_paths.append(parts[-1])

        # print(mdt_paths)

        is_controller_port = True
        total_string = ""
        start = time.time()
        initial_time = time.time()
        total_rtt_value = 0
        total_pacing_rate = 0
        is_first_time = True
        avg_wait_time = 0
        total_wait_time = 0
        total_cwnd_value = 0
        total_rto_value = 0
        byte_ack = 0
        byte_ack_so_far = 0
        data_segs_out = 0
        segs_out = 0
        data_seg_out_so_far = 0
        seg_out_so_far = 0
        segs_in = 0
        seg_in_so_far = 0
        retrans = 0
        total_ssthresh_value =0
        total_ost_read = 0
        send = 0
        unacked = 0
        rcv_space = 0
        time_diff = 0
        epoc_time = 0
        has_transfer_started = False
        sleep_time = 1
        epoc_count = 0
        main_output_string = ""
        total_mss_value = 0
        send_buffer_value = 0

        while(1):
                    ### NETWORK METRICS ###
            
            global is_transfer_done
            # print(is_transfer_done)
            if is_transfer_done:
                break
            try:
                #comm_ss = ['ss', '-t', '-i', 'state', 'ESTABLISHED', 'dst', dst_ip]
                time_now = time.ctime()
                comm_ss = 'ss -tanp -i state ESTABLISHED dst '+dst_ip
                ss_proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE,shell=True)
                line_in_ss = str(ss_proc.stdout.read())
                if line_in_ss.count(dst_ip)>=1:
                    parts = line_in_ss.split("\n")
                    # print("parts")

                    # for part in parts:
                    #     print("part")
                    #     print(part)

                    time_diff+=1
                    epoc_time+=1
        
                    for x in range(len(parts)):
                        if dst_ip in parts[x] and port_number in parts[x]:
                            first_parts = parts[x].split(" ")
                            first_list = []
                            for item in first_parts:
                                if len(item.strip())>0:
                                    first_list.append(item)
                            send_buffer_value = int(first_list[-4].strip())

                            sender_part = first_list[-1].strip()
                            user_parts = sender_part.split(",")
                            process_id_part = user_parts[1].strip()
                            equal_index = process_id_part.find("=")
                            process_id = int(process_id_part[equal_index+1:])
                            # print("process id ", process_id)

                            metrics_line = parts[x+1].strip("\\t").strip()
                            metrics_parts = metrics_line.split(" ")
                            for y in range(len(metrics_parts)):
                                if "data_segs_out" in metrics_parts[y]:
                                    pass

                                elif "rto" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    total_rto_value=value
                                
                                elif "rtt" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    e_index = metrics_parts[y].find("/")
                                    value = float(metrics_parts[y][s_index+1:e_index])
                                    total_rtt_value=value
                                
                                elif "mss" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    total_mss_value=value
                                    
                                elif "cwnd" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    total_cwnd_value=value
                                
                                elif "ssthresh" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    total_ssthresh_value=value
                                
                                elif "bytes_acked" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])                     
                                    # byte_ack=(value-byte_ack_so_far)
                                    # byte_ack_so_far = value
                                    byte_ack = value
                                    
                                elif "segs_out" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    # segs_out=(value-seg_out_so_far)
                                    # seg_out_so_far = value
                                    segs_out = value
                                
                                elif "segs_in" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    # segs_in=(value-seg_in_so_far)
                                    # seg_in_so_far = value
                                    segs_in = value
                                    
                                elif "send" in metrics_parts[y]:
                                    value = metrics_parts[y+1].strip()
                                    if "Mbps" in value:
                                        index = value.find("Mbps")
                                        send = float(value[:index])
                                        
                                    elif "Kbps" in value:
                                        index = value.find("Kbps")
                                        send = float(value[:index])*.001
                                    else:
                                        send=value
                                    
                                elif "pacing_rate" in metrics_parts[y]:
                                    value = metrics_parts[y+1].strip()
                                    if "Mbps" in value:
                                        index = value.find("Mbps")
                                        total_pacing_rate = float(value[:index])
                                        
                                    elif "Kbps" in value:
                                        index = value.find("Kbps")
                                        total_pacing_rate = float(value[:index])*.001
                                    else:
                                        total_pacing_rate=value
                                
                                elif "unacked" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    unacked = value
                                
                                elif "retrans" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    e_index = metrics_parts[y].find("/")
                                    value = float(metrics_parts[y][s_index+1:e_index])
                                    retrans = value
                                
                                elif "rcv_space" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    rcv_space = value

                            new_lst = []

                            new_lst.append(total_rtt_value)
                            new_lst.append(total_pacing_rate)
                            new_lst.append(total_cwnd_value)
                            new_lst.append(total_rto_value)
                            new_lst.append(byte_ack/(1024*1024))
                            new_lst.append(segs_out)
                            new_lst.append(retrans)
                            new_lst.append(total_mss_value)
                            new_lst.append(total_ssthresh_value)
                            new_lst.append(segs_in)
                            new_lst.append(send)
                            new_lst.append(unacked)
                            new_lst.append(rcv_space)
                            new_lst.append(send_buffer_value)

                            system_value_list = collect_system_metrics(process_id)
                            buffer_value_list = get_buffer_value()

                            ost_path = collect_file_path_info(process_id)
                            # print(ost_path)

                            ost_value_list = process_ost_stat(ost_path)
                            mdt_value_list = get_mdt_stat(mdt_paths)

                            global label_value
                            new_lst+=system_value_list
                            new_lst+=buffer_value_list
                            new_lst+=ost_value_list
                            new_lst+=mdt_value_list
                            output_string=""
                            for item in new_lst:
                                output_string+=str(item)+","
                            output_string+=str(label_value)+","+str(time_now)+"\n"

                            # print("length ", len(output_string.split(",")))
                            write_thread =fileWriteThread(output_string,process_id)
                            write_thread.start()     
                                              
            except:
                traceback.print_exc()
            time.sleep(sleep_time)



class fileWriteThread(threading.Thread):
    def __init__(self, metric_string, process_id):
        threading.Thread.__init__(self)
        self.metric_string = metric_string
        self.process_id = process_id

    def run(self):
    
        output_file = open(log_folder + "/dataset_"+str(self.process_id)+".csv","a+")
        output_file.write(str(self.metric_string))
        output_file.flush()
        output_file.close()


class statThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        collect_stat()

stat_thread = statThread()
stat_thread.start()


file_transfer_thread = fileTransferThread(str(0))
file_transfer_thread.start()
file_transfer_thread.join()

is_transfer_done = True
 
# collect_stat()

