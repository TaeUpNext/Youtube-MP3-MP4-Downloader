#Modules needed for this user interface
from __future__ import unicode_literals
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
from pytube import YouTube #imports the library needed to download youtube videos
import os
import moviepy.editor as mp
import re
from tkinter import *
from tkinter import filedialog 

#Sets the window properties
master = Tk()
master.title("YouTube MP3/MP4 Downloader")
master.configure(bg='White')
master.minsize(700,460) #Sets the windows minmum size
master.maxsize(700,460) #Sets the windows maximum size

#Browse button
def browse_button():
  # Allow user to select a directory and store it in global var
  # # called folder_path
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)




#Function for the MP4 button to make the program start downloading the requested video
def mp4Download():
  url = urlEntryBox.get()
  resultsLabel.delete(0,END)
  yt = YouTube(url) # sets the vairable yt to the url the user inputted
  stream = yt.streams.get_highest_resolution()
  stream.download(filename)
  urlEntryBox.delete(0, END)
  completedMessage= ("DOWNLOAD FINISHED! Thank you for using this program")
  results.set(completedMessage)

#Function for the MP3 button to make the program start downloading the requested video
def mp3Download():
  url = urlEntryBox.get()
  resultsLabel.delete(0,END)
  yt = YouTube(url)
  t = yt.streams.filter(only_audio=True).all()
  t[0].download(filename) #downloads the youtube video audio only however the extension is .mp4
  #This for loop creates a file that converts .mp4 files to mp3 files
  for file in [n for n in os.listdir(filename) if re.search('mp4',n)]:
    full_path = os.path.join(filename, file)
    output_path = os.path.join(filename, os.path.splitext(file)[0] + '.mp3')
    clip = mp.AudioFileClip(full_path).subclip(10,) # disable if do not want any clipping
    clip.write_audiofile(output_path)
    urlEntryBox.delete(0, END)
    completedMessage= ("Your download has finished! Thank you for using this program")
    results.set(completedMessage)
    



#! User intface
#*Title Label
titleLblBorder = Label(master, width = 67, height = 3, bg = 'red') #Creates a duplicate of the title label but uses it for a red border effect under the normal label
titleLblBorder.grid(row = 0, padx = 43, pady = 17, column = 0, columnspan = 10, rowspan = 2, sticky = N)
titleLbl = Label(master, width = 35, height = 1, text = " Cryptic Downloader V1 ", font = ('Modak',28, 'bold'), bg = 'Black', fg = 'red' )
titleLbl.grid(row = 0, padx = 43, pady = 20, column = 0, columnspan = 10, rowspan = 5, sticky = N)

#Youtube URL & URL Entry Box
youtubeURLBorder = Label(master, width = 26, height = 3, bg = 'red') # This is the border for the URL Label (adds a red outline)
youtubeURLBorder.grid(row = 2, column = 0, sticky = E, pady = 25, padx = 2, rowspan = 2) # places border label on grid
youtubeURLLbl = Label(master, width = 15, height = 1,text = "YouTube URL", font = ('Modak',25, 'bold'), bg = 'Black', fg = 'red') # label for the youtube URL
youtubeURLLbl.grid(row = 2, column = 0, sticky = E, pady = 25, padx = 6, rowspan = 2) #places label on grid

urlEntryBox = Entry(master, width = 35, font = ('times new roman', 22) , bg = 'black' , fg = 'white', relief = 'sunken',insertbackground = 'white' ,border = 4, highlightthickness = 0, justify = 'center')
urlEntryBox.grid(row = 2, column = 2, sticky = W+E, pady = 30)


folder_path = StringVar()
destinationFolderBorder = Label(master, width = 26, height = 3, bg = 'red') # This is the border for the destination(adds a red outline)
destinationFolderBorder.grid(row = 4, column = 0, sticky = E, pady = 25, padx = 2, rowspan = 2) # places border label on grid
destinationFolderLbl = Label(master, width = 15, height = 1,text = "Destination", font = ('Modak',25, 'bold'), bg = 'Black', fg = 'red') # label for the destination
destinationFolderLbl.grid(row = 4, column = 0, sticky = E, pady = 25, padx = 6, rowspan = 2) #places label on grid
destinationFolder = Label(master, width = 25, font = ('times new roman', 22) ,textvariable = folder_path, background = 'black', justify = 'center', fg = 'white', relief = 'sunken', border = 4, highlightthickness = 0) # A read only entry box for the destination folder 
destinationFolder.grid(row = 4, rowspan = 2, column = 2, pady = 35, sticky = W)



browseBtn = Button(master, font = ('Modak',16, 'bold'), width = 10, height = 1, text = 'Browse', highlightcolor = 'red', bd = 2, relief = 'sunken', command = browse_button) # A read only entry box for the destination folder 
browseBtn.grid(row = 4, rowspan = 2, column = 2, pady = 35, sticky = E)


#MP# Downloader Button
MP3DownloadBtn = Button(master, font = ('Modak',16, 'bold'), width = 16, height = 2, text = 'MP3', highlightcolor = 'red', bd = 2, relief = 'sunken', command = mp3Download)
MP3DownloadBtn.grid(row = 7, rowspan = 2, column = 0, columnspan = 2, padx = 40, pady = 35, sticky = E)


MP4DownloadBtn = Button(master, command =  mp4Download,  font = ('Modak',16, 'bold'), width = 16, height = 2, text = 'MP4', highlightcolor = 'red', bd = 2, relief = 'sunken')
MP4DownloadBtn.grid(row = 7, rowspan = 2, column = 1, columnspan = 2, padx = 20, pady = 35, sticky = E)


results = StringVar()
resultsLabel = Entry(master, readonlybackground = 'black', text = results, fg = 'green', justify = 'center', state = 'readonly', width = 75, relief = 'sunken', border = 4, highlightthickness = 0)
resultsLabel.grid(row = 9, column = 0, columnspan = 7,  padx= 5)


master.mainloop()