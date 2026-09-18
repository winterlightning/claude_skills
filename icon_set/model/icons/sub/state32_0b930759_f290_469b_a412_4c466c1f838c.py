"""Independent 32px profile of state32-0b930759-f290-469b-a412-4c466c1f838c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0b930759-f290-469b-a412-4c466c1f838c'
SOURCE_PATH = 'icon_set/assets/combination-state32/0b930759-f290-469b-a412-4c466c1f838c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0b930759-f290-469b-a412-4c466c1f838c', 'icon_set/assets/combination-state32/0b930759-f290-469b-a412-4c466c1f838c.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'd1dced64de7b81ce2889ea951894aaf596a54642b3a0f841495db8fcff0aecc9'

class Drawing(Sub32):
    icon_id = 'state32-0b930759-f290-469b-a412-4c466c1f838c'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 8), (25, 8))
        self.add_bezier('p1-r1-2', (25, 8), ((27.666666666666668, 8), (29, 9.333333333333334), (29, 12)))
        self.add_line('p1-r1-3', (29, 12), (29, 24))
        self.add_bezier('p1-r1-4', (29, 24), ((29, 26.666666666666668), (27.666666666666668, 28), (25, 28)))
        self.add_line('p1-r1-5', (25, 28), (7, 28))
        self.add_bezier('p1-r1-6', (7, 28), ((4.333333333333334, 28), (3, 26.666666666666668), (3, 24)))
        self.add_line('p1-r1-7', (3, 24), (3, 12))
        self.add_bezier('p1-r1-8', (3, 12), ((3, 9.333333333333334), (4.333333333333334, 8), (7, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (11, 8), (11, 2))
        self.add_line('p2-r1-2', (11, 2), (21, 2))
        self.add_line('p2-r1-3', (21, 2), (21, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p2-r2-1', (8, 28), (8, 30))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
        self.add_line('p2-r3-1', (24, 28), (24, 30))
        self.add_contour('path-2-3', 'p2-r3-1', closed=False)
