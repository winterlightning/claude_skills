"""Batch-07/accessories necklace (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '304c082c-7604-5a82-9d4c-a7d6655317a1'
SOURCE_PATH = 'icons-json/accessories/batch-07/accessories necklace_304c082c-7604-5a82-9d4c-a7d6655317a1.json'
AUTHOR = 'json_to_solo'

class Batch07AccessoriesNecklace(Solo48):
    icon_id = 'batch-07-accessories-necklace'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'accessories', 'necklace')

    def build(self):
        self.add_arc('sym-e0', (19, 39), (29, 39), radius_x=5)
        self.add_arc('sym-e1', (29, 39), (19, 39), radius_x=5)
        self.add_bezier('sym-e2', (21, 34), ((19.215, 33.282), (16.659, 33.027), (15, 32)))
        self.add_bezier('sym-e3', (15, 32), ((10.402, 29.191), (8, 22.609), (8, 17)))
        self.add_bezier('sym-e4', (8, 17), ((8, 16.7), (8, 16.291), (8, 16)))
        self.add_bezier('sym-e5', (8, 16), ((8.008, 15.927), (8, 16.073), (8, 16)))
        self.add_bezier('sym-e6', (8, 16), ((8, 11.764), (10.339, 7.936), (13, 5)))
        self.add_bezier('sym-e7', (13, 5), ((13.303, 4.664), (13.663, 4.264), (14, 4)))
        self.add_bezier('sym-e8', (14, 4), ((14.101, 4), (13.891, 4.073), (14, 4)))
        self.add_bezier('sym-e9', (27, 34), ((28.785, 33.282), (31.341, 33.027), (33, 32)))
        self.add_bezier('sym-e10', (33, 32), ((37.598, 29.191), (40, 22.609), (40, 17)))
        self.add_bezier('sym-e11', (40, 17), ((40, 16.7), (40, 16.291), (40, 16)))
        self.add_bezier('sym-e12', (40, 16), ((39.992, 15.927), (40, 16.073), (40, 16)))
        self.add_bezier('sym-e13', (40, 16), ((40, 11.764), (37.661, 7.936), (35, 5)))
        self.add_bezier('sym-e14', (35, 5), ((34.697, 4.664), (34.337, 4.264), (34, 4)))
        self.add_bezier('sym-e15', (34, 4), ((33.899, 4), (34.109, 4.073), (34, 4)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
