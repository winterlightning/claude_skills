"""Independent 32px profile of cuffless-thumbs-up.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c0076a7e-cfe2-459e-9680-ec515e78c5df'
SOURCE_PATH = 'pictographic-primitives/social/like_c0076a7e-cfe2-459e-9680-ec515e78c5df.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c0076a7e-cfe2-459e-9680-ec515e78c5df', 'pictographic-primitives/social/like_c0076a7e-cfe2-459e-9680-ec515e78c5df.svg'), ('fc83794c-c4dc-4f7e-884b-9c85a97943ce', 'pictographic-primitives/social/like_fc83794c-c4dc-4f7e-884b-9c85a97943ce.svg'))
PROFILE_SOURCE_KEYS = ('solo/cuffless-thumbs-up', 'solo/curled-finger-thumbs-up')
SOLO_SOURCE_ICON_IDS = ('cuffless-thumbs-up', 'curled-finger-thumbs-up')
REFERENCE_EXPORT_SHA256 = 'c43ed24de1c8e617e6603efad1c2ec5f6d9fef6218b46362bdd0eb579438016a'

class Drawing(Sub32):
    icon_id = 'cuffless-thumbs-up-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'social'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (8, 16))
        self.add_line('p1-r1-2', (8, 16), (16, 8))
        self.add_line('p1-r1-3', (16, 8), (16, 2))
        self.add_arc('p1-r1-4', (16, 2), (22, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (22, 8), (20, 16))
        self.add_line('p1-r1-6', (20, 16), (27, 16))
        self.add_arc('p1-r1-7', (27, 16), (30, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (30, 19), (30, 27))
        self.add_arc('p1-r1-9', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-10', (27, 30), (8, 30))
        self.add_line('p1-r1-11', (8, 30), (2, 30))
        self.add_line('p1-r1-12', (2, 30), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
