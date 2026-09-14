"""Psychiatry (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0d4e8d8-2e3e-47b4-82f6-85f8457f25af'
SOURCE_PATH = 'icons-json/health/psychiatry_f0d4e8d8-2e3e-47b4-82f6-85f8457f25af.json'
AUTHOR = 'json_to_solo'

class Psychiatry(Solo48):
    icon_id = 'psychiatry'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('psychiatry', 'health')

    def build(self):
        self.add_line('sym-e0', (20, 8), (24, 8))
        self.add_line('sym-e1', (24, 8), (28, 8))
        self.add_line('sym-e2', (24, 40), (24, 25))
        self.add_line('sym-e3', (24, 25), (24, 8))
        self.add_line('sym-e4', (28, 40), (24, 40))
        self.add_line('sym-e5', (24, 40), (20, 40))
        self.add_line('sym-e6', (44, 8), (42, 8))
        self.add_arc('sym-e7', (42, 8), (38, 11), radius_x=5, sweep=False)
        self.add_line('sym-e8', (38, 11), (38, 17))
        self.add_arc('sym-e9', (38, 17), (36, 21), radius_x=7)
        self.add_arc('sym-e10', (36, 21), (24, 25), radius_x=12)
        self.add_arc('sym-e11', (24, 25), (12, 21), radius_x=12)
        self.add_arc('sym-e12', (12, 21), (10, 17), radius_x=7)
        self.add_line('sym-e13', (10, 17), (10, 11))
        self.add_arc('sym-e14', (10, 11), (6, 8), radius_x=5, sweep=False)
        self.add_arc('sym-e15', (6, 8), (4, 8), radius_x=6)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
