"""Independent 32px profile of text-uppercase-alphabet-letters-e2e77865.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'e2e77865-5fe3-4370-8b07-0bcd6d0b11df'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-alphabet-letters-e2e77865.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2e77865-5fe3-4370-8b07-0bcd6d0b11df', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/abc_e2e77865-5fe3-4370-8b07-0bcd6d0b11df.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-alphabet-letters-e2e77865',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-b-uppercase', 'letter-c-uppercase')
REFERENCE_EXPORT_SHA256 = '21af56470a3ba9c50f71aa55f8cab1f56220f3b77f96933868810c598d9b3b3c'

class Drawing(TextSub32):
    icon_id = 'text-uppercase-alphabet-letters-e2e77865-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 77
    text_ink_bounds = (0.0, 0.0, 77.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (75, 6), (75, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (31, 30), (31, 2))
        self.add_line('p2-r1-2', (31, 2), (40, 2))
        self.add_bezier('p2-r1-3', (40, 2), ((46, 2), (49, 6), (49, 9)))
        self.add_bezier('p2-r1-4', (49, 9), ((49, 13), (46, 16), (40, 16)))
        self.add_line('p2-r1-5', (40, 16), (31, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_bezier('p3-r1-1', (40, 16), ((46, 16), (49, 20), (49, 23)))
        self.add_bezier('p3-r1-2', (49, 23), ((49, 26), (46, 30), (40, 30)))
        self.add_line('p3-r1-3', (40, 30), (31, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 30), (11, 3))
        self.add_bezier('p4-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p4-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p4-r1-4', (14, 3), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (6, 18), (19, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p2-r1-1', 'p3-r1-3')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
