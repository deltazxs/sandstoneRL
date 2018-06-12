add_library('minim')

# class to play sound effects, heavily borrows from the music player class
class SFXPlay(object):
    def __init__(self, minim):
        self.minim = minim
        self.currentSound = None
        
    # function used by other functions to find a specified sound
    def getSound(self, minim, masterList, soundSet, soundName):
        for subSet in masterList:              # locate the specified subset of sounds
            if subSet == soundSet:             # once that's found
                for sound in soundSet:         # locate the specified sound within that subset
                    if sound == soundName:     # once that's found
                        return soundName       # return the sound

    # plays a sound when called
    def playSound(self, minim, masterList, soundSet, soundName):
        sound = self.getSound(masterList, soundSet, soundName)  #calls getSound to get the called sound
        self.sfx = minim.loadFile(sound, 1024)                  #plays it
        
    #stops sound effects (hopefully without interfering with music hehe)
    def stopSound(self, minim):
        self.theme.pause()