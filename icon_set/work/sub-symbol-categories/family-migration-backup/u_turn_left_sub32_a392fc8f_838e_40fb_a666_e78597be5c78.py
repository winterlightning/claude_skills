"""Independent 32px profile of u-turn-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a392fc8f-838e-40fb-a666-e78597be5c78'
SOURCE_PATH = 'pictographic-primitives/transportation/u turn left_a392fc8f-838e-40fb-a666-e78597be5c78.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a392fc8f-838e-40fb-a666-e78597be5c78', 'pictographic-primitives/transportation/u turn left_a392fc8f-838e-40fb-a666-e78597be5c78.svg'),)
PROFILE_SOURCE_KEYS = ('solo/u-turn-left',)
SOLO_SOURCE_ICON_IDS = ('u-turn-left',)
REFERENCE_EXPORT_SHA256 = 'c6ecdc90e372546a16237d02ed993a4211eb4fb0ff76e4fe34bed3e7c5154246'

class Drawing(Sub32):
    icon_id = 'u-turn-left-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 30), (30, 13))
        self.add_arc('p1-r1-2', (30, 13), (8, 13), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (8, 13), (8, 24))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 18), (8, 24))
        self.add_line('p2-r1-2', (8, 24), (14, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
