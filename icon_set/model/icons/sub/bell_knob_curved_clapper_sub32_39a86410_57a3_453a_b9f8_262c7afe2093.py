"""Independent 32px profile of bell-knob-curved-clapper.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '39a86410-57a3-453a-b9f8-262c7afe2093'
SOURCE_PATH = 'pictographic-primitives/symbol/ring_39a86410-57a3-453a-b9f8-262c7afe2093.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('39a86410-57a3-453a-b9f8-262c7afe2093', 'pictographic-primitives/symbol/ring_39a86410-57a3-453a-b9f8-262c7afe2093.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bell-knob-curved-clapper',)
SOLO_SOURCE_ICON_IDS = ('bell-knob-curved-clapper',)
REFERENCE_EXPORT_SHA256 = 'c09581e29e7446aa593c50b6da69f5a0cfca5b93c9cb8eb176e35f8985b406c5'

class Drawing(Sub32):
    icon_id = 'bell-knob-curved-clapper-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (8, 17), (24, 17), radius_x=8, radius_y=9, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (24, 17), (24, 18))
        self.add_arc('p2-r1-3', (24, 18), (27, 22), radius_x=5, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p2-r1-4', (27, 22), (5, 22))
        self.add_arc('p2-r1-5', (5, 22), (8, 18), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p2-r1-6', (8, 18), (8, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_arc('p3-r1-1', (13, 29), (19, 29), radius_x=3, radius_y=1, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
