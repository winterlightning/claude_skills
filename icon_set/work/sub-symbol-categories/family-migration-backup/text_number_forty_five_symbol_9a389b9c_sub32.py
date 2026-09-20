"""Independent 32px profile of text-number-forty-five-symbol-9a389b9c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '9a389b9c-8800-4ddb-a7b5-00af44020677'
SOURCE_PATH = 'icon_set/dist/text32/text-number-forty-five-symbol-9a389b9c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9a389b9c-8800-4ddb-a7b5-00af44020677', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/45_9a389b9c-8800-4ddb-a7b5-00af44020677.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-forty-five-symbol-9a389b9c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-4', 'digit-5')
REFERENCE_EXPORT_SHA256 = 'b5217514c29e24b2d3c8a5142555457a34c22234cbd15de1eef90f75c0e41a0b'

class Drawing(TextSub32):
    icon_id = 'text-number-forty-five-symbol-9a389b9c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 55
    text_ink_bounds = (0.0, 0.0, 55.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (51, 2), (34, 2))
        self.add_bezier('p1-r1-2', (34, 2), ((34, 2), (33, 2), (33, 3)))
        self.add_line('p1-r1-3', (33, 3), (33, 13))
        self.add_bezier('p1-r1-4', (33, 13), ((33, 13), (34, 14), (34, 14)))
        self.add_line('p1-r1-5', (34, 14), (45, 14))
        self.add_bezier('p1-r1-6', (45, 14), ((50, 14), (53, 18), (53, 22)))
        self.add_bezier('p1-r1-7', (53, 22), ((53, 24), (52, 26), (51, 28)))
        self.add_bezier('p1-r1-8', (51, 28), ((49, 29), (47, 30), (45, 30)))
        self.add_line('p1-r1-9', (45, 30), (34, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 20))
        self.add_bezier('p2-r1-2', (2, 20), ((2, 20), (2, 20), (3, 20)))
        self.add_line('p2-r1-3', (3, 20), (26, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (21, 2), (21, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
