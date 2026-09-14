"""Rectangle two dots (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b499c107-a18c-412b-a0f2-7df8766d8257'
SOURCE_PATH = 'icons-json/state/rectangle two dots_b499c107-a18c-412b-a0f2-7df8766d8257.json'
AUTHOR = 'json_to_solo'

class RectangleTwoDotsState(Solo48):
    icon_id = 'rectangle-two-dots-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rectangle', 'two', 'dots', 'state')

    def build(self):
        self.add_bezier('sym-e0', (24, 34), ((24, 34.3), (24, 34.7), (24, 35)))
        self.add_bezier('sym-e1', (24, 15), ((24, 15.3), (24, 15.7), (24, 16)))
        self.add_line('sym-e2', (24, 44), (10, 44))
        self.add_bezier('sym-e3', (10, 44), ((9.01, 43.436), (8, 43.236), (8, 42)))
        self.add_bezier('sym-e4', (8, 42), ((8, 41.918), (8.01, 41.082), (8, 41)))
        self.add_line('sym-e5', (8, 41), (8, 7))
        self.add_bezier('sym-e6', (8, 7), ((8, 6.945), (8, 7.045), (8, 7)))
        self.add_bezier('sym-e7', (8, 7), ((8, 6.164), (8.29, 4.491), (9, 4)))
        self.add_bezier('sym-e8', (9, 4), ((9.19, 4), (9.81, 4.109), (10, 4)))
        self.add_line('sym-e9', (10, 4), (24, 4))
        self.add_line('sym-e10', (24, 4), (38, 4))
        self.add_bezier('sym-e11', (38, 4), ((38.19, 4.109), (38.81, 4), (39, 4)))
        self.add_bezier('sym-e12', (39, 4), ((39.71, 4.491), (40, 6.164), (40, 7)))
        self.add_bezier('sym-e13', (40, 7), ((40, 7.045), (40, 6.945), (40, 7)))
        self.add_line('sym-e14', (40, 7), (40, 41))
        self.add_bezier('sym-e15', (40, 41), ((39.99, 41.082), (40, 41.918), (40, 42)))
        self.add_bezier('sym-e16', (40, 42), ((40, 43.236), (38.99, 43.436), (38, 44)))
        self.add_line('sym-e17', (38, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
