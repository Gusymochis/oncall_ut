#!/bin/bash

echo "Starting script..." >>/home/pi/dev/log/on_call.log
python /home/pi/dev/on_call.py >>/home/pi/dev/log/on_call.log

