import requests
from espeak import espeak
from time import sleep

urls= ['http://pdevicnos100.corp.intuit.net:8080/jenkins/view/ICN%20Services/view/CoreTrunk/job/ICN_Core_Trunk_Build/api/json',
'http://pdevicnos100.corp.intuit.net:8080/jenkins/view/ICN%20Services/view/ChatTrunk/job/ICN_Chat_Trunk_Build/api/json']


def checkLatestBuild(url):
    r = requests.get(url)
    job_detail = r.json()
    print r.status_code
    print job_detail['displayName']
    lastBuildUrl = job_detail['lastBuild']['url']
    print lastBuildUrl

    last_build_req = requests.get(lastBuildUrl + '/api/json')
    print last_build_req.status_code

    last_build_detail = last_build_req.json()
    print last_build_detail['result']

    #os.system("say " + str(last_build_detail['fullDisplayName']))
    #os.system("say 'build '" + str(last_build_detail['number']) + "' result '" + last_build_detail['result'])
   
    espeak.synth("hi") 
    return

for url in urls:
    checkLatestBuild(url)

