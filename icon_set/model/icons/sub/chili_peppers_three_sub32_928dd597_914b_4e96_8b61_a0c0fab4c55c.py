"""Independent 32px profile of chili-peppers-three.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '928dd597-914b-4e96-8b61-a0c0fab4c55c'
SOURCE_PATH = 'pictographic-primitives/symbol/three chilies_928dd597-914b-4e96-8b61-a0c0fab4c55c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('928dd597-914b-4e96-8b61-a0c0fab4c55c', 'pictographic-primitives/symbol/three chilies_928dd597-914b-4e96-8b61-a0c0fab4c55c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/chili-peppers-three',)
SOLO_SOURCE_ICON_IDS = ('chili-peppers-three',)
REFERENCE_EXPORT_SHA256 = 'd0c2b34b6b095d42ff727be1b01fd5394b486e06a726d35ae5c88ce8ea7f9036'

class Drawing(Sub32):
    icon_id = 'chili-peppers-three-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (25, 2))
        self.add_bezier('p1-r1-2', (25, 2), ((26, 2), (27, 2), (27, 3)))
        self.add_bezier('p1-r1-3', (27, 3), ((27, 3), (28, 4), (28, 4)))
        self.add_arc('p1-r1-4', (28, 4), (25, 7), radius_x=2.1213203435596424, radius_y=2.1213203435596424, large_arc=False, sweep=True)
        self.add_arc('p1-r1-5', (25, 7), (2, 2), radius_x=23, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (28, 4), (30, 4))
        self.add_line('p2-r1-2', (30, 4), (30, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 14), (25, 14))
        self.add_arc('p3-r1-2', (25, 14), (28, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (28, 16), (25, 18), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (25, 18), (2, 14), radius_x=23, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (28, 16), (30, 16))
        self.add_line('p4-r1-2', (30, 16), (30, 14))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 25), (25, 25))
        self.add_arc('p5-r1-2', (25, 25), (28, 28), radius_x=2.1213203435596424, radius_y=2.1213203435596424, large_arc=False, sweep=True)
        self.add_bezier('p5-r1-3', (28, 28), ((28, 28), (27, 29), (27, 29)))
        self.add_bezier('p5-r1-4', (27, 29), ((27, 30), (26, 30), (25, 30)))
        self.add_arc('p5-r1-5', (25, 30), (2, 25), radius_x=23, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (28, 28), (30, 28))
        self.add_line('p6-r1-2', (30, 28), (30, 25))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-3', 'p4-r1-1')
        self.relate("connect", 'p5-r1-2', 'p6-r1-1')
        self.relate("connect", 'p5-r1-3', 'p6-r1-1')
