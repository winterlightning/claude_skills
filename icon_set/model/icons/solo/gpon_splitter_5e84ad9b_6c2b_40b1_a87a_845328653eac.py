"""Gpon splitter (networks), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e84ad9b-6c2b-40b1-a87a-845328653eac'
SOURCE_PATH = 'pictographic-primitives/networks/gpon splitter_5e84ad9b-6c2b-40b1-a87a-845328653eac.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class GponSplitter(Solo48):
    icon_id = 'gpon-splitter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    categories = ('primitives', 'networks')
    aliases = ()
    keywords = ('gpon', 'splitter', 'networks')

    def build(self):
        self.add_arc('sym-e0', (17, 24), (23, 18), radius_x=6)
        self.add_arc('sym-e1', (23, 18), (29, 24), radius_x=6)
        self.add_arc('sym-e2', (29, 24), (23, 30), radius_x=6)
        self.add_arc('sym-e3', (23, 30), (17, 24), radius_x=6)
        self.add_line('sym-e4', (6, 24), (17, 24))
        self.add_line('sym-e5', (29, 24), (42, 24))
        self.add_line('sym-e6', (42, 24), (39, 21))
        self.add_line('sym-e7', (20, 9), (23, 6))
        self.add_line('sym-e8', (23, 6), (26, 9))
        self.add_line('sym-e9', (23, 6), (23, 18))
        self.add_line('sym-e10', (20, 39), (23, 42))
        self.add_line('sym-e11', (23, 42), (26, 39))
        self.add_line('sym-e12', (39, 27), (42, 24))
        self.add_line('sym-e13', (23, 42), (23, 30))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c1', 'sym-e4')
        self.add_contour('sym-c2', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c4', 'sym-e9')
        self.add_contour('sym-c5', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c6', 'sym-e12')
        self.add_contour('sym-c7', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c7')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c5', 'sym-c7')
        self.relate('connect', 'sym-c5', 'sym-c7')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c5', 'sym-c7')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c6')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c7')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
