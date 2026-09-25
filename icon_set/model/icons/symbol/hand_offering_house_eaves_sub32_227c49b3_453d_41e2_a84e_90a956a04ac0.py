"""Independent 32px profile of hand-offering-house-eaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '227c49b3-453d-41e2-a84e-90a956a04ac0'
SOURCE_PATH = 'pictographic-primitives/symbol/give hand with house_227c49b3-453d-41e2-a84e-90a956a04ac0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('227c49b3-453d-41e2-a84e-90a956a04ac0', 'pictographic-primitives/symbol/give hand with house_227c49b3-453d-41e2-a84e-90a956a04ac0.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-offering-house-eaves',)
SOLO_SOURCE_ICON_IDS = ('hand-offering-house-eaves',)
REFERENCE_EXPORT_SHA256 = '54ad0f91540c96948f3193918656670bd81594c88b9566b708b3f527f5e96d73'

class Drawing(Sub32):
    icon_id = 'hand-offering-house-eaves-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 21), (11, 21))
        self.add_bezier('p1-r1-2', (11, 21), ((12, 21), (13, 21), (14, 22)))
        self.add_bezier('p1-r1-3', (14, 22), ((14, 22), (14, 23), (14, 24)))
        self.add_bezier('p1-r1-4', (14, 24), ((14, 25), (14, 25), (14, 26)))
        self.add_bezier('p1-r1-5', (14, 26), ((13, 27), (12, 27), (11, 27)))
        self.add_line('p1-r1-6', (11, 27), (8, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (14, 24), (26, 18))
        self.add_bezier('p2-r1-2', (26, 18), ((28, 18), (30, 19), (30, 21)))
        self.add_bezier('p2-r1-3', (30, 21), ((30, 24), (28, 25), (26, 25)))
        self.add_line('p2-r1-4', (26, 25), (21, 28))
        self.add_bezier('p2-r1-5', (21, 28), ((19, 29), (18, 30), (16, 30)))
        self.add_bezier('p2-r1-6', (16, 30), ((14, 30), (13, 29), (11, 28)))
        self.add_line('p2-r1-7', (11, 28), (2, 25))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (10, 12), (10, 7))
        self.add_line('p3-r1-2', (10, 7), (16, 2))
        self.add_line('p3-r1-3', (16, 2), (22, 7))
        self.add_line('p3-r1-4', (22, 7), (22, 12))
        self.add_line('p3-r1-5', (22, 12), (10, 12))
        self.add_line('p3-r1-6', (10, 12), (10, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (10, 7), (7, 9))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 7), (25, 9))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p5-r1-1')
        self.relate('connect', 'p3-r1-4', 'p5-r1-1')
