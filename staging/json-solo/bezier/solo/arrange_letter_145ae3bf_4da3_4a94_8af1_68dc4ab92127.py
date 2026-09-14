"""Arrange letter (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '145ae3bf-4da3-4a94-8af1-68dc4ab92127'
SOURCE_PATH = 'icons-json/_uncategorized_04/arrange letter_145ae3bf-4da3-4a94-8af1-68dc4ab92127.json'
AUTHOR = 'json_to_solo'

class ArrangeLetterUncategorized04(Solo48):
    icon_id = 'arrange-letter-uncategorized-04'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('arrange', 'letter', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (30, 19), (31, 13))
        self.add_line('e1', (40, 19), (39, 13))
        self.add_line('e2', (31, 13), (32, 7))
        self.add_line('e3', (38, 7), (39, 13))
        self.add_line('e4', (31, 13), (39, 13))
        self.add_line('e5', (13, 10), (13, 35))
        self.add_line('e6', (8, 29), (13, 35))
        self.add_line('e7', (19, 29), (13, 35))
        self.add_line('e8', (30, 29), (40, 29))
        self.add_line('e9', (40, 29), (30, 44))
        self.add_line('e10', (30, 44), (39, 44))
        self.add_bezier('e11', (32, 7), ((32.194, 5.509), (33.389, 4.009), (34.737, 4.009)), ((34.77, 4), (34.803, 4), (34.844, 4)), ((34.845, 4), (34.846, 4), (34.846, 4)), ((34.914, 4), (34.981, 4.009), (35.057, 4.009)), ((36.345, 4.009), (37.806, 5.545), (38, 7)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e11', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e8', 'e9', 'e10')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
