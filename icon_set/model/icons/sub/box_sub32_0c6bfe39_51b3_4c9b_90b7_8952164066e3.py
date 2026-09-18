"""Independent 32px profile of box.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0c6bfe39-51b3-4c9b-90b7-8952164066e3'
SOURCE_PATH = 'pictographic-primitives/shipping/box_0c6bfe39-51b3-4c9b-90b7-8952164066e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0c6bfe39-51b3-4c9b-90b7-8952164066e3', 'pictographic-primitives/shipping/box_0c6bfe39-51b3-4c9b-90b7-8952164066e3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/box',)
SOLO_SOURCE_ICON_IDS = ('box',)
REFERENCE_EXPORT_SHA256 = '1c2eeb03e4b8281eab57c4832039e915060e1b001c18cca27601c09ee46742db'

class Drawing(Sub32):
    icon_id = 'box-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'shipping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 11), (10, 2))
        self.add_line('p1-r1-2', (10, 2), (16, 2))
        self.add_line('p1-r1-3', (16, 2), (22, 2))
        self.add_line('p1-r1-4', (22, 2), (30, 11))
        self.add_line('p1-r1-5', (30, 11), (30, 30))
        self.add_line('p1-r1-6', (30, 30), (2, 30))
        self.add_line('p1-r1-7', (2, 30), (2, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (2, 11), (16, 11))
        self.add_line('p2-r1-2', (16, 11), (30, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 11))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-7', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
