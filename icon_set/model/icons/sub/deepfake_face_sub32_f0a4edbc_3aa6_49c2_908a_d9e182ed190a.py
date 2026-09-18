"""Independent 32px profile of deepfake-face.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f0a4edbc-3aa6-49c2-908a-d9e182ed190a'
SOURCE_PATH = 'pictographic-primitives/symbol/deep fake_f0a4edbc-3aa6-49c2-908a-d9e182ed190a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f0a4edbc-3aa6-49c2-908a-d9e182ed190a', 'pictographic-primitives/symbol/deep fake_f0a4edbc-3aa6-49c2-908a-d9e182ed190a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/deepfake-face',)
SOLO_SOURCE_ICON_IDS = ('deepfake-face',)
REFERENCE_EXPORT_SHA256 = '96aca030dc9e0bba6e269d766dba0eabf78e5840774642a171fea63aac10b37e'

class Drawing(Sub32):
    icon_id = 'deepfake-face-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 2), (16, 2))
        self.add_line('p1-r1-2', (16, 2), (20, 2))
        self.add_arc('p1-r1-3', (20, 2), (27, 9), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (27, 9), (27, 13))
        self.add_line('p1-r1-5', (27, 13), (27, 19))
        self.add_arc('p1-r1-6', (27, 19), (16, 30), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (16, 30), (5, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (5, 19), (5, 13))
        self.add_line('p1-r1-9', (5, 13), (5, 9))
        self.add_arc('p1-r1-10', (5, 9), (12, 2), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (5, 13), (16, 13))
        self.add_line('p2-r1-2', (16, 13), (27, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 13))
        self.add_line('p3-r1-2', (16, 13), (16, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (20, 22), (12, 22), radius_x=4, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-8', 'p2-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
