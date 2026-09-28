"""Independent 32px profile of equalizer-cb9c3492.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'cb9c3492-0967-4a4f-9b7f-0f49d4679e9f'
SOURCE_PATH = 'pictographic-primitives/audio/equalizer_cb9c3492-0967-4a4f-9b7f-0f49d4679e9f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cb9c3492-0967-4a4f-9b7f-0f49d4679e9f', 'pictographic-primitives/audio/equalizer_cb9c3492-0967-4a4f-9b7f-0f49d4679e9f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/equalizer-cb9c3492',)
SOLO_SOURCE_ICON_IDS = ('equalizer-cb9c3492',)
REFERENCE_EXPORT_SHA256 = '00e887f627648ebf8fb934e4a2c99eff5642535ab047f7e898c2db64bd822dbd'

class Drawing(Sub32):
    icon_id = 'equalizer-cb9c3492-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'audio'
    categories = ('audio', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 2), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (11, 6), (11, 26))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 21), (21, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 20), (2, 14))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
