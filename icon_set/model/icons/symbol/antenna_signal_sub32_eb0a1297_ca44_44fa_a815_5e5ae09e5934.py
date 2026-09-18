"""Independent 32px profile of antenna-signal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'eb0a1297-ca44-44fa-a815-5e5ae09e5934'
SOURCE_PATH = 'pictographic-primitives/symbol/signal antenna_eb0a1297-ca44-44fa-a815-5e5ae09e5934.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eb0a1297-ca44-44fa-a815-5e5ae09e5934', 'pictographic-primitives/symbol/signal antenna_eb0a1297-ca44-44fa-a815-5e5ae09e5934.svg'),)
PROFILE_SOURCE_KEYS = ('solo/antenna-signal',)
SOLO_SOURCE_ICON_IDS = ('antenna-signal',)
REFERENCE_EXPORT_SHA256 = '3c0b7071dca227a73b4b5c1fcbd32aa55cdeb98a901402551080b0115e4d6f99'

class Drawing(Sub32):
    icon_id = 'antenna-signal-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 30), (11, 19))
        self.add_line('p1-r1-2', (11, 19), (16, 8))
        self.add_line('p1-r1-3', (16, 8), (21, 19))
        self.add_line('p1-r1-4', (21, 19), (25, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (11, 19), (21, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (5, 2), (5, 14), radius_x=3, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (27, 2), (27, 14), radius_x=3, radius_y=6, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
