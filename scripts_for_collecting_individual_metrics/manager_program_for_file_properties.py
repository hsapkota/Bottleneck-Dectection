import threading
import time
from subprocess import PIPE, Popen

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
        # print_time(self.name, 5, self.counter)
        # check_thread_function(self.name, 5, self.counter)
        # file_name = "file_stat_for_" + str(i) + "_process_" + str(j)
        run_command(self.name, self.counter)
        print("\nExiting " + self.name)


def run_command(file_name, delay):
    proc = Popen(['python', file_name])
    proc.communicate()


counter = 5
i = 1
first_start_time = time.time()
file_names = ['ost_metrics.py', 'mdt_metrics.py', 'llite_metrics.py', 'lmv_metrics.py', 'lov_metrics.py' ]

jobs = []

for x in file_names:
    thread1 = myThread(i, x, 10)
    thread1.start()
    jobs.append(thread1)
for t in jobs:
    t.join()
