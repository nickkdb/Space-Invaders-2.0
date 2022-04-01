import pygame 
from os import path

main_dir = path.split(path.abspath(__file__))[0] #Folder Path
SCREENRECT = pygame.Rect(0,0,800,600) #set up a rectangle for the screen to reference later

#creating my own handler for importing images
def load_img(file):
    file = path.join(main_dir, "assets", file)
    try:
        display = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Failed to load image...')
    return display.convert_alpha()