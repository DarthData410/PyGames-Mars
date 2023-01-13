# PyGames-Mars
By: J. Brandon George | darth.data410@gmail.com | twitter: @PyFryDay | medium.com: https://darth-data410.medium.com/
license found @: PyGames-Mars/LICENSE (Apache License Version 2.0 Janurary 2004)

# Details:
This open source project contains elements, source code, graphics, sounds, etc. that support my Medium.com (insert link to starting post) series of post about python3 and pygame. 

# Basis for game:
You have landed a rover on Mars and you are to survey the area in which the rover can move in. In surverying the objective is to find all the minerals that exist, and record their cordinates for later phases that will mine said minerals. You need to pay attention to your power, because if it gets critically low before you extend solar panels and recharge you, the rover, dies. Each operation, like moving, sampling, etc. uses up power. Extending the solar panels uses power, hence why you need enough power to extend them to refill your power. Random events will take place, like storm damage, etc. 

Each of the following sections, list specific, self-contained instances of the game. Each has a certain level of development advancemenet, and the next instance builds from the base of the previous. Each section below also has links to the corresponding medium.com post that make sure and reference code, elements, objects, walkthroughs, guides, etc.

# 01_Intro
1. Instance Overview 

    This instance focuses on getting started with creating the initial 'Mars' game. Introduction to concepts like the game loop, the main Game objects, Sprites (Player and Non), obstacles, basic movement, basic game interaction - including highlights and usage of pyguix.ui.elements.MessageBox and pyguix.ui.elements.SnapHUD heads up display elements. (Link to pyguix project on GitHub)

    A detailed walk through for using ui.MessageBox and ui.SnapHUD instances can be found in the Medium.com Links section below, for this game instance. This includes an introduction to hte pyguix python3|pygame library and its corresponding GitHub project repo source.

2. Medium.com Links:

    1. <a href="https://darth-data410.medium.com/how-to-easily-create-pygame-user-interface-and-heads-up-display-elements-3b1bf424a2c8" target="_blank">How-To: Easily Create PyGame User Interface and Heads Up Display Elements</a>
    2. (Link to second post of Medium.com)

# 02_PopupMenu
1. Instance Overview:

    This instance is a clone of 01_Intro, with a focus on the pyguix.ui.elements.PopupMenu usage. Specifically how the 'player.Player'|(module.class) is targeted for contextof, via setup of '02_PopupMenu/pyguix/ui/context/Rover_menu.json'. In the 'Rover_menu.json' file player.Player is listed as the only 'targetclass(es)'. (Note: You can have multiple sprite classes targeted with the contextof the same right-click, PopupMenu.)

    Further within the Rover_menu.json you find the actionclass = _ _ main _ _.RoverMenu|(module.class), which houses the menuitem.(menu item instance).popupmenuitem.action, which is a bound function on the actionclass, RoverMenu. The parts listed then, expect to be able to call the RoverMenu. _action_ bound function, via reflection concepts of python3, and have the logic contained within that _Actionclass_._action_|(class.bound function) execute, with the ability to reference the calling, 'active', pyguix.ui.elements.PopupMenuItem instance. This PopupMenuItem instance contains a .contextof variable which represents that sprite class instance that the right click action of the mouse took place on. 

    All related python3 code examples for the PopupMenu for the 02_PopupMenu game instance, can be found in 02_PopupMenu/main.py python file. The following is a list for quick reference: (note: developed in vscode, therefore code line numbers referenced are generated by vscode ide.)

    1. class RoverMenu(ui.PopupMenuActions) - Lines 20-41
    2. RoverMenu(...) (instance creation) - Line 61
    3. self.pu (Game.pu - game instance variable for PopupMenu) - Line 62
    4. if event.button == pygame.BUTTON_RIGHT: (Operate upon Right-Click mouse) - Line 108
    5. ui.PopupMenu.clearall(self.pu) - Line 109
    6. self.pu = ui.PopupMenu(...) - Lines 111-115
    7. elif event.button == pygame.BUTTON_LEFT: (Operate upon Left-Click mouse) - Line 117
    8. if isinstance(self.pu,ui.PopupMenu): self.pu.clicked(event_list) - Line 122
    9. if isinstance(self.pu,ui.PopupMenu): self.pu.update() - Line 129 

2. Medium.com Links:

    1. __(TBD)__

# External Attributions
The group behind the pygame library itself (pygame.org) can not be thanked enough for the continued effort in keeping the pygame library fresh, useful and relevant. Further the coding style, naming of classes and python (.py) files adhere (loosely) to standards set forth in examples provided by pygame.org site. Specifically in the Zelda Python (link) was used to he help jump start this work. Finally the graphics found in this game, are in part, cloned / jump started from Pixel-boy. (https://pixel-boy.itch.io/ninja-adventure-asset-pack)

Both the mentioned Zelda Python and Pixel-boy|ninja-adventure-asset-pack are released under the Creative Commons Zero (CC0) license. (Attributions paid forward, thanks!)