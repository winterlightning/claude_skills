"""Independent 32px profile of text-the-number-five-digit-7313b9de.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '7313b9de-e69b-43f7-8caa-a6ffcfca182e'
SOURCE_PATH = 'icon_set/dist/text32/text-the-number-five-digit-7313b9de.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7313b9de-e69b-43f7-8caa-a6ffcfca182e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/5 (text)_7313b9de-e69b-43f7-8caa-a6ffcfca182e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-the-number-five-digit-7313b9de',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-5',)
REFERENCE_EXPORT_SHA256 = '7de60c1141c7ff185b06dcfc0b9595f830469c7b8f20e2a11c9c8de2c5b6b1d2'

class Drawing(TextSub32):
    icon_id = 'text-the-number-five-digit-7313b9de-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 23
    text_ink_bounds = (0.0, 0.0, 23.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (19, 2), (3, 2))
        self.add_bezier('p1-r1-2', (3, 2), ((2, 2), (2, 2), (2, 3)))
        self.add_line('p1-r1-3', (2, 3), (2, 13))
        self.add_bezier('p1-r1-4', (2, 13), ((2, 13), (2, 14), (3, 14)))
        self.add_line('p1-r1-5', (3, 14), (13, 14))
        self.add_bezier('p1-r1-6', (13, 14), ((18, 14), (21, 18), (21, 22)))
        self.add_bezier('p1-r1-7', (21, 22), ((21, 24), (21, 26), (19, 28)))
        self.add_bezier('p1-r1-8', (19, 28), ((18, 29), (15, 30), (13, 30)))
        self.add_line('p1-r1-9', (13, 30), (3, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
