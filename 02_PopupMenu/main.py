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

# Rover Right-click PopupMenu action class:
class RoverMenu(ui.PopupMenuActions):

	def rover_info(self):
		pmi = self.get_active_menuitem()

		ui.MessageBox(
			window=self.window,
			title="Rover Info (Right-Click)",
			message_text=f"Rover located at {pmi.contextof.rect.center}", #NOTE: contextof is right-clicked sprite.
			width=300,
			event_list=pygame.event.get()
		)
	
	def sample_soil(self):
		pmi = self.get_active_menuitem()
		pmi.contextof.samplesoil() #NOTE: contextof is right-clicked sprite. (ie:Player.samplesoil() call works)

	def __init__(self,window,rg):
		self.window = window
		self.rg = rg
		super().__init__()

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('Mars | 02_PopupMenu | Right-click on Rover!')
		self.clock = pygame.time.Clock()

		# Set pyguix ui elements global theme:
		ui.globaltheme("ex_red.json")
		# Rover Details SnapHUD variables:
		self.rover_info = RoverDetailsInfo()
		
		initimages() # Initialize images from settings.py
		self.level = Level() # create instance of Level from level.py
		
		# PopupMenu Variables / Setup:
		RoverMenu(self.screen,self.level.visible_sprites)
		self.pu = None
	
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
			event_list = pygame.event.get()
			for event in event_list:
				
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
					
					# Popup Menu Setup:
					if event.button == pygame.BUTTON_RIGHT:
						ui.PopupMenu.clearall(self.pu)
						# Create new instance of ui.PopupMenu:
						self.pu = ui.PopupMenu(
                        	window=pygame.display.get_surface(),
                        	target_mouse_pos=pygame.mouse.get_pos(),
                        	rg=self.level.visible_sprites
						)

					elif event.button == pygame.BUTTON_LEFT:
						# Respond to left mouse click, if on rover_snap_hud ui element.:
						self.level.rover_snap_hud.clicked()
						
						# NOTE: If PopupMenu instance active then call PopupMenu.clicked() passing in event_list:
						if isinstance(self.pu,ui.PopupMenu): self.pu.clicked(event_list)

			self.level.run()
			self.updatehud() # Update Heads Up Display after game level interactions. (ie: self.level.run())
			
			# NOTE: Check to make sure pu variable is of type ui.PopupMenu, if so then
        	# call .update() for updating when user mouse is 'hovering' over PopupMenu.PopupMenuItem
			if isinstance(self.pu,ui.PopupMenu): self.pu.update()
			
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()