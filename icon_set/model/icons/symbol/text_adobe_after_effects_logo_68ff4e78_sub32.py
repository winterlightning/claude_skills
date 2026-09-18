"""Independent 32px profile of text-adobe-after-effects-logo-68ff4e78.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '68ff4e78-e6b9-4409-8627-b9404af60121'
SOURCE_PATH = 'icon_set/dist/text32/text-adobe-after-effects-logo-68ff4e78.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('68ff4e78-e6b9-4409-8627-b9404af60121', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/Ae_68ff4e78-e6b9-4409-8627-b9404af60121.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-adobe-after-effects-logo-68ff4e78',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = '3436ba42693fd1c8b12fa0425ee34ba1ce4748f1282f492efbea3408b19e7022'

class Drawing(TextSub32):
    icon_id = 'text-adobe-after-effects-logo-68ff4e78-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 52
    text_ink_bounds = (0.0, 0.0, 52.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (50, 20), ((50, 15), (46, 11), (40, 11)))
        self.add_bezier('p1-r1-2', (40, 11), ((35, 11), (31, 15), (31, 20)))
        self.add_bezier('p1-r1-3', (31, 20), ((31, 26), (35, 30), (40, 30)))
        self.add_bezier('p1-r1-4', (40, 30), ((44, 30), (47, 28), (49, 25)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (31, 20), (50, 20))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 30), (11, 3))
        self.add_bezier('p3-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p3-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p3-r1-4', (14, 3), (23, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (6, 18), (19, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
