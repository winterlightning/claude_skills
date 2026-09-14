"""Plant (nature), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b473017-90a0-4c45-ac0d-3352cf57b3e6'
SOURCE_PATH = 'icons-json/nature/plant_5b473017-90a0-4c45-ac0d-3352cf57b3e6.json'
AUTHOR = 'json_to_solo'

class PlantNature(Solo48):
    icon_id = 'plant-nature'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('plant', 'nature')

    def build(self):
        self.add_line('sym-e0', (24, 42), (24, 36))
        self.add_arc('sym-e1', (24, 36), (7, 25), radius_x=18)
        self.add_arc('sym-e2', (7, 25), (6, 20), radius_x=14)
        self.add_arc('sym-e4', (6, 20), (15, 23), radius_x=20)
        self.add_arc('sym-e5', (15, 23), (19, 26), radius_x=31)
        self.add_arc('sym-e6', (19, 26), (21, 10), radius_x=18)
        self.add_arc('sym-e7', (21, 10), (23, 7), radius_x=20)
        self.add_line('sym-e8', (23, 7), (24, 6))
        self.add_arc('sym-e9', (24, 6), (25, 7), radius_x=19, sweep=False)
        self.add_arc('sym-e10', (25, 7), (27, 10), radius_x=20, sweep=False)
        self.add_arc('sym-e11', (27, 10), (29, 26), radius_x=18)
        self.add_arc('sym-e12', (29, 26), (33, 23), radius_x=31)
        self.add_arc('sym-e13', (33, 23), (42, 20), radius_x=19)
        self.add_line('sym-e15', (42, 20), (41, 25))
        self.add_arc('sym-e16', (41, 25), (24, 36), radius_x=18)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16')
