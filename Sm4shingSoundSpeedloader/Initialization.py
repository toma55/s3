#Grabs info from  RAW_ID_LIST.txt  and prepares it
from string import *
import Buttons
from collections import defaultdict
from os import getcwd
import wx
import os.path

f = open('RAW_ID_LIST.txt', 'r')
RAWline = f.readline()

MasterList = defaultdict(list)
NameLookup = {}
StageNameInfo = defaultdict(list)
LevelNames = []
#Save base working directory for default path location
wd = getcwd()
title = ''

profileExist = os.path.exists('myfile.dat')

while RAWline != '':

    #Checking against titles
    if(RAWline[0] != '<'):
        #negate '-----------------------'
        RAWline = f.readline()
        #set title
        title = RAWline[:RAWline.find('\n')]
        LevelNames.append(title)
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

    if not profileExist:
        print("Profile creation in progress\n")
        #Create Info container for loading Panel2
        StageNameInfo[title].append( (name, 'N', 'N/A') )

    #dictionary with level names as keys for RAW names
    NameLookup[name] = RAWname


    #Get next line in file
    RAWline = f.readline()
f.close()




#load profile 'myfile.dat'
if profileExist == True:
    f = open('myfile.dat', 'r')
    RAWline = f.readline()
    title = ''

    while RAWline != '':
        if RAWline[0] == '$':
            title = RAWline[1:RAWline.find('\n')]
            RAWline = f.readline()
            print(title)
            continue

        index1 = RAWline.find('~@~')
        index2 = RAWline.find('~~@')
        track = RAWline[:index1]
        isCustom = RAWline[index1+3:index2]
        ctrack = RAWline[index2+3:-1]
        print(' ' + track + ' ' + isCustom + ' ' + ctrack)
        StageNameInfo[title].append( (track, isCustom, ctrack) )
        RAWline = f.readline()
        
    f.close()
    #print StageNameInfo
    print("myfile.dat was found and loaded")
