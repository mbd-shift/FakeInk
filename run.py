#python
import pyautogui as pag
from python_imagesearch.imagesearch import imagesearch
import time
import os

pag.PAUSE=0

targets=['schliessen.png','fortfahren.png']
printingprocess="Druckvorgang" # -> Start a print Queue, then use >>wmic printjob get jobstatus<< in cmd for local language

while(1):
    if(printingprocess in os.popen("wmic printjob get jobstatus").read()):
        for target in targets:
            pos=imagesearch(target)
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
    