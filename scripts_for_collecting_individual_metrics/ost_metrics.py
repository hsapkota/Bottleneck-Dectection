import os
import subprocess, time
from subprocess import PIPE, Popen
import threading

shouldThreadRun = True

class fileThread(threading.Thread):
    def __init__(self, threadID, path, metric):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.path = path
        self.metric = metric

    def run(self):
        out_file = open("osc_" + self.metric + ".txt", "a+")
        while True:
            proc = Popen(['cat', self.path], universal_newlines=True, stdout=PIPE)
            res = proc.communicate()[0]
            out_file.write(time.ctime() + "\n")
            out_file.write(res)
            out_file.write("\n\n\n")
            out_file.flush()
            if not shouldThreadRun:
                break
            time.sleep(1)
            # out_file.close()
        # print(res)




proc = Popen(['ls', '-l', '/proc/fs/lustre'], universal_newlines=True, stdout=PIPE)
res = proc.communicate()[0]
parts = res.split("\n")
# print(parts)
stat_file_names = []
for x in range(1, len(parts)):
    file_parts = parts[x].split(" ")
    stat_file_names.append(file_parts[len(file_parts) - 1])
    # print(file_parts[len(file_parts) - 1])
OST_name = ""
ost_path = ""
ost_metrics = []
mdt_metrics = []
llite_metrics = []
lmv_metrics = []
lov_metrics = []

mdt_path = []
llite_path = []
lmv_path = []
lov_path = []
for name in stat_file_names:
    if "osc" in name:
        proc = Popen(['ls', '-l', '/proc/fs/lustre/osc'], universal_newlines=True, stdout=PIPE)
        res = proc.communicate()[0]
        parts = res.split("\n")
        for x in range(1, len(parts)):
            ost_name_parts = parts[x].split(" ")
            if "panda-OST0009" in ost_name_parts[len(ost_name_parts) - 1]:
                OST_name = ost_name_parts[len(ost_name_parts) - 1]
                break
        ost_path = '/proc/fs/lustre/osc/' + OST_name
        proc = Popen(['ls', '-l', ost_path], universal_newlines=True, stdout=PIPE)
        res = proc.communicate()[0]
        parts = res.split("\n")
        for x in range(1, len(parts)):
            ost_metrics_name_parts = parts[x].split(" ")
            ost_metrics.append(ost_metrics_name_parts[len(ost_metrics_name_parts) - 1])
            # print(ost_metrics_name_parts[len(ost_metrics_name_parts) - 1])

# out_file = open("osc_metrics.txt", "a+")
count = 1


# out_file.write(time.ctime() + "\n")
i=0
for metric in ost_metrics:
    if "ping" not in metric:
        if len(str(metric).strip())>1:
            metric_path = ost_path+"/"+metric

            thread = fileThread(i, metric_path, metric)
            thread.start()

            i+=1

while True:
    choice = input("Please enter b ")
    if choice == 'b' :
        print("B pressed")
        shouldThreadRun = False
        break



