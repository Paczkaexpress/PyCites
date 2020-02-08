# -- coding: utf-8 --

from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
import csv
import balloontip as ballTip
import time
import random

fileName = 'Kindle_Clippings.txt'
database = 'Kindle_Clippings.csv'
keyWord = '=========='

class clipping:
    book = ''
    date = ''
    cite = ''
    size = 0
    
def readFile():
    file = open(fileName,'r')
    fileRaw = file.read()
    print('text file uploaded')
    file.close()
    return fileRaw

def readCSVFile():
    temp = random.randint(0,clipping.size)
    print('size:' + str(clipping.size))
    print('rand:' + str(temp))
    with open(database) as csvfile:
        dataReader = csv.reader(csvfile,delimiter=';')
        dataReader = list(dataReader)
        print('##'+dataReader[temp][0]+'@@'+dataReader[temp][1]+'@@'+dataReader[temp][2]+'##')
        try:
            clipping.book = dataReader[temp][0]
            clipping.date = dataReader[temp][1]
            clipping.cite = dataReader[temp][2]
        except:
            print('Out of matrix exception')
                
def saveToCSV(fileRaw):
    start = 0
    end = 0
    pre_start = 0
    
    csvfile = open(database, 'w+') 
    fieldnames = 'title;data;citation\n'
    csvfile.write(fieldnames)

    while pre_start <= start:
        pre_start = start
        start = fileRaw.find('==========',start,len(fileRaw))+len(keyWord)+1
        end = fileRaw.find('\n',start,len(fileRaw))
        clipping.book = fileRaw[start:end]
        for i in range(end,len(fileRaw)):
            if not fileRaw[i].isspace():
                end = i
                break
        start = end
        
        end = fileRaw.find('\n',start,len(fileRaw))
        clipping.date = fileRaw[start:end]
        for i in range(end,len(fileRaw)):
            if not fileRaw[i].isspace():
                end = i
                break
        start = end
        
        end = fileRaw.find('\n',start,len(fileRaw))
        clipping.cite = fileRaw[start:end]
        for i in range(end,len(fileRaw)):
            if not fileRaw[i].isspace():
                end = i
                break
            
        clipping.size = clipping.size + 1
        csvfile.write(clipping.book + ';' + clipping.date + ';' + clipping.cite + '\n')

    csvfile.close()
    print('done')
    time.sleep(1) 
        
if __name__ == "__main__":
    fileRaw = readFile()
    saveToCSV(fileRaw)
    
    while True:
        readCSVFile();
        time.sleep(300) 
        print(clipping.book)
        print(clipping.cite)
        ballTip.balloon_tip(clipping.book,clipping.cite)