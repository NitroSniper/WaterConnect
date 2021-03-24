import pygame
from math import floor
from pathlib import Path
from pygame.locals import(
    QUIT,
)

#Function

def loadImagesWithName():
    global NodesImageDict, PathsImageDict
    NodesImageDict = {}
    PathsImageDict = {}
    Folders = ('Nodes', 'Paths', 'Fountains')
    for Folder in Folders:
        paths = Path(f'Images\{Folder}').glob('**/*.png')
        for path in paths:
            path = str(path)
            Image = pygame.image.load(path).convert_alpha()
            #Image = pygame.image.load(path)
            if Folder == ('Nodes'):
                NodesImageDict[path.split('\\')[-1].split('.')[0]] = Image
            elif Folder == ('Fountains'):
                FountainImageDict[path.split('\\')[-1].split('.')[0]] = Image
            else: 
                PathsImageDict[path.split('\\')[-1].split('.')[0]] = Image



def readMapFile(fileName='map'):
    global BOARD, TILECOUNT
    with open(f'{fileName}.txt', 'r') as MapData:
        for row in enumerate(MapData):
            Value = [Tile.rstrip() for Tile in row[1].split(',')]
            BOARD[row[0]] = Value
    TILECOUNT = len(BOARD) #Used to check which dimesion is the most
    for i in BOARD.values():
        if len(i) > TILECOUNT: TILECOUNT = len(i)




def DisplayBoard():
    global BOARD, TILECOUNT
    TileSize = floor(min(SCREEN_WIDTH, SCREEN_HEIGHT)/TILECOUNT)
    for row in BOARD:
        for item in enumerate(BOARD[row]):
            Image =pygame.transform.scale(getImage(item[1]), (TileSize, TileSize))
            SCREEN.blit(Image, (item[0]*TileSize, row*TileSize))


def getImage(TileName):
    TileName = [tile.lstrip() for tile in TileName.split('_')]
    if TileName[0] == 'Paths':
        global PathsImageDict
        return PathsImageDict[TileName[1]]
    elif TileName[0] == 'Nodes':
        global NodesImageDict
        return NodesImageDict[TileName[1]]
    else:
        global FountainImageDict
        return FountainImageDict[TileName[1]]

# used to simmulate mixing Colors 
COLORKEY = {0: (192,192,192), 1: (255, 0, 0), 2: (0, 157, 255), 3: (144, 0, 255), 
            4: (255, 196, 0), 5: (255, 115, 0), 6: (0, 255, 17), 7: (255, 255, 255)}
def ColorMixer(RGB):
    key = 0
    if RGB[0]: key += 1
    if RGB[1]: key += 2
    if RGB[2]: key += 4
    return COLORKEY[key]


#Globals
global NodesImageDict, PathsImageDict, FountainImageDict, BOARD, TILECOUNT, FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_SIZE, SCREEN, DISPLAY
TILEIMAGESIZE = 20
WINDOW_SIZE = (500, 500)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60
TILECOUNT = 0
NodesImageDict = {}
PathsImageDict = {}
FountainImageDict = {}
BOARD = {}



#Window
pygame.display.set_caption("Template")
# Set the Caption Window Like 'Terraria: Also Try Minecraft'
DISPLAY = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # True Screen
# Screen to Blit on other Screen
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()



#Game Function

def Game():
    PROGRAM_RUNNING = True
    while PROGRAM_RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                PROGRAM_RUNNING = False

        SCREEN.fill((255, 0, 0))
        DisplayBoard()
        DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(FPS)



#PreProccesing
loadImagesWithName()
readMapFile()
print (BOARD)
print (TILECOUNT)
#print (PathsImageDict, NodesImageDict)

#------------------------------------------#
Game()