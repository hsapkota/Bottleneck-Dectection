#!/bin/bash

wait_period=0

while true
do
    echo "wait period ${wait_period}"
    if [ $wait_period -gt 3600 ];then
       break
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 test_commands.py 0 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 10;

    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem loss 0.5%;
        sleep 5;
        python2 test_commands.py 1 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi
    
    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem loss 0.1%;
        sleep 5;
        python2 test_commands.py 2 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem loss 0.05%;
        sleep 5;
        python2 test_commands.py 3 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem loss 1%;
        sleep 5;
        python2 test_commands.py 4 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        sudo tc qdisc add dev eno1 root netem delay 0.01ms 0.01ms distribution normal;
        sleep 5;
        python2 test_commands.py 5 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        sudo tc qdisc add dev eno1 root netem delay 0.02ms 0.01ms distribution normal;
        sleep 5;
        python2 test_commands.py 6 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        sudo tc qdisc add dev eno1 root netem delay 0.03ms 0.01ms distribution normal;
        sleep 5;
        python2 test_commands.py 7 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        sudo tc qdisc add dev eno1 root netem delay 0.04ms 0.01ms distribution normal;
        sleep 5;
        python2 test_commands.py 8 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem duplicate 0.5%;
        sleep 5;
        python2 test_commands.py 9 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem duplicate 0.1%;
        sleep 5;
        python2 test_commands.py 10 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem duplicate 0.05%;
        sleep 5;
        python2 test_commands.py 11 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem duplicate 1%;
        sleep 5;
        python2 test_commands.py 12 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem corrupt 0.5%;
        sleep 5;
        python2 test_commands.py 13 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem corrupt 0.1%;
        sleep 5;
        python2 test_commands.py 14 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem corrupt 0.05%;
        sleep 5;
        python2 test_commands.py 15 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem corrupt 1%;
        sleep 5;
        python2 test_commands.py 16 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem reorder 0.5% delay 1ms;
        sleep 5;
        python2 test_commands.py 17 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem reorder 0.1% delay 1ms;
        sleep 5;
        python2 test_commands.py 18 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem reorder 0.05% delay 1ms;
        sleep 5;
        python2 test_commands.py 19 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root netem reorder 1% delay 1ms;
        sleep 5;
        python2 test_commands.py 20 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root tbf rate 9.5GBit burst 32Mbit limit 30000;
        sleep 5;
        python2 test_commands.py 21 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root tbf rate 9.1GBit burst 32Mbit limit 30000;
        sleep 5;
        python2 test_commands.py 22 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root tbf rate 9.2GBit burst 32Mbit limit 30000;
        sleep 5;
        python2 test_commands.py 23 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eno1 root tbf rate 9.3GBit burst 32Mbit limit 30000;
        sleep 5;
        python2 test_commands.py 24 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eno1 root;
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        stress -d 1 &
        sleep 5;
        python2 test_commands.py 25 &
        sleep 60;
        killall stress;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        stress -i 10 &
        sleep 5;
        python2 test_commands.py 26 &
        sleep 60;
        killall stress;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        stress -c 1 &
        sleep 5;
        python2 test_commands.py 27 &
        sleep 60;
        killall stress;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 10;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        stress-ng --vm-bytes $(awk '/MemAvailable/{printf "%d\n", $2 * 0.98;}' < /proc/meminfo)k --vm-keep -m 10  &
        sleep 5;
        python2 test_commands.py 28 &
        sleep 60;
        killall stress-ng;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 10;
    fi


done
