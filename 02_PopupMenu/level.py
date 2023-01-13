import pygame 
import pyguix.ui.elements as ui
from settings import *
from tile import Tile
from gameobject import *
from player import Player

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

				if col == PLAYER_KEY:
					self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
				elif col != NOKEY:
					GameObject(col,(x,y),[self.visible_sprites,self.obstacle_sprites])
		
	def run(self):
		
		# update and draw the game
		self.display_surface.blit(self.background_surf,self.background_rect)
		self.visible_sprites.draw(self.display_surface)
		self.visible_sprites.update()

		
