
class Tile:#A class to hold information about every tile
    def __init__(self, x, y, gfx, solid, pathable, explored, visible, used):
        self.x = x
        self.y = y
        self.gfx = gfx
        self.solid = solid
        self.pathable = pathable
        self.explored = explored
        self.visible = visible    
        self.used = used
    
class room:#A class to help define the room
    def __init__(self, minR, maxR, maxW, maxH):
        self.safe = False
        while self.safe == False:
            print("Looping")
            self.x = int(random(1, maxW-1))
            self.y = int(random(1, maxH-1))
            self.w = self.x + int(random(minR, maxR))
            self.h = self.y + int(random(minR, maxR))
            if self.w > maxW-1 or self.h > maxH-1:
                print("Out of bounds")
            else:
                self.safe = True
    
class Floor:
    def __init__(self, maxW, maxH, level, tileSet, roomNum):
        self.maxW = maxW
        self.maxH = maxH
        self.rooms = []
        self.level = level
        self.tileSet = tileSet
        self.usedTiles = []
        self.roomNum = roomNum
        #### grid init
        self.grid = [[Tile(x, y, self.tileSet[1], True, False, False, False, False) for y in range(0, self.maxH)] for x in range(0, self.maxW)]#Builds a 2d list of list aka a matrix/grid
        self.num = 0
        #### Map gen logic
        while len(self.rooms) < self.roomNum:#While we dont have the desired number of rooms
            self.safe = False
            self.b = False
            print("before")
            self.temp = room(5, 8, self.maxW, self.maxH)
            print("after")
            for x in range(self.temp.x, self.temp.w):
                for y in range(self.temp.y, self.temp.h):
                    if self.grid[x][y].used == True:
                        print("Overlap")
                        self.b = True
                        break
                    else:
                        self.safe = True
                if self.b == True: break
                
            if self.b == False and self.safe == True:
                self.rooms.append(self.temp)
                for x in range(self.temp.x, self.temp.w):#Draws room
                    for y in range(self.temp.y, self.temp.h):
                        self.grid[x][y].gfx = self.tileSet[0]
                        self.grid[x][y].used = True
                        self.grid[x][y].solid = False
                        self.grid[x][y].pathable = True
                
                for x in range(self.temp.x-1, self.temp.w+1):
                    for y in range(self.temp.y-1, self.temp.h+1):
                        if self.grid[x][y].used == True:
                            print("Don't Overwite")
                        else:
                            self.grid[x][y].used = True
                            self.grid[x][y].gfx = self.tileSet[2]
                        
    def MakeHalls(self):#WHOOOO FINALLY
        pass
                        
    def Render(self):#Seperat class method, used to render this specific instance of floor
        for x in range(0, self.maxW):
            for y in range(0, self.maxH):#add logic for FOV
                image(self.grid[x][y].gfx, x*16, y*16, 16, 16)
