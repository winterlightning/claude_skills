"""Independent 32px profile of arrow-thick-left-bottom.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a775dedd-1db8-48f1-b439-a15c9436b0d2'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow thick left bottom_a775dedd-1db8-48f1-b439-a15c9436b0d2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a775dedd-1db8-48f1-b439-a15c9436b0d2', 'pictographic-primitives/symbol/arrow thick left bottom_a775dedd-1db8-48f1-b439-a15c9436b0d2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-thick-left-bottom',)
SOLO_SOURCE_ICON_IDS = ('arrow-thick-left-bottom',)
REFERENCE_EXPORT_SHA256 = 'c8df3f6a64d800c007b941d601d2728792bd21a8ff7a01a06786fe959ddbad88'

class Drawing(Sub32):
    icon_id = 'arrow-thick-left-bottom-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (23, 30), (16, 24))
        self.add_line('p1-r1-2', (16, 24), (30, 10))
        self.add_line('p1-r1-3', (30, 10), (22, 2))
        self.add_line('p1-r1-4', (22, 2), (8, 16))
        self.add_line('p1-r1-5', (8, 16), (2, 10))
        self.add_line('p1-r1-6', (2, 10), (2, 30))
        self.add_line('p1-r1-7', (2, 30), (23, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
