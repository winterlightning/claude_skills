"""Dresser wardrobe (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '809a0b50-e20c-42cc-aecb-521651974674'
SOURCE_PATH = 'icons-json/furnitures/dresser wardrobe_809a0b50-e20c-42cc-aecb-521651974674.json'
AUTHOR = 'json_to_solo'

class DresserWardrobe(Solo48):
    icon_id = 'dresser-wardrobe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('dresser', 'wardrobe', 'furnitures')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 40))
        self.add_line('sym-e1', (24, 40), (9, 40))
        self.add_line('sym-e2', (9, 40), (9, 42))
        self.add_line('sym-e3', (24, 6), (8, 6))
        self.add_arc('sym-e4', (8, 6), (6, 7), radius_x=3, sweep=False)
        self.add_line('sym-e5', (6, 7), (6, 8))
        self.add_line('sym-e6', (6, 8), (6, 39))
        self.add_arc('sym-e8', (6, 39), (8, 40), radius_x=3, sweep=False)
        self.add_line('sym-e9', (8, 40), (9, 40))
        self.add_line('sym-e10', (17, 25), (17, 22))
        self.add_line('sym-e11', (39, 42), (39, 40))
        self.add_line('sym-e12', (39, 40), (40, 40))
        self.add_arc('sym-e13', (40, 40), (42, 39), radius_x=2, sweep=False)
        self.add_line('sym-e15', (42, 39), (42, 8))
        self.add_arc('sym-e16', (42, 8), (42, 7), radius_x=21)
        self.add_line('sym-e17', (42, 7), (40, 6))
        self.add_line('sym-e18', (40, 6), (24, 6))
        self.add_line('sym-e19', (39, 40), (24, 40))
        self.add_line('sym-e20', (31, 25), (31, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c4', 'sym-e19')
        self.add_contour('sym-c5', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
