import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from pytube import YouTube #imports the library needed to download youtube videos

#Global Variables (Variables the whole program will mostly use)
x = 0 #used for while loops for the number of downloads to perform
videoDownloadFolder = ("/Volumes/ITSSD/Youtube/VideoDownloads") #full pathway for the folder you want videos saved too
MP3DownloadFolder = ("/Volumes/ITSSD/Youtube/MP3Downloads") #full pathway of the folder you want the mp3 saved too

#Program Starts Here
while True:
  try:
    downloaderChoice = eval(input("\nWould you like to download an MP3, MP4 or both? Please enter a 1 for MP3, a 2 for an MP4 or a 3 for both: ")) #Input to check what the user would like to download
    if downloaderChoice in range(1, 4):
      break
  except NameError: # Catches errors when a user enters a letter, word, sentence instead of a number
    print("\nThat is not a number, please try again...")
  except SyntaxError: #Catches errors when a user enters nothing or a character that is not recognized 
    print("\nYou did not type in anything or typed in an incorrect character, please try again...")
  
#Program that runs if the user wants to just download an MP4
if downloaderChoice == 2:     
  while True:
    try:
      numberOfDownloads = eval(input("\nHow many videos would you like to download? Number cannot be less than 1 or greater than 10: "))
      if numberOfDownloads in range(1, 11):
        break
      else:
        print('\nYou entered either a number less than 1 or greater than 10, please try again...')
    except NameError: # Catches errors when a user enters a letter, word, sentence instead of a number
      print("\nThat is not a number, please try again...")
    except SyntaxError: # Catches errors when a user enters nothing or a character that is not recognized 
      print("\nYou did not type in anything or typed in an incorrect character, please try again...")
      
  while x <=  numberOfDownloads: # while loop to check if you entered the correct url then downloads each video for the number of urls the user needed
          titleCorrect = False # variable to keep the program in a loop if the user doesnt have the correct video 
          while titleCorrect == False:
            urlDownload = input('\nPlease enter the url for the video you would like to download: \n') #input for the user to paste or type the video URL into
            yt = YouTube(urlDownload) # sets the vairable yt to the url the user inputted
            stream = yt.streams.get_highest_resolution()
            while True:
              try:
                ytTitle = eval(input(f"\nThe video title for the url you inputted is {yt.title} if this is correct enter a 1 for yes or a 2 for no: "))
                if ytTitle in range(1,3):
                  break
                else:
                  print('\nYou entered either a number less than 1 or greater than 10, please try again...')
              except NameError: # Catches errors when a user enters a letter, word, sentence instead of a number
                print("\nThat is not a number, please try again...")
              except SyntaxError: #Catches errors when a user enters nothing or a character that is not recognized 
                print("\nYou did not type in anything or typed in an incorrect character, please try again...")          
            if ytTitle == 1:
              stream.download(videoDownloadFolder) #downloads the youtube video and puts it into the folder 
              x += 1
              titleCorrect = True #ends the loop confirming that the title of the video is the correct one
              break
            elif ytTitle == 2: #Makes the user reinput the url to ensure the right video is being downloaded 
              print("\nYou inputted the wrong URL, please try again...")
              ytTitle = False 
              
          downloadThumbnail = False    
          while downloadThumbnail == False: #while loop to determien if the user wants to download the thumbnail aswell
            while True:
              try:
                thumbnailChoice = eval(input('Would you like to download the thumbnail?: Enter a 1 for a yes or a 2 for a no: '))
                if thumbnailChoice in range(1,3):
                  break
                else:
                  print("\nYou entered either a number less than 1 or greater than 3. Please try again...")
              except NameError: # Catches errors when a user enters a letter, word, sentence instead of a number
                print("\nThat is not a number, please try again...")
              except SyntaxError: #Catches errors when a user enters nothing or a character that is not recognized 
                print("\nYou did not type in anything or typed in an incorrect character, please try again...")   
          if thumbnailChoice == 1:
            print(f"\nURL for the thumbnail is {yt.thumbnail_url}")
            downloadThumbnail = true
          if thumbnailChoice == 2:
            print("\nYour Video is finished/ or is finishing, please check the designated download folder")
              
              
            
          