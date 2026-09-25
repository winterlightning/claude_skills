"""Independent 32px profile of cat-head-nose-line.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '49e8644a-0ad0-4afd-af3d-44a58e035850'
SOURCE_PATH = 'pictographic-primitives/pets/cat head_49e8644a-0ad0-4afd-af3d-44a58e035850.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('49e8644a-0ad0-4afd-af3d-44a58e035850', 'pictographic-primitives/pets/cat head_49e8644a-0ad0-4afd-af3d-44a58e035850.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cat-head-nose-line',)
SOLO_SOURCE_ICON_IDS = ('cat-head-nose-line',)
REFERENCE_EXPORT_SHA256 = '76505d0950010f860b3d323ffc368efc5389a8a3d0eabd3174ab4e63d090eb1f'

class Drawing(Sub32):
    icon_id = 'cat-head-nose-line-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'pets'
    categories = ('pets', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (10, 8))
        self.add_line('p1-r1-3', (10, 8), (22, 8))
        self.add_line('p1-r1-4', (22, 8), (30, 2))
        self.add_line('p1-r1-5', (30, 2), (30, 16))
        self.add_arc('p1-r1-6', (30, 16), (16, 30), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-7', (16, 30), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (10, 16), (10, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 16), (22, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (14, 22), (18, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 22), (16, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p1-r1-6', 'p5-r1-1')
        self.relate("connect", 'p1-r1-7', 'p5-r1-1')
