#Modules needed for this user interface
from __future__ import unicode_literals
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
from pytube import YouTube #imports the library needed to download youtube videos
import os
import moviepy.editor as mp
import re
from tkinter import *

#Sets the window properties
master = Tk()
master.title("YouTube MP3/MP4 Downloader")
master.configure(bg='White')
master.minsize(700,460) #Sets the windows minmum size
master.maxsize(700,460) #Sets the windows maximum size


#! User intface
#*Title Label
titleLabelBorder = Label(master, width = 67, height = 3, bg = 'red') #Creats a duplicate of the title label but uses it for a red border effect under the normal label
titleLabelBorder.grid(row = 0, padx = 47, pady = 17, column = 0, columnspan = 10, rowspan = 2, sticky = N)
titleLabel = Label(master, width = 35, height = 1, text = " YouTube MP3/MP4 Downloader ", font = ('Modak',28, 'bold'), bg = 'Black', fg = 'red' )
titleLabel.grid(row = 0, padx = 47, pady = 20, column = 0, columnspan = 10, rowspan = 2, sticky = N)


master.mainloop()