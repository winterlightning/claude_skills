"""Independent 32px profile of tombstone-with-t-shaped-engraving-batch-014-09.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'd26441e3-9384-56ce-a3fa-339ff35c82bb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/halloween graveyard_d26441e3-9384-56ce-a3fa-339ff35c82bb.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d26441e3-9384-56ce-a3fa-339ff35c82bb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/halloween graveyard_d26441e3-9384-56ce-a3fa-339ff35c82bb.svg'), ('d639010e-7131-46d6-b3fa-028d7353a5b9', 'icon_set/dist/gallery/combination-originals/d639010e-7131-46d6-b3fa-028d7353a5b9.svg'))
PROFILE_SOURCE_KEYS = ('solo/tombstone-with-t-shaped-engraving-batch-014-09',)
SOLO_SOURCE_ICON_IDS = ('tombstone-with-t-shaped-engraving-batch-014-09',)
REFERENCE_EXPORT_SHA256 = 'eac51090dcca8def05fc906a6fddd9edfe9e02601b9140785a2d81f19131ef67'

class Drawing(Sub32):
    icon_id = 'tombstone-with-t-shaped-engraving-batch-014-09-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 30), (8, 10))
        self.add_arc('p1-r1-2', (8, 10), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (24, 10), (24, 30))
        self.add_line('p1-r1-4', (24, 30), (8, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (5, 30), (8, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 30), (27, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 11), (16, 20))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (14, 14), (18, 14))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
