"""Batch-05/hat winter (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc66d74c-cb01-4d93-a56d-1c086f98ec0d'
SOURCE_PATH = 'icons-json/accessories/batch-05/hat winter_bc66d74c-cb01-4d93-a56d-1c086f98ec0d.json'
AUTHOR = 'json_to_solo'

class Batch05HatWinter(Solo48):
    icon_id = 'batch-05-hat-winter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'winter', 'accessories')

    def build(self):
        self.add_line('sym-e0', (8, 28), (40, 28))
        self.add_line('sym-e1', (40, 28), (44, 29))
        self.add_line('sym-e2', (44, 29), (44, 30))
        self.add_line('sym-e3', (44, 30), (44, 37))
        self.add_arc('sym-e5', (44, 37), (41, 40), radius_x=4)
        self.add_line('sym-e7', (41, 40), (24, 40))
        self.add_line('sym-e8', (24, 40), (7, 40))
        self.add_arc('sym-e10', (7, 40), (4, 37), radius_x=4)
        self.add_line('sym-e12', (4, 37), (4, 30))
        self.add_line('sym-e13', (4, 30), (4, 29))
        self.add_line('sym-e14', (4, 29), (8, 28))
        self.add_arc('sym-e15', (8, 28), (8, 19), radius_x=29)
        self.add_arc('sym-e16', (8, 19), (23, 8), radius_x=16)
        self.add_arc('sym-e18', (23, 8), (24, 8), radius_x=39, sweep=False)
        self.add_arc('sym-e19', (24, 8), (25, 8), radius_x=40, sweep=False)
        self.add_arc('sym-e21', (25, 8), (40, 19), radius_x=16)
        self.add_line('sym-e22', (40, 19), (40, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e21', 'sym-e22')
