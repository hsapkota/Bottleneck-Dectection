#!/bin/bash

wait_period=0

while true
do
    echo "wait period ${wait_period}"
    if [ $wait_period -gt 10800 ];then
       break
    fi

    
	python2 test_commands.py 0 &
	sleep 60;
	killall -9 python2;
    killall -9 java;
	wait_period=$(($wait_period+60));
	sleep 5;


    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 20 &
        sleep 5;
        python2 test_commands.py 1 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 21 &
        sleep 5;
        python2 test_commands.py 2 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 22 &
        sleep 5;
        python2 test_commands.py 3 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 23 &
        sleep 5;
        python2 test_commands.py 4 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 24 &
        sleep 5;
        python2 test_commands.py 5 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 25 &
        sleep 5;
        python2 test_commands.py 6 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 26 &
        sleep 5;
        python2 test_commands.py 7 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 27 &
        sleep 5;
        python2 test_commands.py 8 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 28 &
        sleep 5;
        python2 test_commands.py 9 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 32 &
        sleep 5;
        python2 test_commands.py 10 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 48 &
        sleep 5;
        python2 test_commands.py 11 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 49 &
        sleep 5;
        python2 test_commands.py 12 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 50 &
        sleep 5;
        python2 test_commands.py 13 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 64 &
        sleep 5;
        python2 test_commands.py 14 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 65 &
        sleep 5;
        python2 test_commands.py 15 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi

    number=$RANDOM
    if [ $((number%2)) -eq 0 ]
    then
        python2 read_test.py 66 &
        sleep 5;
        python2 test_commands.py 16 &
        sleep 60;
        killall -9 python2;
        killall -9 java;
        wait_period=$(($wait_period+60));
        sleep 5;
    fi
    
done

