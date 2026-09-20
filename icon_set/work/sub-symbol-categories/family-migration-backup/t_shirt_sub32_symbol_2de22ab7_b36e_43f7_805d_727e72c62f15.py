# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of t-shirt.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2de22ab7-b36e-43f7-805d-727e72c62f15'
SOURCE_PATH = 'pictographic-primitives/clothes/t shirt_2de22ab7-b36e-43f7-805d-727e72c62f15.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2de22ab7-b36e-43f7-805d-727e72c62f15', 'pictographic-primitives/clothes/t shirt_2de22ab7-b36e-43f7-805d-727e72c62f15.svg'), ('5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7', 'pictographic-primitives/clothes/t shirt_5f0ac9bd-d1ec-43e8-ba78-79f54033a5b7.svg'), ('9aa1a37e-7127-4719-8aeb-03b09b01c294', 'pictographic-primitives/clothes/t shirt_9aa1a37e-7127-4719-8aeb-03b09b01c294.svg'), ('45dc1629-c2e7-477c-80d5-ad5686c1271e', 'pictographic-primitives/clothes/t shirt_45dc1629-c2e7-477c-80d5-ad5686c1271e.svg'), ('bc825952-a086-4761-9814-673ca2bec10b', 'pictographic-primitives/clothes/t shirt_bc825952-a086-4761-9814-673ca2bec10b.svg'))
PROFILE_SOURCE_KEYS = ('solo/t-shirt', 'solo/crew-neck-t-shirt-with-angled-sleeves', 'solo/t-shirt-45dc1629', 'solo/t-shirt-bc825952')
SOLO_SOURCE_ICON_IDS = ('t-shirt', 'crew-neck-t-shirt-with-angled-sleeves', 't-shirt-45dc1629', 't-shirt-bc825952')
REFERENCE_EXPORT_SHA256 = '3b3df99942fcef6e2f4e2e59018e775771aba262055235c6b1ceb0db3006c20d'

class DrawingContainerSymbol(Sub32):
    icon_id = 't-shirt-sub32-symbol'
    variant_of = 't-shirt-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/t-shirt-sub32'
    counterpart_icon_id = 't-shirt-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'clothes'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (10, 5), (22, 5), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-2', (22, 5), ((27, 5), (30, 8), (30, 12)))
        self.add_line('p1-r1-3', (30, 12), (30, 17))
        self.add_line('p1-r1-4', (30, 17), (24, 17))
        self.add_line('p1-r1-5', (24, 17), (24, 27))
        self.add_line('p1-r1-6', (24, 27), (8, 27))
        self.add_line('p1-r1-7', (8, 27), (8, 17))
        self.add_line('p1-r1-8', (8, 17), (2, 17))
        self.add_line('p1-r1-9', (2, 17), (2, 12))
        self.add_bezier('p1-r1-10', (2, 12), ((2, 8), (5, 5), (10, 5)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (8, 17), (8, 12))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 17), (24, 12))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-5', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
        self.relate('connect', 'p1-r1-8', 'p2-r1-1')
