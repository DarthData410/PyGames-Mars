import enum

# Game Constants:
WIDTH=1280	
HEIGHT=768
FPS=30
TILESIZE=32

# In Game Constants:
INIT_LASTSAMPLE='n/a'
COL_HORIZ='HorizontalCollide'
COL_VERT='VerticalCollide'
NONE='NONE'
MINE_CHOICES=[NONE,'Zinc',NONE,'Gold',NONE,'Silver']


#Game Images / Image Library(dict()):
NOKEY='-1'
BACKGROUND='./graphics/backgrounds/background.png'
BGKEY='[&BACK]'
BLANK='./graphics/backgrounds/blocked_blank32.png'
BLANK_KEY='x'

PLAYER_KEY=100
ROCK='./graphics/objects/rock_one_64_a.png'
ROCK_KEY=200
BOULDER='./graphics/objects/boulder_32.png'
BOULDER_KEY=300
ALIEN_GREEN_KEY=400
ALIEN_BLUE_KEY=500
ALIEN_RED_KEY=600
ALIEN_YELLOW_KEY=700

# Animation Constants:
EXT='.json'
GRAPHICS='./graphics'
PLAYER='/player/'
ENEMIES='/enemies/'
ALIENRED='alienblob_red'
ALIENBLUE='alienblob_blue'
ALIENGREEN='alienblob_green'
ALIENYELLOW='alienblob_yellow'
PLAYERMAP='rover'+EXT

DOWN='down'
LEFT='left'
RIGHT='right'
UP='up'
IDLE='_idle'

# Game Enums
NavDirection = enum.Enum('Direction','North South East West NONE')

# Image Library / Init unbound function:
imglib=dict()
def initimages():
    imglib[ROCK_KEY]=ROCK
    imglib[BOULDER_KEY]=BOULDER
    imglib[BLANK_KEY]=BLANK
    imglib[BGKEY]=BACKGROUND

    
# Game World Map Array:
MAP=[
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','-1','-1','-1',BOULDER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x','x','x','x','x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x','x','x','x',BOULDER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1',BOULDER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x','x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',BOULDER_KEY,'-1','x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1',BOULDER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x','-1',BOULDER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',ALIEN_BLUE_KEY,'-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',PLAYER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1',ROCK_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1',ROCK_KEY,'-1','-1','-1',ALIEN_GREEN_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',BOULDER_KEY,'-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1',ROCK_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',BOULDER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',ROCK_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',BOULDER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',BOULDER_KEY,'-1',BOULDER_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',ROCK_KEY,'-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1',ROCK_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',ALIEN_RED_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1',ALIEN_YELLOW_KEY,'-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1',BOULDER_KEY,'x'],
['x','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','-1','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]
