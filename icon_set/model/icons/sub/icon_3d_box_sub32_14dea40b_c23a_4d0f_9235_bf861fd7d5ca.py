"""Independent 32px profile of icon-3d-box.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '14dea40b-c23a-4d0f-9235-bf861fd7d5ca'
SOURCE_PATH = 'pictographic-primitives/symbol/3d box_14dea40b-c23a-4d0f-9235-bf861fd7d5ca.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14dea40b-c23a-4d0f-9235-bf861fd7d5ca', 'pictographic-primitives/symbol/3d box_14dea40b-c23a-4d0f-9235-bf861fd7d5ca.svg'),)
PROFILE_SOURCE_KEYS = ('solo/icon-3d-box',)
SOLO_SOURCE_ICON_IDS = ('icon-3d-box',)
REFERENCE_EXPORT_SHA256 = '8ba15747e748d7d8372fe617a3e175a1ecb67342ac2ed14850f5d73b4793a0e0'

class Drawing(Sub32):
    icon_id = 'icon-3d-box-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 30), (27, 23))
        self.add_line('p1-r1-2', (27, 23), (27, 9))
        self.add_line('p1-r1-3', (27, 9), (16, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (27, 9), (16, 2))
        self.add_line('p2-r1-2', (16, 2), (5, 9))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 16), (16, 30))
        self.add_line('p3-r1-2', (16, 30), (5, 23))
        self.add_line('p3-r1-3', (5, 23), (5, 9))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (16, 16), (5, 9))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-3')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
