"""Independent 32px profile of controls-previous-video.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd97ce210-8c87-47ca-ad69-8c331dcbc800'
SOURCE_PATH = 'pictographic-primitives/video/controls previous_d97ce210-8c87-47ca-ad69-8c331dcbc800.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d97ce210-8c87-47ca-ad69-8c331dcbc800', 'pictographic-primitives/video/controls previous_d97ce210-8c87-47ca-ad69-8c331dcbc800.svg'),)
PROFILE_SOURCE_KEYS = ('solo/controls-previous-video',)
SOLO_SOURCE_ICON_IDS = ('controls-previous-video',)
REFERENCE_EXPORT_SHA256 = '99e5a6c9075921a8707958112c11ba55694e760744edffbb45af74de8ca8dc55'

class Drawing(Sub32):
    icon_id = 'controls-previous-video-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'video'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (5, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (27, 3), (27, 29))
        self.add_line('p2-r1-2', (27, 29), (11, 17))
        self.add_line('p2-r1-3', (11, 17), (10, 16))
        self.add_line('p2-r1-4', (10, 16), (27, 3))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
