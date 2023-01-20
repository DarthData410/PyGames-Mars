import pygame
import spritesheet as ss
from settings import *

class Enemy(pygame.sprite.Sprite):
	
    def __init__(self,pos,groups,obstacle_sprites,enemy_type):
        super().__init__(groups)
        
        self.obstacle_sprites=obstacle_sprites

        # Enemy Animation & SpriteSheet
        # NOTE: builds out from settings.GRAPHICS + settings.ENEMIES constant folder|string values
        # Further passing in enemy_type, assumes that naming convention employed for naming JSON(ie: EXT)
        # files. For example, resolves to: 
        # GRAPHICS+ENEMIES+enemy_type+EXT
        # -
        # GRAPHICS='./graphics'
        # ENEMIES='/enemies/'
        # enemy_type='alientblob_blue'
        # EXT='.json'
        # -
        # './graphics/enemies/alienblob_blue.json'
        # -
        # For loading SpriteSheet()
        
        self.sprite_sheet = ss.SpriteSheet(loc=GRAPHICS+ENEMIES,file=enemy_type+EXT)
        self.enemy_type = enemy_type
        self.animation_images = self.sprite_sheet.sprites()
        
        self.frame_index = 0
        self.animation_speed = self.sprite_sheet.animation_speed()
        self.animation_framelen = 0

        self.image = self.animation_images[DOWN][0]
        self.rect = self.image.get_rect(topleft = pos)
        self.status = DOWN

        self.vector = pygame.math.Vector2(self.rect.x,self.rect.y)
    
    def animate(self): 
        animation = self.animation_images[self.status] 
        self.animation_framelen = len(animation)

		# loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        animation = animation[int(self.frame_index)]
        # set the image
        self.image = animation
    
    def update(self):
        self.animate()
		
        
		

