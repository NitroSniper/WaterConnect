import pygame
from pygame.locals import(
    QUIT,
)



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

#Window
pygame.display.set_caption("Template")
# Set the Caption Window Like 'Terraria: Also Try Minecraft'
DISPLAY = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # True Screen
# Screen to Blit on other Screen
SCREEN = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def Game():
    PROGRAM_RUNNING = True
    while PROGRAM_RUNNING:
        for event in pygame.event.get():
            if event.type == QUIT:
                PROGRAM_RUNNING = False



    DISPLAY.blit(pygame.transform.scale(SCREEN, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(FPS)

Game()