#Created by DarkByte
#A neopets captcha solver with 100% accuracy
#========================================================
#This works because neopets only has 1,000 captcha images
#This script has the md5 hash and the valid coordinates for all 1k images
#The script performs zero image functions it just looks up the md5 hash of
#the file you request and returns the valid x,y
#========================================================
from class_captcha import class_captcha

captcha_manager = class_captcha()
captcha_result = captcha_manager.getcoordinates("testcaptcha.jpeg")
print "Result: \nx = " + captcha_result["x"]
print "y = " + captcha_result["y"]
