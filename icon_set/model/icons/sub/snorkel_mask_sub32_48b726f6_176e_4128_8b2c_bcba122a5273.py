"""Independent 32px profile of snorkel-mask.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '48b726f6-176e-4128-8b2c-bcba122a5273'
SOURCE_PATH = 'pictographic-primitives/symbol/snorkel_48b726f6-176e-4128-8b2c-bcba122a5273.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('48b726f6-176e-4128-8b2c-bcba122a5273', 'pictographic-primitives/symbol/snorkel_48b726f6-176e-4128-8b2c-bcba122a5273.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snorkel-mask',)
SOLO_SOURCE_ICON_IDS = ('snorkel-mask',)
REFERENCE_EXPORT_SHA256 = '532b9acb3f059911594abad5deef8662f4576c826d2f6571c650b5f4b831df1c'

class Drawing(Sub32):
    icon_id = 'snorkel-mask-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 7), (18, 7))
        self.add_arc('p1-r1-2', (18, 7), (18, 16), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (18, 16), (15, 16))
        self.add_line('p1-r1-4', (15, 16), (13, 13))
        self.add_line('p1-r1-5', (13, 13), (11, 13))
        self.add_line('p1-r1-6', (11, 13), (9, 16))
        self.add_line('p1-r1-7', (9, 16), (7, 16))
        self.add_arc('p1-r1-8', (7, 16), (7, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (30, 2), (30, 20))
        self.add_arc('p2-r1-2', (30, 20), (22, 28), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (22, 28), (18, 28))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (14, 28), (18, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (18, 28), (14, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-2')
