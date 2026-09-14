"""Make up brush (beauty), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e16dd241-96b2-4b10-9b5a-ee1bb50491a2'
SOURCE_PATH = 'icons-json/beauty/make up brush_e16dd241-96b2-4b10-9b5a-ee1bb50491a2.json'
AUTHOR = 'json_to_solo'

class MakeUpBrush(Solo48):
    icon_id = 'make-up-brush'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('make', 'up', 'brush', 'beauty')

    def build(self):
        self.add_line('e0', (16, 20), (8, 12))
        self.add_line('e1', (40, 12), (32, 20))
        self.add_line('e2', (32, 20), (16, 20))
        self.add_line('e3', (19, 28), (19, 41))
        self.add_line('e4', (29, 41), (29, 28))
        self.add_line('e5', (21, 12), (22, 20))
        self.add_line('e6-1', (8, 12), (8, 9))
        self.add_arc('e6-2', (8, 9), (13, 6), radius_x=12)
        self.add_arc('e6-3', (13, 6), (23, 4), radius_x=28)
        self.add_line('e6-4', (23, 4), (32, 5))
        self.add_arc('e6-5', (32, 5), (39, 8), radius_x=20)
        self.add_line('e6-6', (39, 8), (40, 12))
        self.add_arc('e7', (16, 20), (19, 28), radius_x=6, sweep=False)
        self.add_arc('e8-1', (19, 41), (24, 44), radius_x=6, sweep=False)
        self.add_arc('e8-2', (24, 44), (29, 41), radius_x=6, sweep=False)
        self.add_arc('e9', (29, 28), (32, 20), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e1', 'e2', 'e7', 'e3', 'e8-1', 'e8-2', 'e4')
        self.add_contour('c1', 'e9')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c2', 'c0')
