# rename-to-match-folder

This script loops through all folders in a start directory and changes
all filenames inside folder to match name of folder with an index.

Good for renaming axioscan batch output tiffs to prefered filenames.
Prefered filenames can be set by renaming the folders.

Example: changing folder name from "RecognizedCode_2018-01-01_0933" to "Animal1_Slide1" will rename all files within that folder to "Animal_Slide1_i with i going from 1 to how many files are in the folder. 

!!!WARNING THIS SCRIPT WILL MESS UP ALL YOUR FILES IF YOU DONT WATCH OUT!!!
PROCEED WITH EXTREME CAUTION!!!

MAKE SURE ONLY FOLDERS WITH FILES TO BE RENAMED ARE PRESENT IN SELECTED PATH
OTHER FILES IN PATH SPACE MIGHT CAUSE ERRORS AND RENAMING TO STOP PREMATURELY

In case something happens, a log file is created which logs all the name changes. 
it is saved as "renaming_log_<date and time of namechange>.txt"
