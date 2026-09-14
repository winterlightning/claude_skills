"""Kiss (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3da870d-5ef5-5b8c-bdba-94c1a572793f'
SOURCE_PATH = 'icons-json/smileys/kiss_d3da870d-5ef5-5b8c-bdba-94c1a572793f.json'
AUTHOR = 'json_to_solo'

class KissD3da870d(Solo48):
    icon_id = 'kiss-d3da870d'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('kiss', 'smileys')

    def build(self):
        self.add_line('e0', (12, 19), (19, 19))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e2-1', (27, 32), (28, 28), radius_x=3, sweep=False)
        self.add_arc('e2-2', (28, 28), (24, 27), radius_x=6, sweep=False)
        self.add_arc('e3-1', (27, 32), (28, 36), radius_x=3)
        self.add_line('e3-2', (28, 36), (24, 38))
        self.add_arc('e4', (27, 32), (25, 32), radius_x=27, sweep=False)
        self.add_arc('e5', (28, 20), (36, 20), radius_x=6)
        self.add_contour('c0', 'e2-1', 'e2-2')
        self.add_contour('c1', 'e3-1', 'e3-2')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
