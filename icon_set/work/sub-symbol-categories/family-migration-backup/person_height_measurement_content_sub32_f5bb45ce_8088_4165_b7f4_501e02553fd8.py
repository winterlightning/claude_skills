"""Independent 32px profile of person-height-measurement-content.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f5bb45ce-8088-4165-b7f4-501e02553fd8'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/f5bb45ce-8088-4165-b7f4-501e02553fd8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f5bb45ce-8088-4165-b7f4-501e02553fd8', 'icon_set/dist/gallery/combination-originals/f5bb45ce-8088-4165-b7f4-501e02553fd8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-height-measurement-content',)
SOLO_SOURCE_ICON_IDS = ('person-height-measurement-content',)
REFERENCE_EXPORT_SHA256 = 'a99885c9422a4734cb047d6cc537452d9a9d3246d7342246898e52f1b93dfcac'

class Drawing(Sub32):
    icon_id = 'person-height-measurement-content-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2), (7, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 11), (7, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (7, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (7, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (18, 6), (26, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p6-r1-2', (26, 6), (18, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (22, 16), (22, 22))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (14, 16), (22, 16))
        self.add_line('p8-r1-2', (22, 16), (30, 16))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.add_line('p9-r1-1', (16, 30), (22, 22))
        self.add_line('p9-r1-2', (22, 22), (28, 30))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p5-r1-1')
        self.relate("connect", 'p7-r1-1', 'p8-r1-1')
        self.relate("connect", 'p7-r1-1', 'p8-r1-2')
        self.relate("connect", 'p7-r1-1', 'p9-r1-1')
        self.relate("connect", 'p7-r1-1', 'p9-r1-2')
