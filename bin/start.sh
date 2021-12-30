#!/bin/bash
echo $#
echo $2
echo $1
 
#  creare logs dir
mkdir -p logs
 
#start work default
if [ "$1"  = "start" ]
then
    python3 run_http.py
    exit
fi
 
##stop work
if [ "$1"  = "stop" ]
then
    ps -ef  |grep run_http.py  |awk '{print $2}'  |while read pid
        do
            kill -9 $pid
        done
fi
 
##restart work
if [ "$1"  = "restart" ]
then
    ps -ef  |grep run_http.py  |awk '{print $2}'  |while read pid
        do
            kill -9 $pid
        done
 
    python3 run_http.py
    exit
fi