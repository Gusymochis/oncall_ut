On Monday morning before coffee, we don't remember to hand over the on-call duty.
A simple python script which reads the on-call schedule every monday to remind the persons on call this week.


Steps:
Create an entry in crontab to run shell script run_on_call.sh.
$crontab -e
Add an entry.  This schedule runs the shell script every min Mon - Fri.
* * * * 1-5    ~/ut_repo/oncall_ut/bin/run_on_call.sh
