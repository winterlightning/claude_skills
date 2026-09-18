"""Independent 32px profile of herbal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd37ff2bf-eddb-475b-9f5a-3996767a114d'
SOURCE_PATH = 'pictographic-primitives/symbol/herbal_d37ff2bf-eddb-475b-9f5a-3996767a114d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d37ff2bf-eddb-475b-9f5a-3996767a114d', 'pictographic-primitives/symbol/herbal_d37ff2bf-eddb-475b-9f5a-3996767a114d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/herbal',)
SOLO_SOURCE_ICON_IDS = ('herbal',)
REFERENCE_EXPORT_SHA256 = 'bbce1cd34b72c14ac338e4e66ce83598096f5019d740ff075195bedf54d8623f'

class Drawing(Sub32):
    icon_id = 'herbal-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 2), (21, 11))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (13, 5), (13, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 14), (5, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (5, 27))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (19, 27), (5, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (27, 19), (13, 19))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (30, 11), (21, 11))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (27, 7), (21, 11))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (21, 11), (13, 19))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_line('p10-r1-1', (13, 19), (5, 27))
        self.add_contour('path-10-1', 'p10-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p7-r1-1')
        self.relate("connect", 'p1-r1-1', 'p8-r1-1')
        self.relate("connect", 'p1-r1-1', 'p9-r1-1')
        self.relate("connect", 'p2-r1-1', 'p6-r1-1')
        self.relate("connect", 'p2-r1-1', 'p9-r1-1')
        self.relate("connect", 'p2-r1-1', 'p10-r1-1')
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p10-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-1', 'p10-r1-1')
        self.relate("connect", 'p5-r1-1', 'p10-r1-1')
        self.relate("connect", 'p6-r1-1', 'p9-r1-1')
        self.relate("connect", 'p6-r1-1', 'p10-r1-1')
        self.relate("connect", 'p7-r1-1', 'p8-r1-1')
        self.relate("connect", 'p7-r1-1', 'p9-r1-1')
        self.relate("connect", 'p8-r1-1', 'p9-r1-1')
        self.relate("connect", 'p9-r1-1', 'p10-r1-1')
