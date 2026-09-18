"""Independent 32px profile of minus-bold.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a6b4ed56-3a81-4fe8-ab46-c2e8af425eff'
SOURCE_PATH = 'pictographic-primitives/state/minus bold_a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a6b4ed56-3a81-4fe8-ab46-c2e8af425eff', 'pictographic-primitives/state/minus bold_a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.svg'),)
PROFILE_SOURCE_KEYS = ('solo/minus-bold',)
SOLO_SOURCE_ICON_IDS = ('minus-bold',)
REFERENCE_EXPORT_SHA256 = '7b8f3082619ce5237a6e1d44ab69665d9a1569915821bd0df89c59cd4e651d44'

class Drawing(Sub32):
    icon_id = 'minus-bold-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 27), (5, 27))
        self.add_arc('p1-r1-2', (5, 27), (2, 22), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (2, 22), (2, 21))
        self.add_arc('p1-r1-4', (2, 21), (2, 20), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (2, 20), (2, 13))
        self.add_arc('p1-r1-6', (2, 13), (2, 11), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-7', (2, 11), (2, 10))
        self.add_arc('p1-r1-8', (2, 10), (5, 5), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-9', (5, 5), (27, 5))
        self.add_arc('p1-r1-10', (27, 5), (30, 10), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (30, 10), (30, 11))
        self.add_arc('p1-r1-12', (30, 11), (30, 13), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-13', (30, 13), (30, 20))
        self.add_arc('p1-r1-14', (30, 20), (30, 21), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-15', (30, 21), (30, 22))
        self.add_arc('p1-r1-16', (30, 22), (27, 27), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', closed=False)
