"""Independent 32px profile of text-number-twenty-four-e3ef1255.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e3ef1255-7230-466e-a0e3-b1897407d9eb'
SOURCE_PATH = 'icon_set/dist/text32/text-number-twenty-four-e3ef1255.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3ef1255-7230-466e-a0e3-b1897407d9eb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/24 (text)_e3ef1255-7230-466e-a0e3-b1897407d9eb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-twenty-four-e3ef1255',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-2', 'digit-4')
REFERENCE_EXPORT_SHA256 = '4ea08e000af44f9e276dfa903baed513fc578a6cdc3084dcaef0498f42edb88f'

class Drawing(TextSub32):
    icon_id = 'text-number-twenty-four-e3ef1255-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 55
    text_ink_bounds = (0.0, 0.0, 55.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (29, 20))
        self.add_bezier('p1-r1-2', (29, 20), ((29, 20), (30, 20), (30, 20)))
        self.add_line('p1-r1-3', (30, 20), (53, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (48, 2), (48, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 2), (16, 2))
        self.add_bezier('p3-r1-2', (16, 2), ((19, 2), (21, 5), (21, 8)))
        self.add_bezier('p3-r1-3', (21, 8), ((21, 9), (21, 11), (19, 12)))
        self.add_line('p3-r1-4', (19, 12), (6, 21))
        self.add_bezier('p3-r1-5', (6, 21), ((3, 23), (2, 25), (2, 28)))
        self.add_line('p3-r1-6', (2, 28), (2, 29))
        self.add_bezier('p3-r1-7', (2, 29), ((2, 29), (3, 30), (3, 30)))
        self.add_line('p3-r1-8', (3, 30), (22, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', closed=False)
