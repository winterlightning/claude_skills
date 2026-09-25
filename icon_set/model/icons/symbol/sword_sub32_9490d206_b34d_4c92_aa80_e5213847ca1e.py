"""Independent 32px profile of sword.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '9490d206-b34d-4c92-aa80-e5213847ca1e'
SOURCE_PATH = 'pictographic-primitives/video-games/sword_9490d206-b34d-4c92-aa80-e5213847ca1e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9490d206-b34d-4c92-aa80-e5213847ca1e', 'pictographic-primitives/video-games/sword_9490d206-b34d-4c92-aa80-e5213847ca1e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sword',)
SOLO_SOURCE_ICON_IDS = ('sword',)
REFERENCE_EXPORT_SHA256 = 'd25eb78ce0e9d80a18679aa91b3a8e460d5dedf37b14f565e957dbec65710772'

class Drawing(Sub32):
    icon_id = 'sword-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'video-games'
    categories = ('video-games', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 30), (21, 21))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (28, 14), (14, 28))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 18), (12, 4))
        self.add_line('p3-r1-2', (12, 4), (11, 4))
        self.add_line('p3-r1-3', (11, 4), (2, 2))
        self.add_line('p3-r1-4', (2, 2), (4, 11))
        self.add_line('p3-r1-5', (4, 11), (4, 12))
        self.add_line('p3-r1-6', (4, 12), (19, 24))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
