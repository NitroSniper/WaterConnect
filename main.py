import pygame
from math import floor
from pathlib import Path
from pygame.locals import(
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

class Tile(object): 
    def __init__(self, FORMAT, position, RGB=(False, False, False), rotationPos=0):
        self.atype = FORMAT.split('_')[1]
        self.parent = FORMAT.split('_')[0]
        self.position = tuple(floor(Tile.TileSizeScalar*x + Tile.TileSizeScalar/2) for x in position)
        self.RGB = RGB
        self.rotationPos = rotationPos
        self.image = pygame.transform.scale(getImage(self.parent, self.atype), (Tile.TileSizeScalar, Tile.TileSizeScalar))
        self.rect = self.image.get_rect(center=self.position)
        print (self.position)
    def Clicked(self):
        self.rotationPos = (self.rotationPos + 1) %4
        # ((this_month - 1) % 12 + 12) % 12


# Function

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
        for yindex, row in enumerate(MapData):
            BOARD[yindex] = [0]*len(row.split(','))
    TILECOUNT = len(BOARD)  # Used to check which dimension is the most
    for i in BOARD.values():
        if len(i) > TILECOUNT:
            TILECOUNT = len(i)
    Tile.TileSizeScalar = floor(min(SCREEN_WIDTH, SCREEN_HEIGHT)/TILECOUNT)
    with open(f'{fileName}.txt', 'r') as MapData:
        for yindex, row in enumerate(MapData):
            Value = [Tile(tile.strip(), (xindex, yindex))  for xindex, tile in enumerate(row.split(','))]
            BOARD[yindex] = Value


def DisplayBoard():
    global BOARD
    for row in BOARD:
        for index, tile in enumerate(BOARD[row]):
            Image = pygame.transform.scale(
                getImage(tile.parent, tile.atype), (Tile.TileSizeScalar, Tile.TileSizeScalar))
            # SCREEN.blit(Image, tuple(TileSize*x for x in tile.position))
            RotationBlit(SCREEN, tile.image, tile.rotationPos*90, tile.position)


def getImage(parent, atype):
    if parent == 'Paths':
        global PathsImageDict
        return PathsImageDict[atype]
    elif parent == 'Nodes':
        global NodesImageDict
        return NodesImageDict[atype]
    else:
        global FountainImageDict
        return FountainImageDict[atype]


def mouseCollision(mousePos):
    global WindowToScreenScalar
    mousePos = tuple(pos*wintoscr for pos, wintoscr in zip(mousePos, WindowToScreenScalar))
    global BOARD
    for row in BOARD.values():
        for tile in row:
            if tile.rect.collidepoint(mousePos):
                tile.Clicked()




# used to simmulate mixing Colors
COLORKEY = {0: (192, 192, 192), 1: (255, 0, 0), 2: (0, 157, 255), 3: (144, 0, 255),
            4: (255, 196, 0), 5: (255, 115, 0), 6: (0, 255, 17), 7: (255, 255, 255)}


def RotationBlit(Surface, Image, Angle, Position, Alpha=255):
    rotatedIMG = pygame.transform.rotate(Image, Angle)
    rotatedIMG.set_alpha(Alpha)
    Surface.blit(rotatedIMG, (int(Position[0] - rotatedIMG.get_width()/2),
                              int(Position[1] - rotatedIMG.get_height()/2)))


def ColorMixer(RGB):
    key = 0
    if RGB[0]:
        key += 1
    if RGB[1]:
        key += 2
    if RGB[2]:
        key += 4
    return COLORKEY[key]


# Globals
global NodesImageDict, PathsImageDict, FountainImageDict, BOARD, TILECOUNT, FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_SIZE, SCREEN, DISPLAY, WindowToScreenScalar
TILEIMAGESIZE = 20
WINDOW_SIZE = (500, 500)
SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 2000
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60
TILECOUNT = 0
NodesImageDict = {}
PathsImageDict = {}
FountainImageDict = {}
BOARD = {}
WindowToScreenScalar = tuple(scr/win for win, scr in zip(WINDOW_SIZE, SCREEN_SIZE))
print (WindowToScreenScalar)

# Window
pygame.display.set_caption("Template")
# Set the Caption Window Like 'Terraria: Also Try Minecraft'
DISPLAY = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # True Screen
# Screen to Blit on other Screen
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


# Game Function

def Game():
    PROGRAM_RUNNING = True
    while PROGRAM_RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                PROGRAM_RUNNING = False
            elif event.type == MOUSEBUTTONDOWN:
                mouseCollision(pygame.mouse.get_pos())
                

        SCREEN.fill((255, 0, 0))
        DisplayBoard()
        DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(FPS)


# PreProccesing
loadImagesWithName()
readMapFile()
print(BOARD)
print(TILECOUNT)
#print (PathsImageDict, NodesImageDict)

#------------------------------------------#
Game()
