"""Camping tent (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6abce5ce-492a-5630-a30e-c47fb4045166'
SOURCE_PATH = 'icons-json/outdoors/camping tent_6abce5ce-492a-5630-a30e-c47fb4045166.json'
AUTHOR = 'json_to_solo'

class CampingTent6abce5ce(Solo48):
    icon_id = 'camping-tent-6abce5ce'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('camping', 'tent', 'outdoors')

    def build(self):
        self.add_line('sym-e0', (14, 40), (14, 35))
        self.add_line('sym-e1', (14, 35), (15, 31))
        self.add_arc('sym-e2', (15, 31), (21, 20), radius_x=18)
        self.add_arc('sym-e3', (21, 20), (24, 19), radius_x=5)
        self.add_arc('sym-e4', (24, 19), (27, 20), radius_x=5)
        self.add_arc('sym-e5', (27, 20), (33, 31), radius_x=18)
        self.add_arc('sym-e6', (33, 31), (34, 35), radius_x=15, sweep=False)
        self.add_line('sym-e7', (34, 35), (34, 40))
        self.add_line('sym-e8', (34, 40), (44, 40))
        self.add_line('sym-e9', (44, 40), (41, 28))
        self.add_arc('sym-e10', (41, 28), (24, 8), radius_x=25, sweep=False)
        self.add_arc('sym-e11', (24, 8), (7, 28), radius_x=25, sweep=False)
        self.add_line('sym-e12', (7, 28), (4, 40))
        self.add_line('sym-e13', (4, 40), (14, 40))
        self.add_line('sym-e14', (14, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (34, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
