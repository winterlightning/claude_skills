"""Independent 32px profile of text-kilogram-weight-measurement-symbol-23237409.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '23237409-43f0-422b-bb69-aa7978933593'
SOURCE_PATH = 'icon_set/dist/text32/text-kilogram-weight-measurement-symbol-23237409.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('23237409-43f0-422b-bb69-aa7978933593', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/kg (text)_23237409-43f0-422b-bb69-aa7978933593.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-kilogram-weight-measurement-symbol-23237409',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-k-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = '73b8a3e226c7b604f65c13ae786a4e62813e0542a1ded48d5d65435759a9afbd'

class Drawing(TextSub32):
    icon_id = 'text-kilogram-weight-measurement-symbol-23237409-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 52
    text_ink_bounds = (0.0, 0.0, 52.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (47, 6), ((45, 4), (42, 2), (40, 2)))
        self.add_bezier('p1-r1-2', (40, 2), ((35, 2), (29, 9), (29, 17)))
        self.add_bezier('p1-r1-3', (29, 17), ((29, 18), (30, 20), (30, 21)))
        self.add_bezier('p1-r1-4', (30, 21), ((32, 27), (35, 29), (39, 29)))
        self.add_bezier('p1-r1-5', (39, 29), ((44, 29), (50, 24), (50, 16)))
        self.add_line('p1-r1-6', (50, 16), (42, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 2), (2, 17))
        self.add_line('p3-r1-2', (2, 17), (21, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
