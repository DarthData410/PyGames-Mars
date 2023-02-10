from settings import *
from tile import * 

class GameObject(Tile):

    def __init__(self, map_value, pos, groups):
        
        if map_value != NOKEY:
            if not imglib.__contains__(map_value):
                raise LookupError(f'Level map key: {map_value} does not exists in image library. Can not proceed.')

        super().__init__(map_value, pos, groups)