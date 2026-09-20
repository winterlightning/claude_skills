# Variant of zoom-in-sub32; parent file remains unchanged.
"""Independent 32px profile of zoom-in.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a004cae4-ed05-4290-a770-3067f7e07eef'
SOURCE_PATH = 'pictographic-primitives/interface-essential/zoom in_a004cae4-ed05-4290-a770-3067f7e07eef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a004cae4-ed05-4290-a770-3067f7e07eef', 'pictographic-primitives/interface-essential/zoom in_a004cae4-ed05-4290-a770-3067f7e07eef.svg'), ('d2a83b3d-ee41-4915-81af-29e371bfd9b0', 'icon_set/dist/gallery/combination-originals/d2a83b3d-ee41-4915-81af-29e371bfd9b0.svg'))
PROFILE_SOURCE_KEYS = ('solo/zoom-in',)
SOLO_SOURCE_ICON_IDS = ('zoom-in',)
REFERENCE_EXPORT_SHA256 = '209ca90f62812b8d62f2a07ae89b81f3be51b730762084becce5db3d9bca7283'

class DrawingVariant2(Sub32):
    icon_id = 'zoom-in-sub32-v2'
    variant_of = 'zoom-in-sub32'
    variant_label = 'Align magnifier handle with the circle diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 30), (20, 20))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (13, 9), (13, 13))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (9, 13), (13, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 17), (13, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (17, 13), (13, 13))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (2, 13), (24, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p6-r1-2', (24, 13), (2, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
        self.relate('connect', 'path-1-1', 'path-6-1')
