# python file called by .bat
# sums up the word total for each chapter and appends this with the time & date to a new line in TotalWordCount.txt
# J Yap, 2020

import os
import time
import sys
import numpy as np

n=1
maxfilenumb=8
output = []
date_string=time.strftime("%H%M %d/%m/%Y")

outputf = open("TotalWordCount.txt","a")

chapt1 = open("count1.txt","r")
wc1=chapt1.read()
        
chapt2 = open("count2.txt","r")
wc2=chapt2.read()

chapt3 = open("count3.txt","r")
wc3=chapt3.read()

chapt4 = open("count4.txt","r")
wc4=chapt4.read()

chapt5 = open("count5.txt","r")
wc5=chapt5.read()

chapt6 = open("count6.txt","r")
wc6=chapt6.read()

chapt7 = open("count7.txt","r")
wc7=chapt7.read()

abstract = open("count8.txt","r")
wc8=abstract.read()

totals=np.int(wc1)+np.int(wc2)+np.int(wc3)+np.int(wc4)+np.int(wc5)+np.int(wc6)+np.int(wc7)+np.int(wc8)

output=date_string,totals

s = " ".join(map(str, output))
    
outputf.write(s+'\n')                    

outputf.close()
