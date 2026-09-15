'An open hand rises vertically from a row of rounded waves. Four fingers extend above the palm and the thumb spreads right, with the wrist ending just above the water.\n\nConstruction: Open hand projects above water; long fingers and spread thumb distinguish the distress gesture. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '308c7b26-332e-4a63-acca-d4c8af288d7f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety drown hand_308c7b26-332e-4a63-acca-d4c8af288d7f.svg'
AUTHOR = 'gpt-6'

class HandAboveWater(Solo48):
    icon_id = 'hand-above-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('hand', 'water', 'drowning', 'rescue', 'safety', 'waves')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('wrist-left', (14, 29), (10, 29))
        self.add_arc('palm-left', (10, 29), (6, 25), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('little-side', (6, 25), (6, 20))
        self.add_arc('little-tip', (6, 20), (14, 20), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('ring-side', (14, 20), (14, 14))
        self.add_arc('ring-tip', (14, 14), (22, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('middle-side', (22, 14), (22, 10))
        self.add_arc('middle-tip', (22, 10), (30, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('index-side', (30, 10), (30, 14))
        self.add_arc('index-tip', (30, 14), (38, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('index-outer', (38, 14), (38, 20))
        self.add_arc('thumb-tip', (38, 20), (42, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('palm-right', (42, 24), (34, 29), radius_x=8, radius_y=5, large_arc=False, sweep=True)
        self.add_line('finger-14', (14, 20), (14, 24))
        self.add_line('finger-22', (22, 14), (22, 24))
        self.add_line('finger-30', (30, 14), (30, 24))
        self.add_arc('water-0', (6, 40), (18, 40), radius_x=6, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('water-1', (18, 40), (30, 40), radius_x=6, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('water-2', (30, 40), (42, 40), radius_x=6, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('hand', 'wrist-left', 'palm-left', 'little-side', 'little-tip', 'ring-side', 'ring-tip', 'middle-side', 'middle-tip', 'index-side', 'index-tip', 'index-outer', 'thumb-tip', 'palm-right', closed=False)
        self.add_contour('water', 'water-0', 'water-1', 'water-2', closed=False)
        self.relate('connect', 'finger-14', 'hand')
        self.relate('connect', 'finger-22', 'hand')
        self.relate('connect', 'finger-30', 'hand')
