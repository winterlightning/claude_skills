"""Cauldron (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e709f0a8-cd5c-4a9b-8b47-1734cea8a46a'
SOURCE_PATH = 'icons-json/holidays/cauldron_e709f0a8-cd5c-4a9b-8b47-1734cea8a46a.json'
AUTHOR = 'json_to_solo'

class Cauldron(Solo48):
    icon_id = 'cauldron'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('cauldron', 'holidays')

    def build(self):
        self.add_line('sym-e0', (7, 8), (24, 8))
        self.add_line('sym-e1', (24, 8), (41, 8))
        self.add_arc('sym-e3', (41, 8), (44, 11), radius_x=3)
        self.add_arc('sym-e6', (44, 11), (42, 14), radius_x=4)
        self.add_line('sym-e7', (42, 14), (41, 14))
        self.add_arc('sym-e8', (41, 14), (40, 15), radius_x=43)
        self.add_arc('sym-e9', (40, 15), (42, 17), radius_x=27, sweep=False)
        self.add_line('sym-e10', (42, 17), (44, 22))
        self.add_line('sym-e11-1', (44, 22), (41, 33))
        self.add_arc('sym-e11-2', (41, 33), (34, 39), radius_x=15)
        self.add_line('sym-e12', (34, 39), (29, 40))
        self.add_line('sym-e14', (29, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (19, 40))
        self.add_line('sym-e17', (19, 40), (14, 39))
        self.add_arc('sym-e18-1', (14, 39), (7, 33), radius_x=15)
        self.add_line('sym-e18-2', (7, 33), (4, 22))
        self.add_arc('sym-e19', (4, 22), (6, 17), radius_x=16)
        self.add_arc('sym-e20', (6, 17), (8, 15), radius_x=27)
        self.add_arc('sym-e21', (8, 15), (7, 14), radius_x=43, sweep=False)
        self.add_line('sym-e22', (7, 14), (6, 14))
        self.add_arc('sym-e23', (6, 14), (4, 11), radius_x=4)
        self.add_arc('sym-e26', (4, 11), (7, 8), radius_x=3)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11-1', 'sym-e11-2', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18-1', 'sym-e18-2', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e26', closed=True)
