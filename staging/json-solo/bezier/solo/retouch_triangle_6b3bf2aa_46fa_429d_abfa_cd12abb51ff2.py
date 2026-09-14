"""Retouch triangle (photography), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b3bf2aa-46fa-429d-abfa-cd12abb51ff2'
SOURCE_PATH = 'icons-json/photography/retouch triangle_6b3bf2aa-46fa-429d-abfa-cd12abb51ff2.json'
AUTHOR = 'json_to_solo'

class RetouchTrianglePhotography(Solo48):
    icon_id = 'retouch-triangle-photography'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('retouch', 'triangle', 'photography')

    def build(self):
        self.add_line('e0', (24, 9), (24, 4))
        self.add_line('e1', (16, 9), (19, 11))
        self.add_line('e2', (29, 12), (32, 9))
        self.add_line('e3', (24, 14), (40, 44))
        self.add_line('e4', (40, 44), (8, 44))
        self.add_line('e5', (8, 44), (24, 14))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5', closed=True)
