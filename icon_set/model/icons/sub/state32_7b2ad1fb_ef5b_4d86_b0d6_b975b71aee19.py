"""Independent 32px profile of state32-7b2ad1fb-ef5b-4d86-b0d6-b975b71aee19.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7b2ad1fb-ef5b-4d86-b0d6-b975b71aee19'
SOURCE_PATH = 'icon_set/assets/combination-state32/7b2ad1fb-ef5b-4d86-b0d6-b975b71aee19.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b2ad1fb-ef5b-4d86-b0d6-b975b71aee19', 'icon_set/assets/combination-state32/7b2ad1fb-ef5b-4d86-b0d6-b975b71aee19.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'cdd5329a119498e500439c5fca9a30c73d2c52b1c8212ae4c43ae72feef8279e'

class Drawing(Sub32):
    icon_id = 'state32-7b2ad1fb-ef5b-4d86-b0d6-b975b71aee19'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (16, 7), ((14, 4), (11, 3), (8, 3)))
        self.add_bezier('p1-r1-2', (8, 3), ((5, 3), (2, 6), (2, 10)))
        self.add_bezier('p1-r1-3', (2, 10), ((2, 16), (9, 22), (16, 29)))
        self.add_bezier('p1-r1-4', (16, 29), ((23, 22), (30, 16), (30, 10)))
        self.add_bezier('p1-r1-5', (30, 10), ((30, 6), (27, 3), (24, 3)))
        self.add_bezier('p1-r1-6', (24, 3), ((21, 3), (18, 4), (16, 7)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (2, 13), (30, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 22), (23, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
