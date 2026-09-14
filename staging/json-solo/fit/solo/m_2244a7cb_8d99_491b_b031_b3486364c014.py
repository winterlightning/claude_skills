"""M (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2244a7cb-8d99-491b-b031-b3486364c014'
SOURCE_PATH = 'icons-json/typeface/m_2244a7cb-8d99-491b-b031-b3486364c014.json'
AUTHOR = 'json_to_solo'

class M2244a7cb(Solo48):
    icon_id = 'm-2244a7cb'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('m', 'typeface')

    def build(self):
        self.add_line('e0', (4, 9), (4, 40))
        self.add_line('e1', (24, 18), (24, 40))
        self.add_line('e2', (44, 18), (44, 40))
        self.add_arc('e3-1', (4, 16), (14, 8), radius_x=11)
        self.add_arc('e3-2', (14, 8), (24, 18), radius_x=10)
        self.add_arc('e4-1', (24, 16), (28, 10), radius_x=12)
        self.add_line('e4-2', (28, 10), (34, 8))
        self.add_arc('e4-3', (34, 8), (44, 18), radius_x=10)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e1')
        self.add_contour('c2', 'e4-1', 'e4-2', 'e4-3', 'e2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
