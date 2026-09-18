"""Independent 32px profile of text-vip-status-label-a4f4b16a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a4f4b16a-7805-4ee9-86a1-1dab21c53494'
SOURCE_PATH = 'icon_set/dist/text32/text-vip-status-label-a4f4b16a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a4f4b16a-7805-4ee9-86a1-1dab21c53494', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/VIP (text)_a4f4b16a-7805-4ee9-86a1-1dab21c53494.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-vip-status-label-a4f4b16a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-v-uppercase', 'letter-i-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = '123366aeb2e42c91c99c8c852aadeed8691b45a33382d7c8c3ad0d14e4cb0e24'

class Drawing(TextSub32):
    icon_id = 'text-vip-status-label-a4f4b16a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 70
    text_ink_bounds = (0.0, 0.0, 70.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (48, 30), (48, 2))
        self.add_line('p1-r1-2', (48, 2), (58, 2))
        self.add_bezier('p1-r1-3', (58, 2), ((65, 2), (68, 6), (68, 9)))
        self.add_bezier('p1-r1-4', (68, 9), ((68, 13), (65, 17), (58, 17)))
        self.add_line('p1-r1-5', (58, 17), (48, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (31, 2), (40, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (36, 2), (36, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (31, 30), (40, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (11, 28))
        self.add_bezier('p5-r1-2', (11, 28), ((11.666666666666666, 29.333333333333332), (12.333333333333334, 30), (13, 30)))
        self.add_bezier('p5-r1-3', (13, 30), ((13, 30), (13.333333333333334, 29.333333333333332), (14, 28)))
        self.add_line('p5-r1-4', (14, 28), (23, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
