#!/bin/bash

wait_period=0

while true
do
    echo "wait period ${wait_period}"
    if [ $wait_period -gt 36000 ];then
       break
    fi

    
	python2 test_comments.py 0 &
	sleep 60;
	killall -9 python2;
    killall -9 java;
	wait_period=$(($wait_period+60));
	sleep 5;


    
    
    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        stress -c 2 &
        sleep 5;
        python2 test_comments.py 33 &
        sleep 60;
        killall -9 stress;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        stress -i 10 &
        sleep 5;
        python2 test_comments.py 34 &
        sleep 60;
        killall -9 stress;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        stress-ng --vm-bytes $(awk '/MemAvailable/{printf "%d\n", $2 * 0.98;}' < /proc/meminfo)k --vm-keep -m 10  &
        sleep 5;
        python2 test_comments.py 35 &
        sleep 60;
        killall -9 stress-ng;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi


    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem loss 0.5%;
        sleep 5;
        python2 test_comments.py 36 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi
    
    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem loss 0.1%;
        sleep 5;
        python2 test_comments.py 37 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem loss 0.05%;
        sleep 5;
        python2 test_comments.py 38 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem loss 1%;
        sleep 5;
        python2 test_comments.py 39 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        sudo tc qdisc add dev eth0 root netem delay 0.01ms 0.01ms distribution normal;
        sleep 5;
        python2 test_comments.py 40 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        sudo tc qdisc add dev eth0 root netem delay 0.02ms 0.01ms distribution normal;
        sleep 5;
        python2 test_comments.py 41 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        sudo tc qdisc add dev eth0 root netem delay 0.03ms 0.01ms distribution normal;
        sleep 5;
        python2 test_comments.py 42 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        sudo tc qdisc add dev eth0 root netem delay 0.04ms 0.01ms distribution normal;
        sleep 5;
        python2 test_comments.py 43 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem duplicate 0.5%;
        sleep 5;
        python2 test_comments.py 44 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem duplicate 0.1%;
        sleep 5;
        python2 test_comments.py 45 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem duplicate 0.05%;
        sleep 5;
        python2 test_comments.py 46 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem duplicate 1%;
        sleep 5;
        python2 test_comments.py 47 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem corrupt 0.5%;
        sleep 5;
        python2 test_comments.py 48 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem corrupt 0.1%;
        sleep 5;
        python2 test_comments.py 49 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem corrupt 0.05%;
        sleep 5;
        python2 test_comments.py 50 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem corrupt 1%;
        sleep 5;
        python2 test_comments.py 51 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem reorder 0.5% delay 1ms;
        sleep 5;
        python2 test_comments.py 52 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem reorder 0.1% delay 1ms;
        sleep 5;
        python2 test_comments.py 53 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem reorder 0.05% delay 1ms;
        sleep 5;
        python2 test_comments.py 54 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root netem reorder 1% delay 1ms;
        sleep 5;
        python2 test_comments.py 55 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root tbf rate 600Mbit burst 32Mbit limit 30000;
        sleep 5;
        python2 test_comments.py 56 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root tbf rate 500Mbit burst 32Mbit limit 30000;
        sleep 5;
        python2 test_comments.py 57 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root tbf rate 550Mbit burst 32Mbit limit 30000;
        sleep 5;
        python2 test_comments.py 58 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        tc qdisc add dev eth0 root tbf rate 580Mbit burst 32Mbit limit 30000;
        sleep 5;
        python2 test_comments.py 59 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        tc qdisc del dev eth0 root;
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 1 &
        sleep 5;
        python2 test_comments.py 1 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 2 &
        sleep 5;
        python2 test_comments.py 2 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 3 &
        sleep 5;
        python2 test_comments.py 3 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 4 &
        sleep 5;
        python2 test_comments.py 4 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 5 &
        sleep 5;
        python2 test_comments.py 5 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 6 &
        sleep 5;
        python2 test_comments.py 6 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 7 &
        sleep 5;
        python2 test_comments.py 7 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 8 &
        sleep 5;
        python2 test_comments.py 8 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 9 &
        sleep 5;
        python2 test_comments.py 9 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 10 &
        sleep 5;
        python2 test_comments.py 10 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 11 &
        sleep 5;
        python2 test_comments.py 11 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 12 &
        sleep 5;
        python2 test_comments.py 12 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 13 &
        sleep 5;
        python2 test_comments.py 13 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 14 &
        sleep 5;
        python2 test_comments.py 14 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 15 &
        sleep 5;
        python2 test_comments.py 15 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 16 &
        sleep 5;
        python2 test_comments.py 16 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 4 &
        sleep 5;
        python2 test_comments.py 17 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 8 &
        sleep 5;
        python2 test_comments.py 18 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi


    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 12 &
        sleep 5;
        python2 test_comments.py 19 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 16 &
        sleep 5;
        python2 test_comments.py 20 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 20 &
        sleep 5;
        python2 test_comments.py 21 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 24 &
        sleep 5;
        python2 test_comments.py 22 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 28 &
        sleep 5;
        python2 test_comments.py 23 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 32 &
        sleep 5;
        python2 test_comments.py 24 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 36 &
        sleep 5;
        python2 test_comments.py 25 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 40 &
        sleep 5;
        python2 test_comments.py 26 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 44 &
        sleep 5;
        python2 test_comments.py 27 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 48 &
        sleep 5;
        python2 test_comments.py 28 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 64 &
        sleep 5;
        python2 test_comments.py 29 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 72 &
        sleep 5;
        python2 test_comments.py 30 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 96 &
        sleep 5;
        python2 test_comments.py 31 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 write_test.py 128 &
        sleep 5;
        python2 test_comments.py 32 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    
done
