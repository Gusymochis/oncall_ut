#!/bin/bash

echo "Starting script..." >>/home/pi/dev/on_call/log/on_call.log
python /home/pi/ut_repo/oncall_ut/email_test.py >>/home/pi/dev/on_call/log/on_call.log

