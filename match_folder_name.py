#Author: Robert Pretorius 2018
"""

This script loops through all folders in a start directory and changes
all filenames inside folder to match name of folder with an index.

Good for renaming axioscan batch output tiffs to prefered filenames.

!!!WARNING THIS SCRIPT WILL MESS UP ALL YOUR FILES IF YOU DONT WATCH OUT!!!
PROCEED WITH EXTREME CAUTION!!!

MAKE SURE ONLY FOLDERS WITH FILES TO BE RENAMED ARE PRESENT IN SELECTED PATH
OTHER FILES IN PATH SPACE MIGHT CAUSE ERROS AND RENAMING TO STOP PREMATURELY
"""

import os
import time

from time import localtime, strftime
time_now = strftime("%Y-%m-%d-%Hh%Mm%Ss", localtime())

#set starting directory and file extansion
path = "E:/3D reconstruction/A4" #UNCOMMENT TO START, BEWARE
file_extension = ".tif" 

os.chdir(path)
log_name = "renaming_log_" + time_now + ".txt"
log_name = str(log_name)
log = open(log_name,'a')

print(os.getcwd())
log.write((os.getcwd()))
log.write("\n")
folders = os.listdir()

#looping through all the folders
for folder in folders:
    newpath = path + "/"+folder
    os.chdir(newpath)
    print(os.getcwd())
    log.write(os.getcwd())
    log.write("\n")

    #loop through files in folder
    i = 1
    for file in os.listdir():
        new_name =folder + "_" + str(i) + "_" + file_extension
        i = i+1
        prompt = "renamed " + file + " to " + new_name
        print(prompt)
        log.write(prompt)
        log.write("\n")
        os.rename(file,new_name)

log.close()
