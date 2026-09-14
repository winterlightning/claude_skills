"""Love compatibility (romance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13ea8ba1-9370-50ce-9da5-f3a7facdf796'
SOURCE_PATH = 'icons-json/romance/love compatibility_13ea8ba1-9370-50ce-9da5-f3a7facdf796.json'
AUTHOR = 'json_to_solo'

class LoveCompatibilityRomance(Solo48):
    icon_id = 'love-compatibility-romance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('love', 'compatibility', 'romance')

    def build(self):
        self.add_line('e0', (19, 40), (26, 34))
        self.add_line('e1', (26, 34), (31, 40))
        self.add_arc('e2-1', (36, 16), (31, 9), radius_x=11, sweep=False)
        self.add_line('e2-2', (31, 9), (27, 8))
        self.add_arc('e2-3', (27, 8), (20, 12), radius_x=9, sweep=False)
        self.add_arc('e2-4', (20, 12), (12, 8), radius_x=11, sweep=False)
        self.add_arc('e2-5', (12, 8), (6, 11), radius_x=8, sweep=False)
        self.add_line('e2-6', (6, 11), (4, 18))
        self.add_arc('e2-7', (4, 18), (19, 40), radius_x=43, sweep=False)
        self.add_arc('e3-1', (31, 40), (44, 23), radius_x=24, sweep=False)
        self.add_line('e3-2', (44, 23), (43, 19))
        self.add_arc('e3-3', (43, 19), (40, 16), radius_x=6, sweep=False)
        self.add_arc('e3-4', (40, 16), (32, 19), radius_x=7, sweep=False)
        self.add_arc('e3-5', (32, 19), (28, 16), radius_x=9, sweep=False)
        self.add_arc('e3-6', (28, 16), (21, 18), radius_x=6, sweep=False)
        self.add_arc('e3-7', (21, 18), (26, 34), radius_x=13, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e0')
        self.add_contour('c1', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
