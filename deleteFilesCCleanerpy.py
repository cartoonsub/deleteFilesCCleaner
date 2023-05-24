import re
import os
import sys
import shutil
from time import sleep

def getFile() -> str:
    needFile = ''
    # os.chdir('deleteFilesCCleaner')
    curentDir = os.getcwd()
    for root, dirs, files in os.walk(curentDir):
        if not files:
            continue
        for file in files:
            if file.find('delete.txt') == -1:
                continue
            currentFile = os.path.join(root, file)
            needFile = currentFile
            return needFile
    return needFile

def readFile(file) -> list:
    fileList = []
    tempList = []
    extensions = [
        'JPG', 'jpg', 'mp4', 'MP4', "CR2"
    ]
    pattern = r"([\w.\s_()-]+\.\w+)\s+([a-zA-Z]:[\[\]!(),._\\\w\s-]+)\s+\d+[,\d]*\s+[МБMBKКГG]+"

    with open(file, 'r', encoding="utf8") as file:
        for line in file:
            if not line:
                break
            if re.match(r"-{10}", line):
                if not tempList:
                    continue
                fileList.append(tempList)
                tempList = []
                continue
            matches = re.search(pattern, line, re.IGNORECASE|re.UNICODE)
            if not matches:
                continue
            allMatches = matches.groups()
            extension = matches[1].split('.')[-1]
            if not extension in extensions:
                continue
            path = matches[2] + '\\' + matches[1]
            tempList.append(path)

    if not fileList:
        exit()
    with open('file.txt', 'w', encoding="utf8") as file:
        for text in fileList:
            file.write(str(text))
    
    return fileList

def prepareFiles(files) -> list:
    filesForDelete = []
    for line in files:
        fileForDelete = shooseFileForDelete(line)
        if not fileForDelete:
            continue

        filesForDelete.append(fileForDelete)
    return filesForDelete

def shooseFileForDelete(files):
    patterns = [
        r"YandexDisk[\\]+Фотокамера",
    ]
    for file in files:
        for pattern in patterns:
            if not re.search(pattern, file, re.IGNORECASE):
                continue

            return file



file = getFile()
if not file:
    print('file not found')
    exit()

files = readFile(file)
if not files:
    print('files not found')
    exit()

filesForDelete = prepareFiles(files)
for file in filesForDelete:
    if not os.path.isfile(file):
        print('file not found' + file)
        continue
    
    os.remove(file)

print(filesForDelete)