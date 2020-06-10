#!/bin/bash
echo "First arg: $1"
iperf3 -P 128 -c 192.67.81.142
