#!/bin/bash

GIT_REPO=/home/pi/ut_repo/oncall_ut/

echo "Getting ip"
su pi -c "ifconfig eth0 | grep inet | cut -d':' -f2 | awk '{ print $1}' > /home/pi/ut_repo/oncall_ut/pi_list/`hostname`"
echo "running git"
sudo -u pi -i git --git-dir=$GIT_REPO/.git --work-tree=/$GIT_REPO pull
sudo -u pi -i git --git-dir=$GIT_REPO/.git --work-tree=/$GIT_REPO add pi_list/*
sudo -u pi -i git --git-dir=$GIT_REPO/.git --work-tree=/$GIT_REPO commit -m "`hostname` started"
sudo -u pi -i git --git-dir=$GIT_REPO/.git --work-tree=/$GIT_REPO push origin
