"""Independent 32px profile of circular-diverging-arrows-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '94ff1421-50cb-4e9c-918c-422ba8141be2'
SOURCE_PATH = 'pictographic-primitives/other/circle split arrow_94ff1421-50cb-4e9c-918c-422ba8141be2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('94ff1421-50cb-4e9c-918c-422ba8141be2', 'pictographic-primitives/other/circle split arrow_94ff1421-50cb-4e9c-918c-422ba8141be2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circular-diverging-arrows-solo',)
SOLO_SOURCE_ICON_IDS = ('circular-diverging-arrows-solo',)
REFERENCE_EXPORT_SHA256 = '27474575b3eee891d07b569f1a61abaf62fc2fa68cd225fb37edf54f84cd86ec'

class Drawing(Sub32):
    icon_id = 'circular-diverging-arrows-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (16, 23), ((16, 16), (13, 13), (10, 10)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (16, 23), ((16, 16), (19, 13), (22, 10)))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (10, 15), (10, 10))
        self.add_line('p4-r1-2', (10, 10), (15, 10))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (17, 10), (22, 10))
        self.add_line('p5-r1-2', (22, 10), (22, 15))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-1')
        self.relate("connect", 'p2-r1-1', 'p4-r1-2')
        self.relate("connect", 'p3-r1-1', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-2')
