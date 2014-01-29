import subprocess
import new_parse_csv

def speak_now(text):
    subprocess.call(["./bin/run_espeak.sh", text])

data = new_parse_csv.get_oncall()
print data
speak_now(data)

subprocess.call(["mplayer", "final.mp3"])
 
