import subprocess
import time,sys
import shlex

from subprocess import PIPE,Popen
for i in range(100):
    start_time = time.time()
    print("\nfile creation start for "+str(i)+" = "+str(time.ctime()))
    tmp_file_name = 'tmp_file_'+str(i+1)
    file_for_dd_command = 'of='+tmp_file_name

    command = "dd if=/dev/zero of="+tmp_file_name+" status=progress count=1M bs=1024"

    a = subprocess.Popen(shlex.split(command))  # notice stderr
    a.communicate()
    print("\n--- %s seconds ---" % (time.time() - start_time))
    print("file creation end for "+str(i))
