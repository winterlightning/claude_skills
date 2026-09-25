"""Independent 32px profile of arrow-restart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '958c6ea9-a7de-42bf-ba04-e08a99041318'
SOURCE_PATH = 'pictographic-primitives/symbol/power off_958c6ea9-a7de-42bf-ba04-e08a99041318.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('958c6ea9-a7de-42bf-ba04-e08a99041318', 'pictographic-primitives/symbol/power off_958c6ea9-a7de-42bf-ba04-e08a99041318.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-restart',)
SOLO_SOURCE_ICON_IDS = ('arrow-restart',)
REFERENCE_EXPORT_SHA256 = '4fe01aca95b8a47472a13b10284d3e30a00c296a49ec0613b22b5d6089fa02bd'

class Drawing(Sub32):
    icon_id = 'arrow-restart-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (16, 2), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 9), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (9, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 2), (13, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-2', 'p3-r1-1')
