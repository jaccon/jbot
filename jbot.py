# -*- coding: utf-8 -*-
import requests

import os
import json
current = os.getcwd()

scriptDir = "/scripts.pagefai/jbot/"

class Foo:
    
    f = open (scriptDir +'/config.json', "r")
 
    data = json.loads(f.read())
    
 
    def executeTask(t):
        
        status = t["status"]
        task = t["execute"]

        print (" === " + task + " - " + status + "===")
        
        if status == "enabled":
            
            os.system("python " +scriptDir +"/components/" + task+ ".py")
            
    
    for i in data['tasks']:
        executeTask(i)
 
    f.close()
