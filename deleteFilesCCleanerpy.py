import re
import os
import sys
import shutil
from time import sleep

def getFile() -> str:
    needFile = ''
    os.chdir('deleteFilesCCleaner')
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

    pattern = r"([\w.\s_()]+\.\w+)\s+([a-zA-Z]:[\[\]!(),._\\\w\s-]+)\s+\d+[,\d]*\s+[МБMBKКГG]+"

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
            path = allMatches[2] + '\\' + allMatches[1]
            tempList.append(line)

    if not fileList:
        exit()
    with open('file.txt', 'w', encoding="utf8") as file:
        for text in fileList:
            file.write(str(text))
    
    return fileList

def prepareFiles(files) -> list:
    filesForDelete = []
    for file in files:
        for line in file:
            matches = re.search(r"([\w.\s_()]+\.\w+)\s+([a-zA-Z]:[\[\]!(),._\\\w\s-]+)\s+\d+[,\d]*\s+[МБMBKКГG]+", line, re.IGNORECASE|re.UNICODE)
            if not matches:
                continue
            filesForDelete.append(matches[2])
    return filesForDelete


file = getFile()
if not file:
    print('file not found')
    exit()

files = readFile(file)
if not files:
    print('files not found')
    exit()

# filesForDelete = prepareFiles(files)