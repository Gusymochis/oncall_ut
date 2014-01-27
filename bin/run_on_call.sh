#!/bin/bash

echo "Starting script..." >>/home/pi/dev/on_call/log/on_call.log
python /home/pi/dev/on_call.py >>/home/pi/dev/on_call/log/on_call.log

