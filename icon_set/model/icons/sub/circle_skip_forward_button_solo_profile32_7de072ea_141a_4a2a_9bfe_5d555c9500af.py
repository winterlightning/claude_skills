"""Independent 32px profile of circle-skip-forward-button-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7de072ea-141a-4a2a-9bfe-5d555c9500af'
SOURCE_PATH = 'pictographic-primitives/other/circle button next_7de072ea-141a-4a2a-9bfe-5d555c9500af.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7de072ea-141a-4a2a-9bfe-5d555c9500af', 'pictographic-primitives/other/circle button next_7de072ea-141a-4a2a-9bfe-5d555c9500af.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-skip-forward-button-solo',)
SOLO_SOURCE_ICON_IDS = ('circle-skip-forward-button-solo',)
REFERENCE_EXPORT_SHA256 = 'fcfe0047f537e4f077d475f573800958eeecd1d46c71a2f89e0f24f45a8b6d2a'

class Drawing(Sub32):
    icon_id = 'circle-skip-forward-button-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (10, 11), (16, 16))
        self.add_line('p2-r1-2', (16, 16), (10, 21))
        self.add_line('p2-r1-3', (10, 21), (10, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (22, 12), (22, 20))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
