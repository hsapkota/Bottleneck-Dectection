import subprocess, time
from subprocess import PIPE, Popen
import threading

shouldThreadRun = True

class fileThread(threading.Thread):
    def __init__(self, threadID, path, metric, index_number):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.path = path
        self.metric = metric
        self.index_number = index_number

    def run(self):
        out_file = open("mdt_"+str(index_number)+"_"+self.metric+".txt", "a+")
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

    if "mdc" in name:
        proc = Popen(['ls', '-l', '/proc/fs/lustre/mdc'], universal_newlines=True, stdout=PIPE)
        res = proc.communicate()[0]
        parts = res.split("\n")
        for x in range(1, len(parts)):
            name_parts = parts[x].split(" ")
            if "panda" in name_parts[len(name_parts) - 1]:
                mdt_path.append('/proc/fs/lustre/mdc/' + name_parts[len(name_parts) - 1])

        mdt_metric_path = mdt_path[0]
        proc = Popen(['ls', '-l', mdt_metric_path], universal_newlines=True, stdout=PIPE)
        res = proc.communicate()[0]
        parts = res.split("\n")
        for x in range(1, len(parts)):
            metrics_name_parts = parts[x].split(" ")
            mdt_metrics.append(metrics_name_parts[len(metrics_name_parts) - 1])
            # print(metrics_name_parts[len(metrics_name_parts) - 1])




i=0
index_number =0
for mdt in mdt_path:
    for metric in mdt_metrics:
        if "ping" not in metric:
            if len(metric) >= 1:
                metric_path = mdt+"/"+metric
                thread = fileThread(i, metric_path, metric,index_number)
                thread.start()

                i+=1
    index_number = index_number + 1

while True:
    choice = input("Please enter b ")
    if choice == 'b' :
        print("B pressed")
        shouldThreadRun = False
        break

# while True:
#     index_number =0
#     for mdt in mdt_path:
#         for metric in mdt_metrics:
#             if len(metric)>=1:
#                 metric_path = mdt+"/"+metric
#                 proc = Popen(['cat', metric_path], universal_newlines=True, stdout=PIPE)
#                 res = proc.communicate()[0]
#                 # print(res)
#                 out_file = open("mdt_"+str(index_number)+"_"+metric+".txt", "a+")
#                 out_file.write(time.ctime() + "\n")
#                 out_file.write(res)
#                 out_file.write("\n\n\n")
#                 out_file.close()
#         index_number = index_number+1
#     time.sleep(1)






