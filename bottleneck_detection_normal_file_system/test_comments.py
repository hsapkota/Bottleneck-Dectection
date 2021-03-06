import threading
import time
from subprocess import PIPE, Popen
import subprocess
import sys, traceback
import os
from subprocess import check_output
# print (os.environ['PATH'])

src_ip = ""
dst_ip = "172.31.22.200"
port_number = "50505"
time_length = 3600  #one hour data
drive_name = "sda"


# src_path="/data/masud/STransfer1/to/"
# dst_path = "/data/masud/STransfer/received_files/"
src_path='/data/to/'
dst_path = "/home/cc/received_files/"
start_time_global = time.time()
##normal = 0
## HIGH memory = 1
## high cpu = 2

label_value = int(sys.argv[1])
should_run = True
pid = 0
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
    global pid,label_value
    output_file = open("file_transfer_stat.txt","a+")
    #if label_value==29:
    #    comm_ss = ['java', 'SimpleSender2', dst_ip, port_number, src_path, str(label_value)]
    #else:
    #comm_ss = ['java', 'SimpleSender1', dst_ip, port_number, src_path, str(label_value)]
    strings = ""
    comm_ss = "java SimpleSender1 "+str(dst_ip)+" "+str(port_number)+" "+str(src_path)+" "+str(label_value)
    proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE,shell=True)
    pid = check_output(['pidof', '-s', 'java', 'SimpleSender1'])
    print(pid)
    #global label_value
    output_file.write("label = "+str(label_value) + "\n")
    output_file.write("start time = "+time.ctime() + "\n")
    output_file.flush()
    output_file.close
    while(True):
        line = str(proc.stdout.readline()).replace("\r", "\n")
        strings+= line
        if not line.decode("utf-8"):
            break
        strings.replace("\r", "\n")

def collect_system_metrics(pid_str):
    # print("pid ",pid.strip("'b"))
    global pid
    # print("pid ",pid)
    value_list = []
    # try:
    #     proc = Popen(['cat', '/proc/'+str(pid).strip()+'/io'], universal_newlines=True, stdout=PIPE)
    #     res = proc.communicate()[0]
    #     res_parts = res.split("\n")
    #     for line in res_parts:
    #         if len(line.strip())>0:
    # #            print(line)
    #             index= line.rfind(":")
    #             value = int(line[index+1:].strip())
    # #            print(value)
    #             value_list.append(value)
    # except:
    #     print("io stat not possible")
    
    try:
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
    except:
        print("stat not possible")

    try:
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
    except:
        print("cpu mem not possible")
                        
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
    # print(value_list)
    
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
#            print(avg_waittime)
            
        if "inflight:" in metric_line:
            s_index = metric_line.find(":")
            inflight = float(metric_line[s_index+1:].strip())
            value_list.append(inflight)
#            print(inflight)
        
        if "unregistering:" in metric_line:
            s_index = metric_line.find(":")
            unregistering = float(metric_line[s_index+1:].strip())
            value_list.append(unregistering)
#            print(unregistering)
            
        if "timeouts:" in metric_line:
            s_index = metric_line.find(":")
            timeouts = float(metric_line[s_index+1:].strip())
            value_list.append(timeouts)
#            print(timeouts)
    return value_list

