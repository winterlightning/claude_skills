"""Independent 32px profile of text-live-broadcast-text-fd4d233f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'fd4d233f-49e3-4049-8eaa-28c7fcc79a4e'
SOURCE_PATH = 'icon_set/dist/text32/text-live-broadcast-text-fd4d233f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fd4d233f-49e3-4049-8eaa-28c7fcc79a4e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/live (text)_fd4d233f-49e3-4049-8eaa-28c7fcc79a4e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-live-broadcast-text-fd4d233f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-l-uppercase', 'letter-i-uppercase', 'letter-v-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = 'd8debe25c12242e0d7d4d1d297388f4ef7b2eabb5072df9d27ab43eadc0a50a6'

class Drawing(TextSub32):
    icon_id = 'text-live-broadcast-text-fd4d233f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 92
    text_ink_bounds = (0.0, 0.0, 92.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (90, 2), (72, 2))
        self.add_line('p1-r1-2', (72, 2), (72, 30))
        self.add_line('p1-r1-3', (72, 30), (90, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (72, 16), (86, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (43, 2), (52, 28))
        self.add_bezier('p3-r1-2', (52, 28), ((52.666666666666664, 29.333333333333332), (53.333333333333336, 30), (54, 30)))
        self.add_bezier('p3-r1-3', (54, 30), ((54.666666666666664, 30), (55, 29.333333333333332), (55, 28)))
        self.add_line('p3-r1-4', (55, 28), (65, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (26, 2), (36, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (31, 2), (31, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (26, 30), (36, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (2, 2), (2, 30))
        self.add_line('p7-r1-2', (2, 30), (18, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
