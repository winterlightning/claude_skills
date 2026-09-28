"""Divided highway (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '119db938-3f33-45b7-8cd9-06705c94fc1f'
SOURCE_PATH = 'pictographic-primitives/transportation/divided highway_119db938-3f33-45b7-8cd9-06705c94fc1f.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class DividedHighway(Solo48):
    icon_id = 'divided-highway'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('divided', 'highway', 'transportation')

    def build(self):
        self.add_line('sym-e0', (40, 4), (40, 27))
        self.add_line('sym-e1', (40, 27), (38, 29))
        self.add_line('sym-e2', (38, 29), (35, 33))
        self.add_arc('sym-e3', (35, 33), (34, 36), radius_x=5, sweep=False)
        self.add_line('sym-e4', (34, 36), (34, 44))
        self.add_line('sym-e5', (34, 44), (37, 41))
        self.add_line('sym-e6', (31, 41), (34, 44))
        self.add_line('sym-e7', (24, 20), (28, 18))
        self.add_line('sym-e8', (28, 18), (29, 16))
        self.add_line('sym-e9', (29, 16), (29, 7))
        self.add_line('sym-e10', (8, 4), (8, 27))
        self.add_line('sym-e11', (8, 27), (10, 29))
        self.add_line('sym-e12', (10, 29), (13, 33))
        self.add_arc('sym-e13', (13, 33), (14, 36), radius_x=5)
        self.add_line('sym-e14', (14, 36), (14, 44))
        self.add_line('sym-e15', (14, 44), (11, 41))
        self.add_line('sym-e16', (17, 41), (14, 44))
        self.add_line('sym-e17', (24, 20), (20, 18))
        self.add_line('sym-e18', (20, 18), (19, 16))
        self.add_line('sym-e19', (19, 16), (19, 7))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c3', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15')
        self.add_contour('sym-c4', 'sym-e16')
        self.add_contour('sym-c5', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c3', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c1')
