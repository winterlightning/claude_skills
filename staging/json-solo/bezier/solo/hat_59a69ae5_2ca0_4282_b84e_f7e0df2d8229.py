"""Batch-03/hat (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59a69ae5-2ca0-4282-b84e-f7e0df2d8229'
SOURCE_PATH = 'icons-json/accessories/batch-03/hat_59a69ae5-2ca0-4282-b84e-f7e0df2d8229.json'
AUTHOR = 'json_to_solo'

class Batch03Hat(Solo48):
    icon_id = 'batch-03-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'accessories')

    def build(self):
        self.add_line('sym-e0', (11, 31), (37, 31))
        self.add_line('sym-e1', (37, 31), (38, 40))
        self.add_line('sym-e2', (38, 40), (10, 40))
        self.add_line('sym-e3', (10, 40), (4, 40))
        self.add_line('sym-e4', (11, 31), (10, 40))
        self.add_line('sym-e5', (11, 31), (13, 9))
        self.add_bezier('sym-e6', (13, 9), ((13.182, 8.582), (13.482, 8), (14, 8)))
        self.add_bezier('sym-e7', (14, 8), ((14.055, 8), (13.945, 8.012), (14, 8)))
        self.add_line('sym-e8', (14, 8), (24, 12))
        self.add_line('sym-e9', (24, 12), (34, 8))
        self.add_bezier('sym-e10', (34, 8), ((34.055, 8.012), (33.945, 8), (34, 8)))
        self.add_bezier('sym-e11', (34, 8), ((34.518, 8), (34.818, 8.582), (35, 9)))
        self.add_line('sym-e12', (35, 9), (37, 31))
        self.add_line('sym-e13', (44, 40), (38, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c3', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
