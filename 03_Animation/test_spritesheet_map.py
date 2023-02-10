# NOTE:
# This is a quick load of passed in sprite sheets, via JSON SpriteSheetMap file.
# A matching (sprite sheet).json file is expected to exists that matches the schema for
# the spritesheet.SpriteSheet class, found in the spritesheet.py file. 

import pygame
import spritesheet as ss

#NOTE: Quick example test:
#LOC='./graphics/enemies/'
LOC='./graphics/player/'
#FILE='alienblob_yellow.json'
FILE='rover.json'


# pygame init:
pygame.init()
window = pygame.display.set_mode((1200,800))
display = pygame.display.set_caption('Mars | 03_Animation')
clock = pygame.time.Clock()
clock.tick(30)

all = pygame.sprite.Group()

# NOTE: Create instance of SpriteSheet, loading for Rover Example, using the 'SpriteSheetMap'
# JSON schema provided in this example.:
sso = ss.SpriteSheet(LOC,FILE)

pos = (0,0)
x = 0
y = 0
for k in sso.sprites():
    l = sso.sprites()[k]
    for i in l:
        s = pygame.sprite.Sprite(all)
        s.image = i
        s.rect = s.image.get_rect(topleft=pos)
        x += sso.dimensions()[0]
        pos = (x,y)
    y += sso.dimensions()[1]
    x = 0
    pos = (x,y)

run = True

while run:

    all.draw(window)
    pygame.display.update()

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

pygame.quit()            


