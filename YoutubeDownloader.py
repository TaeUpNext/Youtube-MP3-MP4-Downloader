import pytube #imports the library needed to download youtube videos

videoDownloadFolder = ("/Volumes/ITSSD/Youtube/VideoDownloads") #full pathway for the folder you want videos saved too
MP3DownloadFolder = ("/Volumes/ITSSD/Youtube/MP3Downloads") #full pathway of the folder you want the mp3 saved too


while True:
  try:
    downloaderChoice = input("\nWould you like to download an MP3, MP4 or both? Please enter a 1 for MP3, a 2 for an MP4 or a 3 for both: ") #Input to check what the user would like to download
  except NameError: # Catches errors when a user enters a letter, word, sentence instead of a number
    print("\nThat is not a number, please try again...")
  except SyntaxError: #Catches errors when a user enters nothing or a character that is not recognized 
    print("\nYou did not type in anything or typed in an incorrect character, please try again...")
  else:
    if downloaderChoice in range(1, 4):
      break
    else:
      print("\nInvalid number choice, please try again...")
      
while True:
  try:    
    if downloaderChoice == 2: #Determiens the user would like to download an MP4 and executes the program to do so 
      numberOfDownloads = input("How many videos would you like to download?: ")
  except NameError: # Catches errors when a user enters a letter, word, sentence instead of a number
    print("\nThat is not a number, please try again...")
  except SyntaxError: #Catches errors when a user enters nothing or a character that is not recognized 
    print("\nYou did not type in anything or typed in an incorrect character, please try again...")
  else:
    for i in numberOfDownloads:
      urlInput = input("please enter or copy/paste the url of video you would like to download from YouTube: ") #has the user paste the url of the Youtube Video
      youtube = pytube.YouTube(urlInput) #loads the url in function Youtube
      
      video = youtube.streams.get_highest_resolution() #gets the highest resolution for the video you
      
      
      
      break
    else:
      print("\nInvalid number choice, please try again...")
      