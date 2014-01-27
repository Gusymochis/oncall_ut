#!/bin/bash

echo "Starting script..." >>/home/pi/dev/on_call/log/on_call.log
python /home/pi/ut_repo/oncall_ut/parse_csv.py >>/home/pi/dev/on_call/log/on_call.log

