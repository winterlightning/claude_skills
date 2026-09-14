"""Megaphone (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '419cefd4-6e8d-4c3c-8b36-3566f3fa846b'
SOURCE_PATH = 'icons-json/interface-essential/megaphone_419cefd4-6e8d-4c3c-8b36-3566f3fa846b.json'
AUTHOR = 'json_to_solo'

class Megaphone419cefd4(Solo48):
    icon_id = 'megaphone-419cefd4'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('megaphone', 'interface-essential')

    def build(self):
        self.add_line('e0', (21, 39), (19, 40))
        self.add_line('e1', (16, 38), (11, 32))
        self.add_line('e2', (16, 21), (19, 31))
        self.add_line('e3', (11, 32), (19, 31))
        self.add_line('e4', (16, 21), (20, 20))
        self.add_line('e5', (32, 12), (38, 8))
        self.add_line('e6', (38, 8), (44, 32))
        self.add_line('e7', (44, 32), (38, 30))
        self.add_line('e8', (25, 30), (19, 31))
        self.add_bezier('e9', (19, 40), ((18.9, 40), (19.245, 40), (19.145, 40)), ((17.864, 40), (16.736, 38.952), (16, 38)))
        self.add_bezier('e10', (11, 32), ((7.482, 32.724), (4, 31.385), (4, 27.688)), ((4, 27.687), (4, 27.686), (4, 27.684)), ((4, 27.593), (4, 27.493), (4, 27.402)), ((4, 23.141), (8.864, 22.535), (12.245, 21.634)), ((13.455, 21.314), (14.764, 21.227), (16, 21)))
        self.add_bezier('e11', (20, 20), ((21.164, 19.781), (22.455, 18.939), (23.436, 18.375)), ((26.573, 16.539), (29.164, 14.189), (32, 12)))
        self.add_bezier('e12', (38, 30), ((34.918, 29.183), (28.209, 29.503), (25, 30)))
        self.add_contour('c0', 'e0', 'e9', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e10', 'e4', 'e11', 'e5', 'e6', 'e7', 'e12', 'e8')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
