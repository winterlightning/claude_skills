"""Batch-04/beanie (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e562e3f9-df4c-5aa5-883f-3833004c6400'
SOURCE_PATH = 'icons-json/accessories/batch-04/beanie_e562e3f9-df4c-5aa5-883f-3833004c6400.json'
AUTHOR = 'json_to_solo'

class Batch04Beanie(Solo48):
    icon_id = 'batch-04-beanie'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'beanie', 'accessories')

    def build(self):
        self.add_line('sym-e0', (8, 29), (8, 22))
        self.add_arc('sym-e1', (8, 22), (23, 8), radius_x=16)
        self.add_line('sym-e2', (23, 8), (24, 8))
        self.add_arc('sym-e5', (24, 8), (25, 8), radius_x=43, sweep=False)
        self.add_arc('sym-e6', (25, 8), (40, 22), radius_x=16)
        self.add_line('sym-e7', (40, 22), (40, 29))
        self.add_line('sym-e8', (40, 29), (41, 29))
        self.add_arc('sym-e9', (41, 29), (44, 32), radius_x=3)
        self.add_line('sym-e11', (44, 32), (44, 37))
        self.add_arc('sym-e12', (44, 37), (41, 40), radius_x=3)
        self.add_line('sym-e13', (41, 40), (40, 40))
        self.add_line('sym-e14', (40, 40), (24, 40))
        self.add_line('sym-e15', (24, 40), (8, 40))
        self.add_arc('sym-e16', (8, 40), (7, 40), radius_x=1, sweep=False)
        self.add_arc('sym-e17', (7, 40), (4, 37), radius_x=3)
        self.add_line('sym-e18', (4, 37), (4, 32))
        self.add_arc('sym-e20', (4, 32), (7, 29), radius_x=3)
        self.add_line('sym-e21', (7, 29), (8, 29))
        self.add_line('sym-e22', (8, 29), (24, 29))
        self.add_line('sym-e23', (24, 29), (40, 29))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
