"""Independent 32px profile of text-underlined-pt-typography-icon-a877b1f2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a877b1f2-7112-423f-ba6f-00b26c285a22'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-pt-typography-icon-a877b1f2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a877b1f2-7112-423f-ba6f-00b26c285a22', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/pt (text u)_a877b1f2-7112-423f-ba6f-00b26c285a22.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-pt-typography-icon-a877b1f2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-t')
REFERENCE_EXPORT_SHA256 = '7dd40d50d7865f9561f7cc77c851ea18c41dd3fb6f627478f140188ffb0a06c2'

class Drawing(TextSub32):
    icon_id = 'text-underlined-pt-typography-icon-a877b1f2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 33
    text_ink_bounds = (0.0, 0.0, 33.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (31, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (26, 3), ((26, 3), (26, 8), (26, 12)))
        self.add_bezier('p2-r1-2', (26, 12), ((26, 14), (26, 16), (26, 17)))
        self.add_bezier('p2-r1-3', (26, 17), ((26, 18), (26, 20), (28, 21)))
        self.add_bezier('p2-r1-4', (28, 21), ((29, 21), (29, 21), (30, 21)))
        self.add_bezier('p2-r1-5', (30, 21), ((31, 21), (31, 21), (31, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (22, 8), (30, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (9, 2))
        self.add_bezier('p4-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p4-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p4-r1-5', (9, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
