"""Split (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9be1009-50ba-42ef-813c-965725fd3f12'
SOURCE_PATH = 'icons-json/transportation/split_d9be1009-50ba-42ef-813c-965725fd3f12.json'
AUTHOR = 'json_to_solo'

class SplitD9be1009(Solo48):
    icon_id = 'split-d9be1009'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('split', 'transportation')

    def build(self):
        self.add_line('e0', (39, 8), (44, 13))
        self.add_line('e1', (4, 24), (20, 24))
        self.add_line('e2', (40, 40), (44, 36))
        self.add_line('e3', (40, 31), (44, 36))
        self.add_line('e4', (39, 17), (44, 13))
        self.add_line('e5', (25, 20), (28, 16))
        self.add_line('e6', (34, 13), (44, 13))
        self.add_line('e7', (25, 28), (28, 32))
        self.add_line('e8', (34, 36), (44, 36))
        self.add_bezier('e9', (20, 24), ((21.709, 22.87), (23.782, 21.78), (25, 20)))
        self.add_bezier('e10', (28, 16), ((29.255, 14.16), (31.973, 13), (34, 13)))
        self.add_bezier('e11', (20, 24), ((21.809, 25.12), (23.745, 26.16), (25, 28)))
        self.add_bezier('e12', (28, 32), ((29.218, 33.79), (31.882, 36), (34, 36)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e9', 'e5', 'e10', 'e6')
        self.add_contour('c6', 'e11', 'e7', 'e12', 'e8')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
