"""Ligature (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b92a4ea-94ba-4b72-ab50-9dc8c6925a25'
SOURCE_PATH = 'icons-json/interface-essential/ligature_7b92a4ea-94ba-4b72-ab50-9dc8c6925a25.json'
AUTHOR = 'json_to_solo'

class LigatureInterfaceEssential(Solo48):
    icon_id = 'ligature-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('ligature', 'interface-essential')

    def build(self):
        self.add_line('e0', (12, 13), (12, 26))
        self.add_line('e1', (9, 26), (12, 26))
        self.add_line('e2', (8, 44), (12, 44))
        self.add_line('e3', (16, 44), (12, 44))
        self.add_line('e4', (32, 44), (36, 44))
        self.add_line('e5', (40, 44), (36, 44))
        self.add_line('e6', (12, 44), (12, 26))
        self.add_line('e7', (36, 44), (36, 26))
        self.add_line('e8', (36, 26), (12, 26))
        self.add_bezier('e9', (36, 17), ((36, 15.373), (36.1, 13.491), (35.62, 11.9)), ((34.29, 7.509), (29.7, 4.009), (24.6, 4.009)), ((24.531, 4.009), (24.452, 4), (24.383, 4)), ((24.382, 4), (24.381, 4), (24.38, 4)), ((24.15, 4), (23.93, 4.009), (23.7, 4.009)), ((18.94, 4.009), (13.93, 7.164), (12.48, 11.291)), ((12.29, 11.818), (12, 12.445), (12, 13)))
        self.add_contour('c0', 'e9', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c7')
