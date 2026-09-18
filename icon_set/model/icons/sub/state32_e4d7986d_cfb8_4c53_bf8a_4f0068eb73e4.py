"""Independent 32px profile of state32-e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4'
SOURCE_PATH = 'icon_set/assets/combination-state32/e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4', 'icon_set/assets/combination-state32/e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '852bfe78dab491f90267233e91c8ca1a3a1fb3b823b94cc6b0864860ab436d07'

class Drawing(Sub32):
    icon_id = 'state32-e4d7986d-cfb8-4c53-bf8a-4f0068eb73e4'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 20), (23, 20))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (13, 20), (13, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 20), (16, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (19, 20), (19, 9))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p5-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
