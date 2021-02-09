#!/bin/bash
myarray=(0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
       17 18 19 20 21 22 23 24 25 26 27 28 29)

wait_period=0

while true
do
    echo "wait period ${wait_period}"
    if [ $wait_period -gt 36000 ];then
       break
    fi

    myarray=( $(shuf -e "${myarray[@]}") )
    # printf "%s" "${myarray[@]}"
    for t in ${myarray[@]}; do
    
        if [ $t -eq 0 ]
        then
            python2 test_comments.py 0 &
            sleep 60;
            pkill -9 python2;
            pkill -9 java;
            wait_period=$(($wait_period+60));
            sleep 5;
        fi

        if [ $t -eq 1 ]
        then
            tc qdisc add dev eth0 root netem loss 0.5%;
            sleep 5;
            python2 test_commands.py 1 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi
        
       
        if [ $t -eq 2 ]
        then
            tc qdisc add dev eth0 root netem loss 0.1%;
            sleep 5;
            python2 test_commands.py 2 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 3 ]
        then
            tc qdisc add dev eth0 root netem loss 0.05%;
            sleep 5;
            python2 test_commands.py 3 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 4 ]
        then
            tc qdisc add dev eth0 root netem loss 1%;
            sleep 5;
            python2 test_commands.py 4 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 5 ]
        then
            sudo tc qdisc add dev eth0 root netem delay 0.01ms 0.01ms distribution normal;
            sleep 5;
            python2 test_commands.py 5 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 6 ]
        then
            sudo tc qdisc add dev eth0 root netem delay 0.02ms 0.01ms distribution normal;
            sleep 5;
            python2 test_commands.py 6 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 7 ]
        then
            sudo tc qdisc add dev eth0 root netem delay 0.03ms 0.01ms distribution normal;
            sleep 5;
            python2 test_commands.py 7 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 8 ]
        then
            sudo tc qdisc add dev eth0 root netem delay 0.04ms 0.01ms distribution normal;
            sleep 5;
            python2 test_commands.py 8 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 9 ]
        then
            tc qdisc add dev eth0 root netem duplicate 0.5%;
            sleep 5;
            python2 test_commands.py 9 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 10 ]
        then
            tc qdisc add dev eth0 root netem duplicate 0.1%;
            sleep 5;
            python2 test_commands.py 10 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 11 ]
        then
            tc qdisc add dev eth0 root netem duplicate 0.05%;
            sleep 5;
            python2 test_commands.py 11 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 12 ]
        then
            tc qdisc add dev eth0 root netem duplicate 1%;
            sleep 5;
            python2 test_commands.py 12 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 13 ]
        then
            tc qdisc add dev eth0 root netem corrupt 0.5%;
            sleep 5;
            python2 test_commands.py 13 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 14 ]
        then
            tc qdisc add dev eth0 root netem corrupt 0.1%;
            sleep 5;
            python2 test_commands.py 14 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 15 ]
        then
            tc qdisc add dev eth0 root netem corrupt 0.05%;
            sleep 5;
            python2 test_commands.py 15 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 16 ]
        then
            tc qdisc add dev eth0 root netem corrupt 1%;
            sleep 5;
            python2 test_commands.py 16 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 17 ]
        then
            tc qdisc add dev eth0 root netem reorder 0.5% delay 1ms;
            sleep 5;
            python2 test_commands.py 17 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 18 ]
        then
            tc qdisc add dev eth0 root netem reorder 0.1% delay 1ms;
            sleep 5;
            python2 test_commands.py 18 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 19 ]
        then
            tc qdisc add dev eth0 root netem reorder 0.05% delay 1ms;
            sleep 5;
            python2 test_commands.py 19 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 20 ]
        then
            tc qdisc add dev eth0 root netem reorder 1% delay 1ms;
            sleep 5;
            python2 test_commands.py 20 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 21 ]
        then
            tc qdisc add dev eth0 root tbf rate 9.5GBit burst 32Mbit limit 30000;
            sleep 5;
            python2 test_commands.py 21 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 22 ]
        then
            tc qdisc add dev eth0 root tbf rate 9.1GBit burst 32Mbit limit 30000;
            sleep 5;
            python2 test_commands.py 22 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 23 ]
        then
            tc qdisc add dev eth0 root tbf rate 9.2GBit burst 32Mbit limit 30000;
            sleep 5;
            python2 test_commands.py 23 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 24 ]
        then
            tc qdisc add dev eth0 root tbf rate 9.3GBit burst 32Mbit limit 30000;
            sleep 5;
            python2 test_commands.py 24 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            tc qdisc del dev eth0 root;
            sleep 5;
        fi

       
        if [ $t -eq 25 ]
        then
            stress -d 1 &
            sleep 5;
            python2 test_commands.py 25 &
            sleep 60;
            killall stress;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            sleep 5;
        fi

       
        if [ $t -eq 26 ]
        then
            stress -i 10 &
            sleep 5;
            python2 test_commands.py 26 &
            sleep 60;
            killall stress;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            sleep 5;
        fi

       
        if [ $t -eq 27 ]
        then
            stress -c 1 &
            sleep 5;
            python2 test_commands.py 27 &
            sleep 60;
            killall stress;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            sleep 5;
        fi

       
        if [ $t -eq 28 ]
        then
            stress-ng --vm-bytes $(awk '/MemAvailable/{printf "%d\n", $2 * 0.98;}' < /proc/meminfo)k --vm-keep -m 10  &
            sleep 5;
            python2 test_commands.py 28 &
            sleep 60;
            killall stress-ng;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            sleep 5;
        fi

       
        if [ $t -eq 29 ]
        then
            python2 test_commands.py 29 &
            sleep 60;
            killall -9 python2;
            killall -9 java;
            wait_period=$(($wait_period+60));
            sleep 5;
        fi
    done    
done
