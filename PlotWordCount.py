# J YAP Sept 2020
# Script to plot thesis progress by accumulated word count
# Percentage of total words, accumulated word count and counts/entry over recorded entry dates

import os
import time
import sys
import math
import numpy as np
from decimal import Decimal

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

import datetime as dt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

f = open("TotalWordCount.txt","r")

dates = []
words = []

for line in f.readlines():            

 dates.append(line.split(' ')[1])
 words.append(line.split(' ')[2]) 

w = list(map(int, words))   # remove line break
wordcount = np.array(w)
datesX = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates] # Convert dates

# Trend
TotalCount = max(wordcount)
dispTotalCount = '{:,}'.format(TotalCount)
Percentage = wordcount/TotalCount*100

# Cumulative progress
progression = np.diff(w)    # differences between successive counts
progressionEntries = list(progression)
DateSpacing=np.diff(datesX)
# get bar positions by adding half the interval to each date
progressEqualDates = datesX[:-1]+DateSpacing/2

# Plot
fig = plt.figure()
fig.set_figheight(6)
fig.set_figwidth(12)
ax = plt.gca()
plt.title("Thesis Progress",y=1,fontsize=26,pad=20)
plt.xlabel('Entry date',fontsize=12,fontweight='bold',labelpad=10)

# y-axis: Percentage (right)
ax.plot(datesX,wordcount,marker='o',markersize=7,fillstyle='none',linewidth=2,color='black')
plt.ylabel('Accumulated Count\n [Total = '+str(dispTotalCount)+']',fontsize=12,fontweight='bold',rotation='horizontal',verticalalignment='center',labelpad=80)
plt.ylim(0, TotalCount*1.02) #same 5% padding
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
ax.yaxis.grid(which='major',linewidth=1.5,alpha=0.6)

# y-axis: Words (left)
ax1 = ax.twinx()
ax1.set_ylabel('Completion \n'' Percentage [%]',fontsize=12,fontweight='bold',rotation='horizontal',verticalalignment='center',labelpad=50)
ax1.plot(datesX, Percentage, color='black')
plt.ylim(0, 102)

# Progression bar plot
minLim=min(progressionEntries)*1.2
maxLim=max(progressionEntries)*1.1
equalFactor=maxLim-minLim
ax2 = ax.twinx()
barplot=plt.bar(progressEqualDates, progressionEntries, color ='b', width = 5)
plt.ylim(minLim,maxLim)
ax2.yaxis.set_label_coords(0, 1.02)
plt.axhline(y=0,color='b',linewidth='1')
plt.ylabel('Entry Count [words]',fontsize=12,fontweight='bold',color='b',rotation=360)
ax2.get_yaxis().set_label_position('left')
ax2.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) 
ax2.tick_params(axis='y',colors='b',pad=-669,width=0)
ax2.yaxis.grid(which='major',linestyle='--',color='b',alpha=0.3)

# x-axis: Date
plt.margins(x=0)
ax.xaxis.set_major_locator(mdates.DayLocator(interval=29))
ax.xaxis.set_major_formatter(DateFormatter('%b-%y'))
plt.setp(ax.get_xticklabels(),rotation = 45)

# saves plot automatically
date_string = time.strftime("%d-%m-%Y.%H%M")
savefile = 'TotalWordCount'+ date_string + ".png"
plt.savefig(savefile, dpi=300, bbox_inches='tight')
sys.stdout.write("Plot saved\n")