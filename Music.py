"""
Module to make manipulating music easier.

Include these lines of code in the main program:
    
    import Music
    add_library("minim")
    minim = Minim(this)
    Player = Music.Player(minim)
    
You should also probably make Player and minim global.

Then to call a function within the module:
    Music.Player.<function>(<arguments>)
"""


add_library("minim")

# Class for playing music, to make self-communication within Music module easier.
class Player(object):
    def __init__(self, minim):
        self.minim = minim
        self.currentSong = None
    # Function referenced by other functions within Player to return the song chosen in main code.
    def getSong(self, masterList, songSet, songName):
        for find_song_set in masterList:
            if find_song_set == songSet:
                for song in songSet:
                    if song == songName:
                        return songName
                    
    # Plays a song specified by master list, sublist, and file name.
    def playSong(self, minim, masterList, songSet, songName):
        song = self.getSong(masterList, songSet, songName)
        self.theme = minim.loadFile(song, 1024)
        self.theme.loop()
    
    # Stops playing any current music.
    def quitPlayer(self):
        self.theme.pause()
        self.theme.rewind()
        
    #Fades out current playing song, then fades in the next one.
    def switchSong(self, minim, masterList, songSet, newSong):
        song = self.getSong(masterList, songSet, newSong)

#       Fades out currently playing song
        self.theme.shiftGain(self.theme.getGain(), -30, 3000)
        if self.theme.getGain() == -30:
            self.theme.pause
        self.theme = False
        
#       Begins new song
        self.theme = minim.loadFile(song)
        self.theme.loop()
