"""Helmet (protection), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83968c0b-0769-4e90-a1c4-33974d290536'
SOURCE_PATH = 'icons-json/protection/helmet_83968c0b-0769-4e90-a1c4-33974d290536.json'
AUTHOR = 'gpt-6'

class Helmet83968c0b(Solo48):
    icon_id = 'helmet-83968c0b'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('helmet', 'protection')

    def build(self):
        self.add_line('sym-e0', (44, 31), (4, 31))
        self.add_line('sym-e3', (4, 31), (4, 35))
        self.add_line('sym-e5', (4, 35), (5, 40))
        self.add_line('sym-e6', (5, 40), (43, 40))
        self.add_line('sym-e8', (43, 40), (44, 35))
        self.add_line('sym-e9', (44, 35), (44, 33))
        self.add_arc('sym-e10-1', (44, 33), (44, 32), radius_x=34, radius_y=34, large_arc=False, sweep=True)
        self.add_line('sym-e10-2', (44, 32), (44, 31))
        self.add_line('sym-e11', (28, 8), (20, 8))
        self.add_line('sym-e12', (20, 8), (19, 11))
        self.add_line('sym-e13', (19, 11), (19, 12))
        self.add_arc('sym-e14', (19, 12), (8, 23), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('sym-e15', (8, 23), (8, 31), radius_x=30, radius_y=30, large_arc=False, sweep=False)
        self.add_line('sym-e16', (19, 22), (19, 12))
        self.add_arc('sym-e17', (29, 12), (40, 23), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e18', (40, 23), (40, 31))
        self.add_line('sym-e19', (29, 22), (29, 11))
        self.add_line('sym-e21', (29, 11), (28, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', closed=True)
        self.add_contour('sym-c1', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=False)
        self.add_contour('sym-c2', 'sym-e16', closed=False)
        self.add_contour('sym-c3', 'sym-e17', 'sym-e18', closed=False)
        self.add_contour('sym-c4', 'sym-e19', 'sym-e21', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
