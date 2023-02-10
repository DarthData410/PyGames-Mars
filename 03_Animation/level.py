import pygame 
import pyguix.ui.elements as ui
from settings import *
from gameobject import *
from player import Player
from enemy import Enemy

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = pygame.sprite.Group()
		self.obstacle_sprites = pygame.sprite.Group()

		# create background:
		self.background_surf = pygame.image.load(imglib[BGKEY]).convert()
		self.background_rect = self.background_surf.get_rect(topleft = (0,0))

		# enemies array:
		self.enemies=list()

		# sprite setup
		self.create_map()

		# Create UI Elements:
		# 01 - SnapHUD for Mars Rover Details:
		self.rover_snap_hud = ui.SnapHUD(
			window=self.display_surface,
			context='SnapHUD_default.json',
			rg=self.visible_sprites
		)
		
	def create_map(self):
		for row_index,row in enumerate(MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE

				if col != NOKEY:
					
					if col == PLAYER_KEY:
						self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
				
					# NOTE Enemy map entry check:
					elif col == ALIEN_GREEN_KEY or col == ALIEN_BLUE_KEY or col == ALIEN_RED_KEY or col == ALIEN_YELLOW_KEY:
						alien = None
						if col == ALIEN_GREEN_KEY:
							alien = ALIENGREEN
						elif col == ALIEN_BLUE_KEY:
							alien = ALIENBLUE
						elif col == ALIEN_RED_KEY:
							alien = ALIENRED
						elif col == ALIEN_YELLOW_KEY:
							alien = ALIENYELLOW
					
						if alien != None:
							e = Enemy((x,y),[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites,alien)
							self.enemies.append(e)
					
					else: 
						GameObject(col,(x,y),[self.visible_sprites,self.obstacle_sprites])
		
	def run(self):
		
		# update and draw the game
		self.display_surface.blit(self.background_surf,self.background_rect)
		self.visible_sprites.draw(self.display_surface)
		self.visible_sprites.update()

		
