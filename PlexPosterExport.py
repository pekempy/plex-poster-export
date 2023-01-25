# Set variables here, otherwise you will be asked them during script run
baseurl = 'http://127.0.0.1:32400'
token = ''

######################################################################################################
#                                                                                                    #
# - Movie Libraries -> Download poster and place next to video as poster.png                         # 
# - TV Libraries -> Download show poster, place in root folder for show as poster.png                #
#                -> Download season poster and save to season folder as poster.png                   #
#                -> Download episode title card, place next to episode named the same as episode     #
#                                                                                                    #
######################################################################################################

from plexapi.server import PlexServer
from plexapi.utils import download
from plexapi import video
if baseurl == '' and token == '' :
    baseurl = input('What is your Plex URL:  ')
    token = input('What is your Plex Token:  ')
repeat = True
plex = PlexServer(baseurl, token)
    
def runScript():
    # list libraries for user to select which to export from
    sectionList = [x.title for x in plex.library.sections()]
    print(" ")
    print ("  Your Libraries: ")
    for i in sectionList:
        print ("      " + str(sectionList.index(i)) + " - " + i)

    selectedLibrary = int(input("Enter the number of the library to export posters from:  "))
    selectedLibraryType = plex.library.section(sectionList[selectedLibrary]).type
    selectedLibraryItems = plex.library.section(sectionList[selectedLibrary]).search()

    if selectedLibraryType == "movie" :
        # loop through movies and export poster
        for video in selectedLibraryItems:
            videoTitle = video.title
            videoPath = video.media[0].parts[0].file
            videoFolder = videoPath.rpartition('\\')[0] + "\\"
            videoPoster = video.thumb
            print("Downloading poster for " + videoTitle)
            posterPath = download(baseurl + videoPoster, token, "poster.png", videoFolder)

    if selectedLibraryType == "show" :
        # loop through tv shows and export main show poster
        for video in selectedLibraryItems:
            showTitle = video.title
            showPath = video.locations
            showFolder = showPath[0] + "\\"
            showPoster = video.thumb
            print("Downloading images for " + showTitle)
            posterPath = download(baseurl + showPoster, token, "poster.png", showFolder)
            
            # todo - add loop through season posters and save to season folder.
            for season in video.seasons():
                seasonTitle = season.title
                seasonThumb = season.thumb
                seasonPoster = download(baseurl + seasonThumb, token, seasonTitle + ".png", showFolder)
                
            # now loop through episodes and grab title cards
            for episode in video.episodes() :
                episodeTitle = episode.title
                episodePath = episode.locations[0].rpartition('\\')[0] + "\\"
                episodeFile = episode.locations[0][episode.locations[0].rindex("\\")+1:][:-4]
                episodeThumb = episode.thumb
                episodeThumbPath = download(baseurl + episodeThumb, token, episodeFile + ".png", episodePath)
    print(" ")
        
while (repeat):
    runScript()
    runagain = input("Would you like to run on another library (y/n)?   ")
    if(runagain != "y"):
        repeat = False
else:
    exit()
