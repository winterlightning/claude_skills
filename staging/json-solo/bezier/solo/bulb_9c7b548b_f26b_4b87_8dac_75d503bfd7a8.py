"""Bulb (work), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c7b548b-f26b-4b87-8dac-75d503bfd7a8'
SOURCE_PATH = 'icons-json/work/bulb_9c7b548b-f26b-4b87-8dac-75d503bfd7a8.json'
AUTHOR = 'json_to_solo'

class BulbWork(Solo48):
    icon_id = 'bulb-work'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    aliases = ()
    keywords = ('bulb', 'work')

    def build(self):
        self.add_line('e0', (24, 8), (24, 10))
        self.add_line('e1', (9, 13), (11, 15))
        self.add_line('e2', (4, 26), (6, 26))
        self.add_line('e3', (44, 26), (42, 26))
        self.add_line('e4', (18, 31), (30, 31))
        self.add_line('e5', (21, 40), (27, 40))
        self.add_line('e6', (30, 32), (32, 28))
        self.add_line('e7', (16, 28), (18, 32))
        self.add_bezier('e8', (37, 14), ((37.609, 13.722), (38.391, 13.278), (39, 13)))
        self.add_bezier('e9', (27, 40), ((27.191, 40), (27.109, 39.983), (27.3, 39.983)), ((27.736, 39.983), (28.691, 38.762), (28.791, 38.349)), ((29.018, 37.415), (28.873, 36.303), (28.936, 35.36)), ((29.009, 34.274), (29.473, 32.977), (30, 32)))
        self.add_bezier('e10', (32, 28), ((32.709, 26.678), (33.591, 25.415), (33.664, 23.933)), ((33.755, 22.198), (33.1, 20.556), (31.991, 19.166)), ((27.991, 14.147), (19.927, 14.198), (16, 19.251)), ((15.018, 20.514), (14.473, 22.046), (14.427, 23.604)), ((14.391, 25.145), (15.264, 26.636), (16, 28)))
        self.add_bezier('e11', (18, 32), ((18.682, 33.263), (19.009, 34.442), (19.118, 35.857)), ((19.173, 36.589), (19.064, 37.373), (19.218, 38.097)), ((19.3, 38.526), (20.255, 40), (20.736, 40)), ((20.782, 39.983), (20.818, 39.966), (20.864, 39.949)), ((21, 39.966), (20.864, 39.983), (21, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3')
        self.add_contour('c5', 'e4')
        self.add_contour('c6', 'e5', 'e9', 'e6', 'e10', 'e7', 'e11', closed=True)
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c6')
