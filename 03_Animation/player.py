import pygame,random
import pyguix.ui.elements as ui
import spritesheet as ss
from settings import *

class Player(pygame.sprite.Sprite):
	
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)

		# Player Animtations & Animation Frames:
		self.sprite_sheet = ss.SpriteSheet(loc=GRAPHICS+PLAYER,file=PLAYERMAP)
		self.animation_images = self.sprite_sheet.sprites()
		
		self.frame_index = 0
		self.animation_speed = self.sprite_sheet.animation_speed() 
		
		self.image = self.animation_images[DOWN+IDLE][0]
		self.rect = self.image.get_rect(topleft = pos)
		self.direction = pygame.math.Vector2(self.rect.x,self.rect.y)
		self.speed = 2

		self.obstacle_sprites = obstacle_sprites
		self.last_sample = INIT_LASTSAMPLE
		self.nav_direction = NavDirection.South
		self.status = DOWN
		self.lifebar = 100

		# Minerals Found dict:
		self.mine_cords=dict()

	def add2mine_cords(self,pos) -> bool:
		ret = False
		if not self.mine_cords.__contains__(pos):
			m = random.choice(MINE_CHOICES)
			if m != NONE:
				self.mine_cords[pos]=m
				ret = True
		return ret

	def samplesoil(self):
		# NOTE: Use MessageBox to interact with player to confirm action:
			msgbox = ui.MessageBox(
				window=pygame.display.get_surface(),
				message_text=('Take a sample at %s ?' % str(self.rect.center)),
				title="Soil Sample",
				buttons=('Yes','No'),
				event_list=pygame.event.get()
			)

			if msgbox.clicked() == "Yes":
				print(f'taking sample at {self.last_sample}....')
				self.last_sample = self.rect.center
				if(self.add2mine_cords(self.last_sample)):
					print(f'Mineral {self.mine_cords[self.last_sample]} found!')
				else:
					print('... nothing found ...')
			else:
				print("... no sample taken.")

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
			self.nav_direction = NavDirection.North
			self.status = UP
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
			self.nav_direction = NavDirection.South
			self.status = DOWN
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
			self.nav_direction = NavDirection.East
			self.status = RIGHT
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.nav_direction = NavDirection.West
			self.status = LEFT
		else:
			self.direction.x = 0

		if keys[pygame.K_s]: # Take Soil Sample:
			self.samplesoil()

	def get_status(self):
		
		if IDLE in self.status:
			self.status = self.status.replace(IDLE,'') 

		if self.direction.x == 0 and self.direction.y == 0:
			if not IDLE in self.status:
				self.status = self.status + IDLE
		else:
			self.status.rstrip(IDLE)

	
	def move(self,speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.rect.x += self.direction.x * speed
		self.collision(COL_HORIZ)
		self.rect.y += self.direction.y * speed
		self.collision(COL_VERT)

	def collision(self,direction):
		if direction == COL_HORIZ:
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.x > 0: # moving right
						self.rect.right = sprite.rect.left
					if self.direction.x < 0: # moving left
						self.rect.left = sprite.rect.right

		if direction == COL_VERT:
			for sprite in self.obstacle_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.y > 0: # moving down
						self.rect.bottom = sprite.rect.top
					if self.direction.y < 0: # moving up
						self.rect.top = sprite.rect.bottom

	def animate(self):
		animation = self.animation_images[self.status] 

		# loop over the frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		animation = animation[int(self.frame_index)]
		# set the image
		self.image = animation
		
	def update(self):
		self.input()
		self.get_status()
		self.animate()	
		self.move(self.speed)
	