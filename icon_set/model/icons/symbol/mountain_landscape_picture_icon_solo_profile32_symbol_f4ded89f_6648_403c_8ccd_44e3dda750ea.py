"""Independent 32px profile of mountain-landscape-picture-icon-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f4ded89f-6648-403c-8ccd-44e3dda750ea'
SOURCE_PATH = 'pictographic-primitives/images/image_f4ded89f-6648-403c-8ccd-44e3dda750ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f4ded89f-6648-403c-8ccd-44e3dda750ea', 'pictographic-primitives/images/image_f4ded89f-6648-403c-8ccd-44e3dda750ea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mountain-landscape-picture-icon-solo',)
SOLO_SOURCE_ICON_IDS = ('mountain-landscape-picture-icon-solo',)
REFERENCE_EXPORT_SHA256 = '5d1fa048e0e9db621d5bf186e1836195fc7ee7b0b915dee0cfb207d80d16c017'

class DrawingContainerSymbol(Sub32):
    icon_id = 'mountain-landscape-picture-icon-solo-profile32-symbol'
    related_origin_icon_id = 'mountain-landscape-picture-icon-solo-profile32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/mountain-landscape-picture-icon-solo-profile32'
    counterpart_icon_id = 'mountain-landscape-picture-icon-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'images'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (6, 2), (26, 2))
        self.add_arc('p1-r1-2', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (30, 6), (30, 26))
        self.add_arc('p1-r1-4', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (26, 30), (6, 30))
        self.add_arc('p1-r1-6', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (2, 26), (2, 6))
        self.add_arc('p1-r1-8', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (9, 11), (14, 11), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (14, 11), (9, 11), radius_x=2.5, radius_y=2.5, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 26), (11, 21))
        self.add_line('p3-r1-2', (11, 21), (15, 25))
        self.add_line('p3-r1-3', (15, 25), (22, 17))
        self.add_line('p3-r1-4', (22, 17), (30, 26))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p1-r1-3', 'p3-r1-4')
        self.relate('connect', 'p1-r1-4', 'p3-r1-4')
        self.relate('connect', 'p1-r1-6', 'p3-r1-1')
        self.relate('connect', 'p1-r1-7', 'p3-r1-1')
