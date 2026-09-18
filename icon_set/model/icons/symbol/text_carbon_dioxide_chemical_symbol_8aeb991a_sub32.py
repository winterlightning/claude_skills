"""Independent 32px profile of text-carbon-dioxide-chemical-symbol-8aeb991a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '8aeb991a-9c5c-47c1-ae2e-eb43cacad66e'
SOURCE_PATH = 'icon_set/dist/text32/text-carbon-dioxide-chemical-symbol-8aeb991a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8aeb991a-9c5c-47c1-ae2e-eb43cacad66e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/co2 (text)_8aeb991a-9c5c-47c1-ae2e-eb43cacad66e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-carbon-dioxide-chemical-symbol-8aeb991a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-o-uppercase', 'digit-2')
REFERENCE_EXPORT_SHA256 = 'e15561f8934c33c32869258ae6ba6129c3f8c0f5ca2352a038773ebb89349fa1'

class Drawing(TextSub32):
    icon_id = 'text-carbon-dioxide-chemical-symbol-8aeb991a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 77
    text_ink_bounds = (0.001457877762348403, 0.0, 77.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (55, 2), (69, 2))
        self.add_bezier('p1-r1-2', (69, 2), ((73, 2), (75, 5), (75, 8)))
        self.add_bezier('p1-r1-3', (75, 8), ((75, 9), (74, 11), (72, 12)))
        self.add_line('p1-r1-4', (72, 12), (59, 21))
        self.add_bezier('p1-r1-5', (59, 21), ((56, 23), (55, 25), (55, 28)))
        self.add_line('p1-r1-6', (55, 28), (55, 29))
        self.add_bezier('p1-r1-7', (55, 29), ((55, 29), (56, 30), (57, 30)))
        self.add_line('p1-r1-8', (57, 30), (75, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (27, 16), (47, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('p2-r1-2', (47, 16), (27, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_arc('p3-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
