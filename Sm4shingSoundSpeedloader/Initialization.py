#Grabs info from  RAW_ID_LIST.txt  and prepares it
from string import *
import Buttons
from collections import defaultdict
from os import getcwd
import wx

f = open('RAW_ID_LIST.txt', 'r')
RAWline = f.readline()

MasterList = defaultdict(list)
NameLookup = {}
StageNameInfo = defaultdict(list)
#Save base working directory for default path location
wd = getcwd()
title = ''

while RAWline != '':

    #Checking against titles
    if(RAWline[0] != '<'):
        #negate '-----------------------'
        RAWline = f.readline()
        #set title
        title = RAWline[:RAWline.find('\n')]
        #negate and grab newline
        f.readline()
        RAWline = f.readline()
        continue

    RAWname = RAWline[RAWline.find('<')+1:RAWline.find('>')]
    name = RAWline[RAWline.find('- ')+2:RAWline.find('\n')]
    #print(name)
    #print(RAWname)    
    
    #list of track names sorted by world
    MasterList[title].append(name)

    #Create Info container for loading Panel2
    StageNameInfo[title].append( (name, 'N', 'N/A') )

    #dictionary with level names as keys for RAW names
    NameLookup[name] = RAWname


    #Get next line in file
    RAWline = f.readline()


#print(MasterList)


