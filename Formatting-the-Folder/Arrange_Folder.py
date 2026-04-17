'''
Author: Adityaraj Yadav 
Date: 2 January 2022
Project Name: Formating the Folder
Purpose:For Practising Purpose
'''

import os

def createIfNotExist(folder):
    if not os.path(folder):
        os.makdir(folder)

def moveFolder(foldername,files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

files = os.listdir()
files.remove("Arrange.py")
print(files)

createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Others')

ImageExten = ['.png','.jpg','.jpeg']
Images = [file for file in files if os.path.splittext(file)[1] in ImageExten]

DocsExten = ['.pdf','.txt','.doc','.docx']
Docs = [file for file in files if os.path.splittext(file)[1] in DocExten]

MediaExten = ['.mp4','.mp3','.flv']
Media = [file for file in files if os.path.splittext(file)[1] in MediaExten]

Others = []
for file in files:
    other = os.path.splittext(file)[1]
    if other not in MediaExten and other not in DocsExten and other not in ImageExten:
        Others.append(file)

move("Images", Images)
move("Docs", Docs)
move("Media", Media)
move("Others", Others)
