"""Independent 32px profile of text-eighties-retro-decade-text-e6507059.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e6507059-e63e-42cc-bb37-3004dc017157'
SOURCE_PATH = 'icon_set/dist/text32/text-eighties-retro-decade-text-e6507059.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e6507059-e63e-42cc-bb37-3004dc017157', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/80s_e6507059-e63e-42cc-bb37-3004dc017157.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-eighties-retro-decade-text-e6507059',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-8', 'digit-0', 'letter-s')
REFERENCE_EXPORT_SHA256 = '422eae62c508756346e409a1d6e08a230ed5ea680ae7f717a35160b00b152ec5'

class Drawing(TextSub32):
    icon_id = 'text-eighties-retro-decade-text-e6507059-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 71
    text_ink_bounds = (0.0, 0.0, 71.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (69, 13), ((69, 13), (69, 11), (63, 11)))
        self.add_bezier('p1-r1-2', (63, 11), ((59, 11), (57, 13), (57, 16)))
        self.add_bezier('p1-r1-3', (57, 16), ((57, 17), (58, 19), (60, 19)))
        self.add_bezier('p1-r1-4', (60, 19), ((65, 21), (64, 21), (67, 22)))
        self.add_bezier('p1-r1-5', (67, 22), ((69, 23), (69, 24), (69, 25)))
        self.add_bezier('p1-r1-6', (69, 25), ((69, 27), (67, 30), (63, 30)))
        self.add_bezier('p1-r1-7', (63, 30), ((56, 30), (56, 26), (56, 26)))
        self.add_bezier('p1-r1-8', (56, 26), ((56, 26), (56, 26), (56, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (29, 10), (49, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (49, 10), (49, 22))
        self.add_arc('p2-r1-3', (49, 22), (29, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (29, 22), (29, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (3, 9), ((3, 5), (6, 2), (10, 2)))
        self.add_line('p3-r1-2', (10, 2), (14, 2))
        self.add_bezier('p3-r1-3', (14, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p3-r1-4', (20, 9), ((20, 12), (17, 15), (14, 15)))
        self.add_line('p3-r1-5', (14, 15), (10, 15))
        self.add_bezier('p3-r1-6', (10, 15), ((6, 15), (3, 12), (3, 9)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_bezier('p4-r1-1', (2, 23), ((2, 19), (5, 15), (9, 15)))
        self.add_line('p4-r1-2', (9, 15), (14, 15))
        self.add_bezier('p4-r1-3', (14, 15), ((18, 15), (21, 19), (21, 23)))
        self.add_bezier('p4-r1-4', (21, 23), ((21, 27), (18, 30), (14, 30)))
        self.add_line('p4-r1-5', (14, 30), (9, 30))
        self.add_bezier('p4-r1-6', (9, 30), ((5, 30), (2, 27), (2, 23)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.relate("connect", 'p3-r1-4', 'p4-r1-2')
        self.relate("connect", 'p3-r1-4', 'p4-r1-3')
        self.relate("connect", 'p3-r1-5', 'p4-r1-2')
        self.relate("connect", 'p3-r1-5', 'p4-r1-3')
