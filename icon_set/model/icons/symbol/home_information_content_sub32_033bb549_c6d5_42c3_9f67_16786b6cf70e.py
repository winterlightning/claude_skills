"""Independent 32px profile of home-information-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '033bb549-c6d5-42c3-9f67-16786b6cf70e'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/033bb549-c6d5-42c3-9f67-16786b6cf70e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('033bb549-c6d5-42c3-9f67-16786b6cf70e', 'icon_set/dist/gallery/combination-originals/033bb549-c6d5-42c3-9f67-16786b6cf70e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/home-information-content',)
SOLO_SOURCE_ICON_IDS = ('home-information-content',)
REFERENCE_EXPORT_SHA256 = '73ceb1f0cb4c376204885421cc35b32d692362040560582dab746a1e541a706b'

class Drawing(Sub32):
    icon_id = 'home-information-content-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 12), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (27, 12))
        self.add_line('p1-r1-3', (27, 12), (27, 19))
        self.add_line('p1-r1-4', (27, 19), (5, 19))
        self.add_line('p1-r1-5', (5, 19), (5, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5, 24), (22, 24))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 30), (27, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
