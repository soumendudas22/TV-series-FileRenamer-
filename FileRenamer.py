
'''
FILE RENAMER v1.0
STEPS TO BE FOLLOWED :
1. COPY THIS FILE TO THE PLACE YOU WANT TO RENAME THE FILES AND FOLDERS
2. RUN THE PROGRAM
3. VOALA!! ALL FILES RENAMED WITH INSTANT CLICK

NEXT VERSION UNDER DEVELOPMENT...
'''

import os

#1. get the list of folders
listOfFolders = os.listdir()

#2. Rename all the folders
season = 0
for folder in listOfFolders:
    if folder == 'FileRenamer.exe':
        continue
    season+=1
    os.rename(folder,"S{}".format(season))

#3. get current directory
current = os.getcwd()


#4. get inside each folder(by changing directory)
for folder in listOfFolders:

    if folder == 'FileRenamer.exe':
        continue
    
    os.chdir(current + "\\" + folder)
    
    #get the list of files
    listOfFiles = os.listdir()
    
    #rename each and everey file present
    episode = 0
    for file in listOfFiles:
        episode += 1
        if file.endswith(".txt"):
            os.rename(file,"E{}.mp4".format(episode)) #for mp4 file
        if file.endswith(".mkv"):
            os.rename(file,"E{}.mkv".format(episode)) #for matroska file
    #after renaming the files come back to main
    os.chdir(current)

input()
