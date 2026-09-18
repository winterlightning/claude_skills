"""Independent 32px profile of grid-cross-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9df1cf27-f581-44da-8016-6680a5b4805c'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/9df1cf27-f581-44da-8016-6680a5b4805c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9df1cf27-f581-44da-8016-6680a5b4805c', 'icon_set/dist/gallery/combination-originals/9df1cf27-f581-44da-8016-6680a5b4805c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/grid-cross-content',)
SOLO_SOURCE_ICON_IDS = ('grid-cross-content',)
REFERENCE_EXPORT_SHA256 = 'd203621ffa42c93c619cbef485c8ff5af123f02ea155feeb76e5cbb293dd378b'

class Drawing(Sub32):
    icon_id = 'grid-cross-content-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 5), (2, 5))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 16), (2, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 27), (2, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 5), (13, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (13, 16), (13, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (13, 27), (13, 27))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (22, 12), (26, 16))
        self.add_line('p7-r1-2', (26, 16), (30, 20))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.add_line('p8-r1-1', (22, 20), (26, 16))
        self.add_line('p8-r1-2', (26, 16), (30, 12))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.relate("connect", 'p7-r1-1', 'p8-r1-1')
        self.relate("connect", 'p7-r1-1', 'p8-r1-2')
        self.relate("connect", 'p7-r1-2', 'p8-r1-1')
        self.relate("connect", 'p7-r1-2', 'p8-r1-2')
