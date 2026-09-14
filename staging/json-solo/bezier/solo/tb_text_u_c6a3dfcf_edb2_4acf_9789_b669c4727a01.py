"""Tb (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6a3dfcf-edb2-4acf-9789-b669c4727a01'
SOURCE_PATH = 'icons-json/symbol/tb (text u)_c6a3dfcf-edb2-4acf-9789-b669c4727a01.json'
AUTHOR = 'json_to_solo'

class TbTextUSymbol(Solo48):
    icon_id = 'tb-text-u-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('tb', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (8, 4), (21, 4))
        self.add_line('e1', (15, 27), (15, 4))
        self.add_line('e2', (30, 4), (30, 20))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_bezier('e4', (37, 12), ((31.375, 9.655), (29.651, 15.309), (29.895, 20.364)), ((29.962, 21.736), (30.147, 23.191), (30.829, 24.391)), ((32.286, 26.927), (36, 27.091), (37.971, 25.173)), ((39.427, 23.745), (39.983, 21.436), (39.983, 19.364)), ((39.983, 19.027), (40, 18.691), (40, 18.345)), ((40, 18.027), (39.983, 17.709), (39.983, 17.391)), ((39.983, 15.182), (38.718, 13.191), (37, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c4')