def process_mdt_stat(mdt_path):
    value_list=[]
    proc = Popen(['cat', mdt_path+"/stats"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for metric_line in res_parts:
        if len(metric_line.strip())>0 and "snapshot_time" not in metric_line:
            tokens = str(metric_line).split(" ")
            value = float(tokens[len(tokens)-2])
            value_list.append(value)
    # print(value_list)

    proc = Popen(['cat', mdt_path+"/md_stats"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for metric_line in res_parts:
        if len(metric_line.strip())>0 and "snapshot_time" not in metric_line:
            tokens = str(metric_line).split(" ")
            value = float(tokens[len(tokens)-3])
            value_list.append(value)
    # print(value_list)

    return value_list

def process_ost_stat(ost_path):
    value_list=[]
    proc = Popen(['cat', ost_path+"/stats"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for metric_line in res_parts:
        if len(metric_line.strip())>0 and "snapshot_time" not in metric_line:
            tokens = str(metric_line).split(" ")
            value = float(tokens[len(tokens)-2])
            value_list.append(value)
    # print(value_list)

    proc = Popen(['cat', ost_path+"/rpc_stats"], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    res_parts = res.split("\n")
    for metric_line in res_parts:
        if "pending read pages" in metric_line:
            index = metric_line.find(":")
            value = float(metric_line[index+1:])
            # total_pending_page+=value
            value_list.append(value)

        if "read RPCs in flight" in metric_line:
            index = metric_line.find(":")
            value = float(metric_line[index+1:])
            # total_pending_rpc+=value
            value_list.append(value)
    # print(value_list)
    return value_list

    
def get_mdt_stat(mdt_paths):
    global mdt_parent_path
    value_list=[]
    for path in mdt_paths:
        value_list+= process_mds_rpc(mdt_parent_path+path)
        # print(" val 1 ",value_list)
        value_list+=process_mdt_stat(mdt_parent_path+path)
        # print("val 2 ",value_list)
    # print("final",value_list)
    return value_list

def collect_stat():
    isparallel_file_system=False
    proc = Popen(['ls', '-l', '/proc/fs/'], universal_newlines=True, stdout=PIPE)
    res = proc.communicate()[0]
    parts = res.split("\n")

    for x in parts:
        if "lustre" in x:
            isparallel_file_system=True

    if isparallel_file_system:

        proc = Popen(['ls', '-l', '/proc/fs/lustre/osc'], universal_newlines=True, stdout=PIPE)
        res = proc.communicate()[0]
        parts = res.split("\n")
        for x in range(1, len(parts)):
            ost_name_parts = parts[x].split(" ")
            if "owtwrbmv-OST0000" in ost_name_parts[len(ost_name_parts) - 1]:
                OST_name = ost_name_parts[len(ost_name_parts) - 1]
                break
        ost_path = '/proc/fs/lustre/osc/' + OST_name
        # print(ost_path)
        
        mdt_paths =[]
        proc = Popen(['ls', '-l',mdt_parent_path], universal_newlines=True, stdout=PIPE)
        res = proc.communicate()[0]
        res_parts = res.split("\n")
        for line in res_parts:
            if len(line.strip())>0:
                if "panda" in line:
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
        sleep_time = .1
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
                comm_ss = 'ss -t -i state ESTABLISHED dst '+dst_ip
                ss_proc = subprocess.Popen(comm_ss, stdout=subprocess.PIPE,shell=True)
                line_in_ss = str(ss_proc.stdout.read())
                if line_in_ss.count(dst_ip)>=1:
                    if (is_first_time):
                        initial_time = time.time()
                        is_first_time = False
                    
                    #print(line_in_ss)
                    # print(type(line_in_ss))
                    parts = line_in_ss.split("\n")
                    # print("parts")
                    # print(len(parts))

                    # for part in parts:
                    #     print(part)

                    time_diff+=1
                    epoc_time+=1
        
                    for x in range(len(parts)):
                        if dst_ip in parts[x] and port_number in parts[x]:
                            # print("here")
                            first_parts = parts[x].split(" ")
                            first_list = []
                            #print(first_parts)
                            for item in first_parts:
                                if len(item.strip())>0:
                                    first_list.append(item)
                            send_buffer_value = int(first_list[-3].strip())
                            #print("buffer ",send_buffer_value)
                            
                            if (is_first_time):
                                initial_time = time.time()
                                is_first_time = False
                            
                            metrics_line = parts[x+1].strip("\\t").strip()
                            metrics_parts = metrics_line.split(" ")
                            # print("metric parts ", metrics_parts)
                            for y in range(len(metrics_parts)):
                                if "data_segs_out" in metrics_parts[y]:
                                    pass
                                    # s_index = metrics_parts[y].find(":")
                                    # value = float(metrics_parts[y][s_index+1:])
                                    # data_segs_out=(value-data_seg_out_so_far)
                                    # data_seg_out_so_far = value

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
                                    # print("value ",value)
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
                                    byte_ack=(value-byte_ack_so_far)
                                    byte_ack_so_far = value
                                    
                                elif "segs_out" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    # print("value ", value)
                                    # print("seg_out_so_far ", seg_out_so_far)
                                    segs_out=(value-seg_out_so_far)
                                    seg_out_so_far = value
                                
                                elif "segs_in" in metrics_parts[y]:
                                    s_index = metrics_parts[y].find(":")
                                    value = float(metrics_parts[y][s_index+1:])
                                    segs_in=(value-seg_in_so_far)
                                    seg_in_so_far = value
                                    
                                elif "send" in metrics_parts[y]:
                                    value = metrics_parts[y+1].strip()
                                    send=value
                                    
                                elif "pacing_rate" in metrics_parts[y]:
                                    value = metrics_parts[y+1].strip()
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
    
                    if(time_diff>=(.1/sleep_time)):
                        avg_rto_value = total_rto_value/time_diff
                        avg_rtt_value = total_rtt_value/time_diff
                        avg_mss_value = total_mss_value/time_diff
                        avg_cwnd_value = total_cwnd_value/time_diff
                        avg_ssthresh_value = total_ssthresh_value/time_diff
                        avg_byte_ack = byte_ack/(1024*1024)
                        avg_seg_out = segs_out
                        avg_seg_in = segs_in
                        avg_send_value = send
                        p_avg_value = total_pacing_rate
                        avg_unacked_value = unacked
                        avg_retrans = retrans/time_diff
                        avg_rcv_space = rcv_space/time_diff
                        
                        # print("14 ", data_segs_out)


                        #print("Individual values")
                        #print("1 ",avg_rto_value)
                        #print("2, ",avg_rtt_value)
                        #print("3, ",avg_mss_value)
                        #print("4, ",avg_cwnd_value)
                        #print("5, ",avg_ssthresh_value)
                        #print("6, ",avg_byte_ack)
                        #print("7, ",avg_seg_out)
                        #print("8, ",avg_seg_in)
                        #print("9, ",avg_send_value)
                        #print("10, ",p_avg_value)
                        #print("11, ",avg_unacked_value)
                        #print("12, ",avg_retrans)
                        system_value_list=[]

                        global pid
                        if pid !=0:
                            system_value_list = collect_system_metrics(pid)
                        buffer_value_list = get_buffer_value()

                        ost_value_list = process_ost_stat(ost_path)
                        mdt_value_list = get_mdt_stat(mdt_paths)
                        # mdt_rpc_avg_waittime, rpc_inflight, rpc_unregistering, rpc_timeouts = process_mds_rpc(mdt_path)
                        # read_req,write_req,rkB,wkB,rrqm,wrqm,rrqm_perc,wrqm_perc,r_await,w_await,areq_sz,rareq_sz,wareq_sz,svctm,util = get_disk_stat()
                        output_string = str(avg_rtt_value)+","+str(p_avg_value) + ","+str(avg_cwnd_value)+","+str(avg_rto_value)+","+\
                                    str(avg_byte_ack)+","+str(avg_seg_out) +","+str(retrans)+","+\
                                    str(avg_mss_value)+","+str(avg_ssthresh_value) + ","+str(avg_seg_in)+","+\
                                    str(avg_send_value)+","+str(avg_unacked_value) + ","+str(avg_rcv_space)+","+\
                                    str(send_buffer_value)
                                    
                                    # +","+str(read_req)+","+str(write_req)+","+str(rkB)+","+str(wkB)+","+str(rrqm)+","+str(wrqm)+","+\
                                    # str(rrqm_perc)+","+str(wrqm_perc)+","+str(r_await)+","+str(w_await)+","+str(areq_sz)+","+str(rareq_sz)+","+str(wareq_sz)+","+str(svctm)+","+str(util)
                            
                        global label_value
                        for item in system_value_list:
                            output_string+=","+str(item)
                        for item in buffer_value_list:
                            output_string+=","+str(item)
                        for item in ost_value_list:
                            output_string+=","+str(item)
                        for item in mdt_value_list:
                            output_string+=","+str(item)
                        output_string+=","+str(label_value)+"\n"
                        main_output_string+=output_string

                        epoc_count+=1
                        # if(epoc_count==10):
                        if(epoc_count%10==0):
                            if(epoc_count%100==0):
                                print("tarnsfering file.... ",epoc_count)
                                epoc_count = 0
                            write_thread =fileWriteThread(main_output_string, label_value)
                            write_thread.start()
                            main_output_string=""
                
            except:
                traceback.print_exc()
            time.sleep(sleep_time)

class fileWriteThread(threading.Thread):
    def __init__(self, metric_string, label_value):
        threading.Thread.__init__(self)
        self.metric_string = metric_string
        self.label_value = label_value

    def run(self):
        
        output_string = "avg_rtt_value, p_avg_value ,avg_cwnd_value,avg_rto_value,"+\
                        "avg_byte_ack,avg_seg_out , retrans,"+\
                        "avg_mss_value,avg_ssthresh_value ,avg_seg_in,"+\
                        "avg_send_value,avg_unacked_value ,avg_rcv_space,"+\
                        "send_buffer_value,tps,rkB,wkB,areq_sz,aqu_sz,await_time,svctm,util,label_value\n"
        
        output_file = open("dataset_"+str(self.label_value)+".csv","a+")
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
