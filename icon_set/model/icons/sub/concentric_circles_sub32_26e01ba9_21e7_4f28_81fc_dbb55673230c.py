"""Independent 32px profile of concentric-circles.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '26e01ba9-21e7-4f28-81fc-dbb55673230c'
SOURCE_PATH = 'pictographic-primitives/symbol/concentric circles_26e01ba9-21e7-4f28-81fc-dbb55673230c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('26e01ba9-21e7-4f28-81fc-dbb55673230c', 'pictographic-primitives/symbol/concentric circles_26e01ba9-21e7-4f28-81fc-dbb55673230c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/concentric-circles',)
SOLO_SOURCE_ICON_IDS = ('concentric-circles',)
REFERENCE_EXPORT_SHA256 = '47bdd3925984cab8e42192c0b6dd0c984af45fa0a80c625d4559e95cc18302a4'

class Drawing(Sub32):
    icon_id = 'concentric-circles-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (8, 16), (24, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (24, 16), (8, 16), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
