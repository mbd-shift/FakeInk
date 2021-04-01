#python
import pyautogui as pag
from python_imagesearch.imagesearch import imagesearch
import time
import os

pag.PAUSE=0

while(1):
    jobs=[]
    for i in os.popen("wmic printjob get jobid").read().split("\n"):
        try:
            jobs.append(int(i))
        except:
            None
    if("Druckvorgang" in os.popen("wmic printjob get jobstatus").read()):
              
        pos=imagesearch('schliessen.png')
        if pos[0] != -1:
            sp=pag.position()
            pag.moveTo([pos[0]+50,pos[1]+20])
            pag.click()
            pag.moveTo(sp)
            time.sleep(25)
        else:
            None
    else:
        time.sleep(0.3)
    