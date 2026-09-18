"""Independent 32px profile of arrow-trend-up.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3d84de66-b548-49ba-a6cb-614bce76c814'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow trend up_3d84de66-b548-49ba-a6cb-614bce76c814.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3d84de66-b548-49ba-a6cb-614bce76c814', 'pictographic-primitives/symbol/arrow trend up_3d84de66-b548-49ba-a6cb-614bce76c814.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-trend-up',)
SOLO_SOURCE_ICON_IDS = ('arrow-trend-up',)
REFERENCE_EXPORT_SHA256 = '6860be3555adaf6a946a60752e12c0fefa1a1fd86f413be0f8f0ed972c3c82b3'

class Drawing(Sub32):
    icon_id = 'arrow-trend-up-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (23, 5), (30, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 27), (13, 13))
        self.add_line('p2-r1-2', (13, 13), (19, 22))
        self.add_line('p2-r1-3', (19, 22), (30, 5))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (30, 16), (30, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
