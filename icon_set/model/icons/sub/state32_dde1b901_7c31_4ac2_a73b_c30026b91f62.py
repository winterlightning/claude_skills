"""Independent 32px profile of state32-dde1b901-7c31-4ac2-a73b-c30026b91f62.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dde1b901-7c31-4ac2-a73b-c30026b91f62'
SOURCE_PATH = 'icon_set/assets/combination-state32/dde1b901-7c31-4ac2-a73b-c30026b91f62.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dde1b901-7c31-4ac2-a73b-c30026b91f62', 'icon_set/assets/combination-state32/dde1b901-7c31-4ac2-a73b-c30026b91f62.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'aca4bb3c9659c2d19565388c2a8fbe60efcfcf3891b20c75163324e028d13cc0'

class Drawing(Sub32):
    icon_id = 'state32-dde1b901-7c31-4ac2-a73b-c30026b91f62'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (4, 19), ((4, 17), (3, 16), (3, 15)))
        self.add_bezier('p1-r1-2', (3, 15), ((3, 8), (10, 3), (16, 3)))
        self.add_bezier('p1-r1-3', (16, 3), ((20, 3), (24, 5), (26, 8)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p1-r2-1', (26, 2), (26, 8))
        self.add_line('p1-r2-2', (26, 8), (21, 8))
        self.add_contour('path-1-2', 'p1-r2-1', 'p1-r2-2', closed=False)
        self.add_bezier('p1-r3-1', (28, 13), ((28, 15), (29, 16), (29, 17)))
        self.add_bezier('p1-r3-2', (29, 17), ((29, 24), (22, 29), (16, 29)))
        self.add_bezier('p1-r3-3', (16, 29), ((12, 29), (8, 27), (6, 24)))
        self.add_contour('path-1-3', 'p1-r3-1', 'p1-r3-2', 'p1-r3-3', closed=False)
        self.add_line('p1-r4-1', (6, 30), (6, 24))
        self.add_line('p1-r4-2', (6, 24), (11, 24))
        self.add_contour('path-1-4', 'p1-r4-1', 'p1-r4-2', closed=False)
        self.relate("connect", 'p1-r1-3', 'p1-r2-1')
        self.relate("connect", 'p1-r1-3', 'p1-r2-2')
        self.relate("connect", 'p1-r3-3', 'p1-r4-1')
        self.relate("connect", 'p1-r3-3', 'p1-r4-2')
