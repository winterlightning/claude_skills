"""Independent 32px profile of pdf-trefoil-logo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e5772ae5-6260-4859-a6ab-c6216f211330'
SOURCE_PATH = 'pictographic-primitives/symbol/adobe_e5772ae5-6260-4859-a6ab-c6216f211330.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e5772ae5-6260-4859-a6ab-c6216f211330', 'pictographic-primitives/symbol/adobe_e5772ae5-6260-4859-a6ab-c6216f211330.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pdf-trefoil-logo',)
SOLO_SOURCE_ICON_IDS = ('pdf-trefoil-logo',)
REFERENCE_EXPORT_SHA256 = '58475180f353284e85c41e9df1455f355becca08ca70cc4d1356822eb7cbd1f3'

class Drawing(Sub32):
    icon_id = 'pdf-trefoil-logo-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 21), (16, 11))
        self.add_line('p1-r1-2', (16, 11), (22, 18))
        self.add_line('p1-r1-3', (22, 18), (11, 21))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (16, 11), (11, 5))
        self.add_arc('p2-r1-2', (11, 5), (19, 5), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (19, 5), (16, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (11, 21), (5, 30))
        self.add_arc('p3-r1-2', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (2, 27), (5, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (5, 24), (11, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (22, 18), (27, 16))
        self.add_arc('p4-r1-2', (27, 16), (30, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('p4-r1-3', (30, 19), (27, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p4-r1-4', (27, 22), (22, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-1', 'p3-r1-4')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-4')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-4')
        self.relate("connect", 'p1-r1-3', 'p4-r1-1')
        self.relate("connect", 'p1-r1-3', 'p4-r1-4')
