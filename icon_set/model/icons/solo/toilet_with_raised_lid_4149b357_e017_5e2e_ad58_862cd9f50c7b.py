'A toilet is shown from the side with a tall rounded lid raised behind a horizontal seat. The bowl curves inward to a narrow pedestal above a short flat base.\n\nConstruction: Side-view bowl with an upright lid and pedestal foot. Bounds (8,4)-(40,44).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4149b357-e017-5e2e-ad58-862cd9f50c7b'
SOURCE_PATH = 'pictographic-primitives/wayfinding/toilet seat_4149b357-e017-5e2e-ad58-862cd9f50c7b.svg'
AUTHOR = 'gpt-6'

class ToiletWithRaisedLid(Solo48):
    icon_id = 'toilet-with-raised-lid'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('toilet', 'lid', 'seat', 'bowl', 'bathroom', 'restroom')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('lid-0', (12, 4), (12, 4))
        self.add_arc('lid-1', (12, 4), (16, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('lid-2', (16, 8), (16, 20))
        self.add_arc('lid-3', (16, 20), (12, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('lid-4', (12, 24), (12, 24))
        self.add_arc('lid-5', (12, 24), (8, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('lid-6', (8, 20), (8, 8))
        self.add_arc('lid-7', (8, 8), (12, 4), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('rim-1', (16, 24), (40, 24))
        self.add_line('rim-2', (40, 24), (40, 32))
        self.add_arc('bowl', (40, 32), (26, 40), radius_x=14, radius_y=8, large_arc=False, sweep=True)
        self.add_line('pedestal-1', (26, 40), (30, 44))
        self.add_line('pedestal-2', (30, 44), (14, 44))
        self.add_line('pedestal-3', (14, 44), (14, 32))
        self.add_line('pedestal-4', (14, 32), (8, 24))
        self.add_line('pedestal-5-joint-1', (8, 24), (12, 24))
        self.add_line('pedestal-5-joint-2', (12, 24), (16, 24))
        self.add_contour('lid', 'lid-0', 'lid-1', 'lid-2', 'lid-3', 'lid-4', 'lid-5', 'lid-6', 'lid-7', closed=True)
        self.add_contour('toilet', 'rim-1', 'rim-2', 'bowl', 'pedestal-1', 'pedestal-2', 'pedestal-3', 'pedestal-4', 'pedestal-5-joint-1', 'pedestal-5-joint-2', closed=False)
        self.relate('connect', 'lid', 'toilet')
