#Created by DarkByte
#A neopets captcha solver with 100% accuracy
import json 
import os
import hashlib
import random

class class_captcha:
    def __init__(self):
        settingsfile = "captcha.dat"
        with open(settingsfile) as data_file:    
            self.settings = json.load(data_file)  

    def getcoordinates(self,captchaimage):
        try:
            thehash = hashlib.md5(open(captchaimage, 'rb').read()).hexdigest() #Convert the img to a md5 hash....
            captchaline = self.settings["captchadata"][thehash]
            captch_coords = captchaline.split(",") #Split captcha coords at comma
            
            Xlow = int(captch_coords[0])
            Ylow = int(captch_coords[1])
            Xhigh = int(captch_coords[2])
            Yhigh = int(captch_coords[3])
            Xrand = random.randrange(Xlow, Xhigh) #Random number betweeb Xlow and Xhigh
            Yrand = random.randrange(Ylow, Yhigh) #Random number betweeb Ylow and Yhigh
            return {"x" : str(Xrand),
                    "y" : str(Yrand)}
        except:
            return ["0","0"] #Error occured , this will only happen if neopets add new images to counter this script , right now this wont happen





