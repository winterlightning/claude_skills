"""Independent 32px profile of shield-3bbd3635.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3bbd3635-ed19-4db8-953f-adcc7ed97b05'
SOURCE_PATH = 'pictographic-primitives/protection/shield_3bbd3635-ed19-4db8-953f-adcc7ed97b05.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3bbd3635-ed19-4db8-953f-adcc7ed97b05', 'pictographic-primitives/protection/shield_3bbd3635-ed19-4db8-953f-adcc7ed97b05.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shield-3bbd3635',)
SOLO_SOURCE_ICON_IDS = ('shield-3bbd3635',)
REFERENCE_EXPORT_SHA256 = '1af47d7d7b1c4ee049f475dfdc90039a4955a204e45826475e5df167bf55fb5a'

class Drawing(Sub32):
    icon_id = 'shield-3bbd3635-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 5), (10, 6), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-2', (10, 6), (16, 2))
        self.add_line('p1-r1-3', (16, 2), (22, 6))
        self.add_arc('p1-r1-4', (22, 6), (25, 6), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (25, 6), (27, 5))
        self.add_line('p1-r1-6', (27, 5), (27, 17))
        self.add_arc('p1-r1-7', (27, 17), (24, 24), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('p1-r1-8', (24, 24), (16, 30), radius_x=25, radius_y=25, large_arc=False, sweep=True)
        self.add_arc('p1-r1-9', (16, 30), (5, 16), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (5, 16), (5, 5))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (27, 14), (5, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
