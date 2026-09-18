"""Independent 32px profile of text-bike-lane-text-sign-38ab6d8c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '38ab6d8c-ec97-43bd-ba8c-e25edc8ad4f4'
SOURCE_PATH = 'icon_set/dist/text32/text-bike-lane-text-sign-38ab6d8c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('38ab6d8c-ec97-43bd-ba8c-e25edc8ad4f4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/BIKE LANE_38ab6d8c-ec97-43bd-ba8c-e25edc8ad4f4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bike-lane-text-sign-38ab6d8c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'letter-i-uppercase', 'letter-k-uppercase', 'letter-e-uppercase', 'letter-l-uppercase', 'letter-a-uppercase', 'letter-n-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = '82962b1ec2e14b8836a6fa5dd4b178a4671dc6356c006a11042029bf64877e28'

class Drawing(TextSub32):
    icon_id = 'text-bike-lane-text-sign-38ab6d8c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 228
    text_ink_bounds = (0.0, 0.0, 227.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (225, 2), (208, 2))
        self.add_line('p1-r1-2', (208, 2), (208, 30))
        self.add_line('p1-r1-3', (208, 30), (225, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (208, 16), (222, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (177, 30), (177, 2))
        self.add_line('p3-r1-2', (177, 2), (197, 30))
        self.add_line('p3-r1-3', (197, 30), (197, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (146, 30), (155, 3))
        self.add_bezier('p4-r1-2', (155, 3), ((155.66666666666666, 2.3333333333333335), (156, 2), (156, 2)))
        self.add_bezier('p4-r1-3', (156, 2), ((156.66666666666666, 2), (157, 2.3333333333333335), (157, 3)))
        self.add_line('p4-r1-4', (157, 3), (167, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (150, 18), (163, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (119, 2), (119, 30))
        self.add_line('p6-r1-2', (119, 30), (135, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (98, 2), (81, 2))
        self.add_line('p7-r1-2', (81, 2), (81, 30))
        self.add_line('p7-r1-3', (81, 30), (98, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.add_line('p8-r1-1', (81, 16), (95, 16))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (51, 2), (51, 30))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.add_line('p10-r1-1', (70, 2), (51, 17))
        self.add_line('p10-r1-2', (51, 17), (70, 30))
        self.add_contour('path-10-1', 'p10-r1-1', 'p10-r1-2', closed=False)
        self.add_line('p11-r1-1', (31, 2), (40, 2))
        self.add_contour('path-11-1', 'p11-r1-1', closed=False)
        self.add_line('p12-r1-1', (36, 2), (36, 30))
        self.add_contour('path-12-1', 'p12-r1-1', closed=False)
        self.add_line('p13-r1-1', (31, 30), (40, 30))
        self.add_contour('path-13-1', 'p13-r1-1', closed=False)
        self.add_line('p14-r1-1', (2, 30), (2, 2))
        self.add_line('p14-r1-2', (2, 2), (11, 2))
        self.add_bezier('p14-r1-3', (11, 2), ((17, 2), (20, 6), (20, 9)))
        self.add_bezier('p14-r1-4', (20, 9), ((20, 13), (17, 16), (11, 16)))
        self.add_line('p14-r1-5', (11, 16), (2, 16))
        self.add_contour('path-14-1', 'p14-r1-1', 'p14-r1-2', 'p14-r1-3', 'p14-r1-4', 'p14-r1-5', closed=False)
        self.add_bezier('p15-r1-1', (11, 16), ((18, 16), (21, 19), (21, 23)))
        self.add_bezier('p15-r1-2', (21, 23), ((21, 26), (18, 30), (11, 30)))
        self.add_line('p15-r1-3', (11, 30), (2, 30))
        self.add_contour('path-15-1', 'p15-r1-1', 'p15-r1-2', 'p15-r1-3', closed=False)
        self.relate('connect', 'p14-r1-1', 'p15-r1-3')
        self.relate('connect', 'p14-r1-4', 'p15-r1-1')
        self.relate('connect', 'p14-r1-5', 'p15-r1-1')
