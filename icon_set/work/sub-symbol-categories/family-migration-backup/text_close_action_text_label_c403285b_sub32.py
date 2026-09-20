"""Independent 32px profile of text-close-action-text-label-c403285b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c403285b-1b40-4c4e-98a9-1cbf0794c03f'
SOURCE_PATH = 'icon_set/dist/text32/text-close-action-text-label-c403285b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c403285b-1b40-4c4e-98a9-1cbf0794c03f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/close (text)_c403285b-1b40-4c4e-98a9-1cbf0794c03f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-close-action-text-label-c403285b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-l-uppercase', 'letter-o-uppercase', 'letter-s-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = '492fbb1574ec1459b12bcf13da6bbc67ed90d37860e40e0114a597184bb5f112'

class Drawing(TextSub32):
    icon_id = 'text-close-action-text-label-c403285b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 125
    text_ink_bounds = (0.001457877762348403, 0.0, 125.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (123, 2), (106, 2))
        self.add_line('p1-r1-2', (106, 2), (106, 30))
        self.add_line('p1-r1-3', (106, 30), (123, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (106, 16), (120, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (97, 6), ((96, 3), (93, 2), (89, 2)))
        self.add_bezier('p3-r1-2', (89, 2), ((85, 2), (81, 4), (80, 9)))
        self.add_bezier('p3-r1-3', (80, 9), ((80, 9), (80, 9), (80, 10)))
        self.add_bezier('p3-r1-4', (80, 10), ((80, 17), (97, 13), (98, 22)))
        self.add_bezier('p3-r1-5', (98, 22), ((98, 22), (98, 22), (98, 23)))
        self.add_bezier('p3-r1-6', (98, 23), ((98, 28), (93, 30), (88, 30)))
        self.add_bezier('p3-r1-7', (88, 30), ((85, 30), (81, 29), (79, 26)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_bezier('p4-r1-1', (51, 16), ((51, 8), (56, 2), (61, 2)))
        self.add_bezier('p4-r1-2', (61, 2), ((67, 2), (72, 8), (72, 16)))
        self.add_bezier('p4-r1-3', (72, 16), ((72, 24), (67, 30), (61, 30)))
        self.add_bezier('p4-r1-4', (61, 30), ((56, 30), (51, 24), (51, 16)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (27, 2), (27, 30))
        self.add_line('p5-r1-2', (27, 30), (43, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_arc('p6-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
