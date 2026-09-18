"""Independent 32px profile of lines-and-small-rectangle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '25e17989-6e72-4275-91e0-9c3a9bf1e98b'
SOURCE_PATH = 'pictographic-primitives/symbol/lines and small rectangle_25e17989-6e72-4275-91e0-9c3a9bf1e98b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('25e17989-6e72-4275-91e0-9c3a9bf1e98b', 'pictographic-primitives/symbol/lines and small rectangle_25e17989-6e72-4275-91e0-9c3a9bf1e98b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lines-and-small-rectangle',)
SOLO_SOURCE_ICON_IDS = ('lines-and-small-rectangle',)
REFERENCE_EXPORT_SHA256 = '6731f9002ce451d2d0e1dd356c36329b9dc8cc09a22c0477dbf979b313e3a3c9'

class Drawing(Sub32):
    icon_id = 'lines-and-small-rectangle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 7), (30, 7))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (21, 25), (30, 25))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (13, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 11))
        self.add_line('p3-r1-3', (2, 11), (13, 11))
        self.add_line('p3-r1-4', (13, 11), (13, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (13, 21), (2, 21))
        self.add_line('p4-r1-2', (2, 21), (2, 30))
        self.add_line('p4-r1-3', (2, 30), (13, 30))
        self.add_line('p4-r1-4', (13, 30), (13, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
