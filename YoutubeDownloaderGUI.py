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
titleLblBorder = Label(master, width = 67, height = 3, bg = 'red') #Creates a duplicate of the title label but uses it for a red border effect under the normal label
titleLblBorder.grid(row = 0, padx = 47, pady = 17, column = 0, columnspan = 10, rowspan = 2, sticky = N)
titleLbl = Label(master, width = 35, height = 1, text = " YouTube MP3/MP4 Downloader ", font = ('Modak',28, 'bold'), bg = 'Black', fg = 'red' )
titleLbl.grid(row = 0, padx = 47, pady = 20, column = 0, columnspan = 10, rowspan = 5, sticky = N)

#Youtube URL & URL Entry Box
youtubeURLBorder = Label(master, width = 26, height = 3, bg = 'red') # This is the border for the URL Label (adds a red outline)
youtubeURLBorder.grid(row = 2, column = 0, sticky = E, pady = 25, padx = 2, rowspan = 2) # places border label on grid
youtubeURLLbl = Label(master, width = 15, height = 1,text = "YouTube URL", font = ('Modak',25, 'bold'), bg = 'Black', fg = 'red') # label for the youtube URL
youtubeURLLbl.grid(row = 2, column = 0, sticky = E, pady = 25, padx = 6, rowspan = 2) #places label on grid

urlEntryBox = Entry(master, width = 35, font = ('times new roman', 22) , bg = 'black' , fg = 'white', relief = 'sunken',insertbackground = 'white' ,border = 4, highlightthickness = 0, justify = 'center')
urlEntryBox.grid(row = 2, column = 2, sticky = W+E, pady = 30)





#destination folder URL & Entry Box
destinationString = StringVar()
destinationString.set("./desktop") #destination file for the downloads
destinationFolderBorder = Label(master, width = 26, height = 3, bg = 'red') # This is the border for the destination(adds a red outline)
destinationFolderBorder.grid(row = 4, column = 0, sticky = E, pady = 25, padx = 2, rowspan = 5) # places border label on grid
destinationFolderLbl = Label(master, width = 15, height = 1,text = "Destination", font = ('Modak',25, 'bold'), bg = 'Black', fg = 'red') # label for the destination
destinationFolderLbl.grid(row = 4, column = 0, sticky = E, pady = 25, padx = 6, rowspan = 5) #places label on grid

destinationFolderEntry = Entry(master, state = 'readonly', textvariable = destinationString, width = 35, font = ('times new roman', 22) , readonlybackground = 'black', justify = 'center', fg = 'white', relief = 'sunken', border = 4, highlightthickness = 0) # A read only entry box for the destination folder 
destinationFolderEntry.grid(row = 4, column = 2, sticky = W+E, pady = 35)


master.mainloop()