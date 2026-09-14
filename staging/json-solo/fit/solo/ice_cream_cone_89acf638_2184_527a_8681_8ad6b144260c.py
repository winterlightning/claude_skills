"""Ice cream cone (food), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89acf638-2184-527a-8681-8ad6b144260c'
SOURCE_PATH = 'icons-json/food/ice cream cone_89acf638-2184-527a-8681-8ad6b144260c.json'
AUTHOR = 'json_to_solo'

class IceCreamCone89acf638(Solo48):
    icon_id = 'ice-cream-cone-89acf638'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'cone', 'food')

    def build(self):
        self.add_line('e0', (12, 22), (23, 42))
        self.add_line('e1', (23, 42), (24, 44))
        self.add_line('e2', (24, 44), (36, 23))
        self.add_line('e3', (34, 7), (29, 5))
        self.add_arc('e4', (30, 21), (19, 21), radius_x=7)
        self.add_arc('e5-1', (36, 23), (40, 19), radius_x=4, sweep=False)
        self.add_line('e5-2', (40, 19), (38, 12))
        self.add_arc('e5-3', (38, 12), (34, 7), radius_x=8, sweep=False)
        self.add_arc('e6-1', (29, 5), (23, 4), radius_x=22, sweep=False)
        self.add_arc('e6-2', (23, 4), (13, 8), radius_x=18, sweep=False)
        self.add_line('e6-3', (13, 8), (8, 18))
        self.add_arc('e6-4', (8, 18), (19, 21), radius_x=7, sweep=False)
        self.add_arc('e7', (36, 23), (30, 21), radius_x=8)
        self.add_contour('c0', 'e4')
        self.add_contour('c1', 'e0', 'e1', 'e2')
        self.add_contour('c2', 'e5-1', 'e5-2', 'e5-3', 'e3', 'e6-1', 'e6-2', 'e6-3', 'e6-4')
        self.add_contour('c3', 'e7')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
