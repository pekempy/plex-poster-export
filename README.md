# Plex Poster Export
## Export your plex posters, and episode title cards to file
---
### Requirements:
- Python
- plexapi (`pip install plexapi`)
---

### Setup:
If you don't provide your Plex URL and Plex token on line 2/3, the script will prompt you for them.   
On running the script, it will prompt you which library you want to run the script on.

#### Movies
- The poster will be exported to the same directory as the media file with the name `poster.png`

#### TV Series
- The show poster will be exported to the parent directory of the show with the name `poster.png`
- The season covers will be exported to the parent directory of the show with the name `Season x.png`
- The episode title cards will be exported next to each file with the name matching the video file.

At the end of the script, you can instantly run it again on another library by entering `y` (case sensitive)


I know it's not the most elegant code but it's functional :)
