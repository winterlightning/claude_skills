"""Batch-01/astrology aries (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28ab2a14-d6a4-56d6-82df-af778631fe00'
SOURCE_PATH = 'icons-json/culture/batch-01/astrology aries_28ab2a14-d6a4-56d6-82df-af778631fe00.json'
AUTHOR = 'json_to_solo'

class Batch01AstrologyAries(Solo48):
    icon_id = 'batch-01-astrology-aries'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'aries', 'culture')

    def build(self):
        self.add_bezier('sym-e0', (24, 40), ((25.5, 34.173), (26.809, 28.659), (29, 23)))
        self.add_bezier('sym-e1', (29, 23), ((30.082, 20.213), (31.2, 17.467), (33, 15)))
        self.add_bezier('sym-e2', (33, 15), ((35.036, 12.196), (39.055, 8), (43, 8)))
        self.add_bezier('sym-e3', (43, 8), ((43.291, 8), (43.709, 8), (44, 8)))
        self.add_bezier('sym-e4', (24, 40), ((22.5, 34.173), (21.191, 28.659), (19, 23)))
        self.add_bezier('sym-e5', (19, 23), ((17.918, 20.213), (16.8, 17.467), (15, 15)))
        self.add_bezier('sym-e6', (15, 15), ((12.964, 12.196), (8.945, 8), (5, 8)))
        self.add_bezier('sym-e7', (5, 8), ((4.709, 8), (4.291, 8), (4, 8)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.relate('connect', 'sym-c0', 'sym-c1')
