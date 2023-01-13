import pygame, sys
import pyguix.ui.elements as ui
from settings import *
from level import Level

# Rover Details pyguix.ui.elements.SnapHUDPartInfo class:
class RoverDetailsInfo(ui.SnapHUDPartInfo):

	def center_pos(self,v=None):
		return self.partinfo("center_pos",v)
	def rover_direction(self,v=None):	
		return self.partinfo("rover_direction",v)
	def last_sample(self,v=None,md=None):
		self.partinfo("mineral_detected",md)
		return self.partinfo("last_sample",v)
	def mineral_detected(self):
		# NOTE: lookup call only, set with sample code above.
		return self.partinfo("mineral_detected")

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('Mars | 01_Intro')
		self.clock = pygame.time.Clock()

		# Set pyguix ui elements global theme:
		ui.globaltheme("ex_red.json")
		# Rover Details SnapHUD variables:
		self.rover_info = RoverDetailsInfo()
		
		initimages() # Initialize images from settings.py
		self.level = Level() # create instance of Level from level.py
	
	def game_quit(self) -> bool:
		""" check to see if user wants to quit game, if so then quit, otherwise continue on """
		
		msgbox = ui.MessageBox(
			window = self.level.display_surface,
			message_text="Would you like to quit the game?",
			title="Quit?",
			buttons=("Yes","No"),
			width=300,
			event_list=pygame.event.get()
		)

		ret = False if msgbox.canceled() or msgbox.clicked() == "No" else True
		return ret
	
	def updatehud(self):
		""" update SnapHUD Rover Details parts """
		self.rover_info.center_pos(str(self.level.player.rect.center))
		self.rover_info.rover_direction(str(self.level.player.nav_direction.name))
		# NOTE: Check to see if last sample produced a valid mineral found in sample taken:
		if self.level.player.mine_cords.__contains__(self.level.player.last_sample):
			m = self.level.player.mine_cords[self.level.player.last_sample]
		else:
			m = None
		self.rover_info.last_sample(str(self.level.player.last_sample),m)

	def run(self):
		while True:
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					if self.game_quit():
						pygame.quit()
						sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
						if self.game_quit():
							pygame.quit()
							sys.exit()
				
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == pygame.BUTTON_LEFT:
						# Respond to left mouse click, if on rover_snap_hud ui element.:
						self.level.rover_snap_hud.clicked()

			self.level.run()
			self.updatehud() # Update Heads Up Display after game level interactions. (ie: self.level.run())
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()