#!/bin/bash

python2 test_commands.py 30 &
sleep 600;
killall -9 python2;
killall -9 java;
#wait_period=$(($wait_period+60));
#sleep 10;

