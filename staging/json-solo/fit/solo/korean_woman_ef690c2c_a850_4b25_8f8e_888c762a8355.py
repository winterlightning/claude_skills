"""Korean woman (avatars), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef690c2c-a850-4b25-8f8e-888c762a8355'
SOURCE_PATH = 'icons-json/avatars/korean woman_ef690c2c-a850-4b25-8f8e-888c762a8355.json'
AUTHOR = 'json_to_solo'

class KoreanWomanAvatars(Solo48):
    icon_id = 'korean-woman-avatars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('korean', 'woman', 'avatars')

    def build(self):
        self.add_line('e0', (20, 12), (20, 8))
        self.add_arc('e1-1', (36, 28), (44, 34), radius_x=7)
        self.add_arc('e1-2', (44, 34), (41, 39), radius_x=6)
        self.add_line('e1-3', (41, 39), (37, 40))
        self.add_arc('e1-4', (37, 40), (31, 36), radius_x=7)
        self.add_arc('e2', (36, 28), (31, 36), radius_x=16)
        self.add_arc('e3', (36, 28), (36, 22), radius_x=23)
        self.add_arc('e4', (20, 12), (36, 22), radius_x=15, sweep=False)
        self.add_arc('e5', (20, 12), (4, 22), radius_x=16)
        self.add_arc('e6-1', (36, 22), (32, 13), radius_x=12, sweep=False)
        self.add_arc('e6-2', (32, 13), (21, 8), radius_x=17, sweep=False)
        self.add_arc('e6-3', (21, 8), (20, 8), radius_x=31)
        self.add_arc('e7-1', (20, 8), (4, 21), radius_x=17, sweep=False)
        self.add_line('e7-2', (4, 21), (4, 22))
        self.add_arc('e8-1', (31, 36), (20, 40), radius_x=18)
        self.add_line('e8-2', (20, 40), (14, 39))
        self.add_arc('e8-3', (14, 39), (6, 32), radius_x=17)
        self.add_arc('e8-4', (6, 32), (4, 25), radius_x=15)
        self.add_line('e8-5', (4, 25), (4, 22))
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e0')
        self.add_contour('c6', 'e6-1', 'e6-2', 'e6-3')
        self.add_contour('c7', 'e7-1', 'e7-2')
        self.add_contour('c8', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
