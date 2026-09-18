"""Independent 32px profile of text-adobe-photoshop-software-symbol-2b16c0a6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '2b16c0a6-3195-43b8-b0f1-7e5388700c78'
SOURCE_PATH = 'icon_set/dist/text32/text-adobe-photoshop-software-symbol-2b16c0a6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2b16c0a6-3195-43b8-b0f1-7e5388700c78', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/Ps_2b16c0a6-3195-43b8-b0f1-7e5388700c78.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-adobe-photoshop-software-symbol-2b16c0a6',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-s')
REFERENCE_EXPORT_SHA256 = '34ba42ee7aff77a3dbc0afe9e01a0ff8a645bd861606e3679c5061f2680700cc'

class Drawing(TextSub32):
    icon_id = 'text-adobe-photoshop-software-symbol-2b16c0a6-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 44
    text_ink_bounds = (0.0, 0.0, 44.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (42, 13), ((42, 13), (41, 11), (36, 11)))
        self.add_bezier('p1-r1-2', (36, 11), ((32, 11), (30, 13), (30, 16)))
        self.add_bezier('p1-r1-3', (30, 16), ((30, 17), (31, 19), (32, 19)))
        self.add_bezier('p1-r1-4', (32, 19), ((38, 21), (37, 21), (40, 22)))
        self.add_bezier('p1-r1-5', (40, 22), ((41, 23), (42, 24), (42, 25)))
        self.add_bezier('p1-r1-6', (42, 25), ((42, 27), (40, 30), (36, 30)))
        self.add_bezier('p1-r1-7', (36, 30), ((29, 30), (29, 26), (29, 26)))
        self.add_bezier('p1-r1-8', (29, 26), ((29, 26), (29, 26), (29, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (2, 30), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (12, 2))
        self.add_bezier('p2-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p2-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p2-r1-5', (12, 17), (2, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
