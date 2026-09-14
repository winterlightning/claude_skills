"""Specialty skin (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5f6a274-d60d-4b27-95f2-f11ba7c9c63e'
SOURCE_PATH = 'icons-json/health/specialty skin_c5f6a274-d60d-4b27-95f2-f11ba7c9c63e.json'
AUTHOR = 'json_to_solo'

class SpecialtySkinHealth(Solo48):
    icon_id = 'specialty-skin-health'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('specialty', 'skin', 'health')

    def build(self):
        self.add_line('sym-e0', (4, 8), (44, 8))
        self.add_arc('sym-e1-1', (24, 17), (27, 18), radius_x=3)
        self.add_arc('sym-e1-2', (27, 18), (34, 25), radius_x=11, sweep=False)
        self.add_arc('sym-e2', (34, 25), (40, 18), radius_x=11, sweep=False)
        self.add_arc('sym-e3', (40, 18), (44, 16), radius_x=5)
        self.add_line('sym-e4', (29, 32), (29, 40))
        self.add_line('sym-e5', (37, 40), (37, 32))
        self.add_arc('sym-e6-1', (24, 17), (21, 18), radius_x=3, sweep=False)
        self.add_arc('sym-e6-2', (21, 18), (14, 25), radius_x=11)
        self.add_arc('sym-e7', (14, 25), (8, 18), radius_x=11)
        self.add_arc('sym-e8', (8, 18), (4, 16), radius_x=5, sweep=False)
        self.add_line('sym-e9', (19, 32), (19, 40))
        self.add_line('sym-e10', (11, 40), (11, 32))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1-1', 'sym-e1-2', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6-1', 'sym-e6-2', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c5', 'sym-e9')
        self.add_contour('sym-c6', 'sym-e10')
        self.relate('connect', 'sym-c1', 'sym-c4')
