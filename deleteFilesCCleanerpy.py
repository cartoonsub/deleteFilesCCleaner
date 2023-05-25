import re
import os
import sys
import shutil
import codecs
from time import sleep
from pprint import pprint

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

    with codecs.open(file, 'r', encoding="utf16") as file:
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
        # r"YandexDisk[\\]+Фотокамера",
        # r"YandexDisk[\\]+",
        # r"YandexDisk.+greece.+camera",
        # r"YandexDisk.+DCIM",
        # r"YandexDisk.+phone.+Camera",
        r"myphone[\\]+DCIM[\\]+Camera",
    ]
    data = {}
    for key in range(len(files)):
        file = files[key]
        for pattern in patterns:
            if not re.search(pattern, file, re.IGNORECASE):
                continue

            data['delete'] = file
            data['keep'] = files[key - 1]
            break
            
    if 'delete' not in data:
        data = {}
    return data



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
    if not os.path.isfile(file['delete']):
        print('file not found' + file['delete'])
        continue
    
    os.remove(file['delete'])

for file in filesForDelete:
    print(file['delete'])
    print(file['keep'])
    print('-----------------')