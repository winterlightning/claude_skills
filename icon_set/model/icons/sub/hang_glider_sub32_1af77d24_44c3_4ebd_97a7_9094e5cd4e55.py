"""Independent 32px profile of hang-glider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1af77d24-44c3-4ebd-97a7-9094e5cd4e55'
SOURCE_PATH = 'pictographic-primitives/animals/fly_1af77d24-44c3-4ebd-97a7-9094e5cd4e55.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1af77d24-44c3-4ebd-97a7-9094e5cd4e55', 'pictographic-primitives/animals/fly_1af77d24-44c3-4ebd-97a7-9094e5cd4e55.svg'), ('c154bd5e-85cc-4682-977f-bac1bfee4f64', 'pictographic-primitives/animals/fly_c154bd5e-85cc-4682-977f-bac1bfee4f64.svg'))
PROFILE_SOURCE_KEYS = ('solo/hang-glider', 'solo/hang-glider-with-harness')
SOLO_SOURCE_ICON_IDS = ('hang-glider', 'hang-glider-with-harness')
REFERENCE_EXPORT_SHA256 = '8af35c4515fbf2960523b2057f0128f30f6f21bc95e75a45d47415fef7a08c2f'

class Drawing(Sub32):
    icon_id = 'hang-glider-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/sports'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 5), (3, 16))
        self.add_bezier('p1-r1-2', (3, 16), ((2, 17), (2, 19), (2, 20)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (2, 20), (10, 19))
        self.add_line('p2-r1-2', (10, 19), (16, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 17), (22, 19))
        self.add_line('p3-r1-2', (22, 19), (30, 20))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_bezier('p4-r1-1', (30, 20), ((30, 19), (30, 17), (29, 16)))
        self.add_line('p4-r1-2', (29, 16), (16, 5))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (10, 19), (13, 27))
        self.add_line('p5-r1-2', (13, 27), (20, 27))
        self.add_line('p5-r1-3', (20, 27), (22, 19))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p4-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p5-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p5-r1-1')
        self.relate("connect", 'p3-r1-1', 'p5-r1-3')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p5-r1-3')
