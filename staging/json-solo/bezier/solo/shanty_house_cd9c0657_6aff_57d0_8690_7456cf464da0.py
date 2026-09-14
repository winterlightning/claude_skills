"""Batch-06/shanty house (landmarks), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd9c0657-6aff-57d0-8690-7456cf464da0'
SOURCE_PATH = 'icons-json/landmarks/batch-06/shanty house_cd9c0657-6aff-57d0-8690-7456cf464da0.json'
AUTHOR = 'json_to_solo'

class Batch06ShantyHouse(Solo48):
    icon_id = 'batch-06-shanty-house'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('batch', 'shanty', 'house', 'landmarks')

    def build(self):
        self.add_line('sym-e0', (29, 40), (29, 27))
        self.add_line('sym-e1', (29, 27), (19, 27))
        self.add_line('sym-e2', (19, 27), (19, 40))
        self.add_line('sym-e3', (19, 40), (10, 40))
        self.add_bezier('sym-e4', (10, 40), ((8.2, 39.419), (8, 38.869), (8, 37)))
        self.add_line('sym-e5', (8, 37), (8, 19))
        self.add_line('sym-e6', (4, 21), (24, 8))
        self.add_line('sym-e7', (24, 8), (44, 21))
        self.add_line('sym-e8', (40, 19), (40, 37))
        self.add_bezier('sym-e9', (40, 37), ((40, 38.869), (39.8, 39.419), (38, 40)))
        self.add_line('sym-e10', (38, 40), (29, 40))
        self.add_line('sym-e11', (29, 40), (24, 40))
        self.add_line('sym-e12', (24, 40), (19, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
