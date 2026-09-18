"""Independent 32px profile of plus-minus-mathematical-sign-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7adfa015-1e70-4aa5-a35c-0902119d672c'
SOURCE_PATH = 'pictographic-primitives/other/circle plus minus_7adfa015-1e70-4aa5-a35c-0902119d672c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7adfa015-1e70-4aa5-a35c-0902119d672c', 'pictographic-primitives/other/circle plus minus_7adfa015-1e70-4aa5-a35c-0902119d672c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/plus-minus-mathematical-sign-solo',)
SOLO_SOURCE_ICON_IDS = ('plus-minus-mathematical-sign-solo',)
REFERENCE_EXPORT_SHA256 = 'aa2095a0d08ddb7850de28a17e9ed9c92085ba2a4dc15064d4a5f0d1a4faf854'

class Drawing(Sub32):
    icon_id = 'plus-minus-mathematical-sign-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (10, 11), (11, 11))
        self.add_line('p2-r1-2', (11, 11), (13, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (11, 10), (11, 11))
        self.add_line('p3-r1-2', (11, 11), (11, 13))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (10, 22), (22, 10))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (20, 21), (22, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
