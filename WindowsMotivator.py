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
        
class Clipping:
    clippingList = []

    keyWord = '=========='
    def __init__(self, txtFile):
        self.txtFile = txtFile + ".txt"
        self.readFile()
        print(self.fileRaw)
        self.prepareData()  

    def readFile(self):
        file = open(self.txtFile,'rt', encoding='utf-8')
        self.fileRaw = file.read()
        print('text file uploaded')
        file.close()

    def prepareData(self):
        start = 0
        end = 0
        pre_start = 0

        while pre_start <= start:
            pre_start = start
            start = self.fileRaw.find(self.keyWord,start,len(self.fileRaw))+len(self.keyWord)+1
            end = self.fileRaw.find('\n',start,len(self.fileRaw))
            book = self.fileRaw[start:end]
            for i in range(end,len(self.fileRaw)):
                if not self.fileRaw[i].isspace():
                    end = i
                    break
            start = end
            
            end = self.fileRaw.find('\n',start,len(self.fileRaw))
            date = self.fileRaw[start:end]
            for i in range(end,len(self.fileRaw)):
                if not self.fileRaw[i].isspace():
                    end = i
                    break
            start = end
            
            end = self.fileRaw.find('\n',start,len(self.fileRaw))
            cite = self.fileRaw[start:end]
            for i in range(end,len(self.fileRaw)):
                if not self.fileRaw[i].isspace():
                    end = i
                    break
            self.clippingList.append((book, date, cite))    

        print('data preparation finished')
        time.sleep(1) 

    def returnRandomCite(self):
        randomPick = random.randint(0, len(self.clippingList))
        return self.clippingList[randomPick][0], self.clippingList[randomPick][2]


if __name__ == "__main__":
    clip = Clipping("Kindle_Clippings")
    for x in clip.clippingList:
        print(x)
    while True:
        print(clip.returnRandomCite())
        book, cite = clip.returnRandomCite()
        ballTip.balloon_tip(book, cite)
        Sleep(300)