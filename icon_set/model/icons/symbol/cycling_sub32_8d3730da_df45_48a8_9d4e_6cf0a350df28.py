"""Independent 32px profile of cycling.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8d3730da-df45-48a8-9d4e-6cf0a350df28'
SOURCE_PATH = 'pictographic-primitives/symbol/cycling_8d3730da-df45-48a8-9d4e-6cf0a350df28.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8d3730da-df45-48a8-9d4e-6cf0a350df28', 'pictographic-primitives/symbol/cycling_8d3730da-df45-48a8-9d4e-6cf0a350df28.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cycling',)
SOLO_SOURCE_ICON_IDS = ('cycling',)
REFERENCE_EXPORT_SHA256 = '79f19792932b7ed28723b4f90d07ff21bb1c8645dcd232b4737940c04059f98b'

class Drawing(Sub32):
    icon_id = 'cycling-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Cyclist: two wheels, bike frame from rim to rim, rider leaning forward from the seat, head dot.
        for k, x in enumerate((7, 25)):
            self.add_arc(f'w{k}-1', (x - 5, 25), (x + 5, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
            self.add_arc(f'w{k}-2', (x + 5, 25), (x - 5, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
            self.add_contour(f'wheel-{k}', f'w{k}-1', f'w{k}-2', closed=True)
        self.add_polyline('frame', (10, 21), (14, 14), (18, 14), (25, 20))
        self.add_line('torso', (14, 14), (17, 10))
        self.add_arc('head-1', (23, 4), (27, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('head-2', (27, 4), (23, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        for a, b in (('frame', 'wheel-0'), ('frame', 'wheel-1'), ('frame', 'torso')):
            self.relate('connect', a, b)
