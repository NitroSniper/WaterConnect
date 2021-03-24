import pygame
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
    global BOARD
    with open(f'{fileName}.txt', 'r') as MapData:
        for Row in enumerate(MapData):
            Value = [Tile.rstrip() for Tile in Row[1].split(',')]
            BOARD[Row[0]] = Value


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
TILEIMAGESIZE = 20
WINDOW_SIZE = (500, 500)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60
global NodesImageDict, PathsImageDict, FountainImageDict, BOARD
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



    DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(FPS)



#PreProccesing
loadImagesWithName()
readMapFile()
print (BOARD)
#print (PathsImageDict, NodesImageDict)

#------------------------------------------#
Game()