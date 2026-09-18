"""Independent 32px profile of text-dwg-cad-file-format-26e20867.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '26e20867-fec6-496d-91f2-39291a2d0fc6'
SOURCE_PATH = 'icon_set/dist/text32/text-dwg-cad-file-format-26e20867.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('26e20867-fec6-496d-91f2-39291a2d0fc6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dwg (text)_26e20867-fec6-496d-91f2-39291a2d0fc6.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-dwg-cad-file-format-26e20867',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-w-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = '04e95afdc2e5b7af22d65df1e2229ad17bda8bb5cdb8fa98a77ae6b3f6ae7130'

class Drawing(TextSub32):
    icon_id = 'text-dwg-cad-file-format-26e20867-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 89
    text_ink_bounds = (0.0, 0.0, 89.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (84, 6), ((82, 4), (80, 2), (78, 2)))
        self.add_bezier('p1-r1-2', (78, 2), ((72, 2), (67, 9), (67, 17)))
        self.add_bezier('p1-r1-3', (67, 17), ((67, 18), (67, 20), (67, 21)))
        self.add_bezier('p1-r1-4', (67, 21), ((69, 27), (73, 29), (76, 29)))
        self.add_bezier('p1-r1-5', (76, 29), ((82, 29), (87, 24), (87, 16)))
        self.add_line('p1-r1-6', (87, 16), (79, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (29, 2), (36, 28))
        self.add_bezier('p2-r1-2', (36, 28), ((36, 29.333333333333332), (36, 30), (36, 30)))
        self.add_bezier('p2-r1-3', (36, 30), ((36.666666666666664, 30), (37, 29.333333333333332), (37, 28)))
        self.add_line('p2-r1-4', (37, 28), (43, 4))
        self.add_bezier('p2-r1-5', (43, 4), ((43.666666666666664, 3.3333333333333335), (44, 3), (44, 3)))
        self.add_bezier('p2-r1-6', (44, 3), ((44, 3), (44.333333333333336, 3.3333333333333335), (45, 4)))
        self.add_line('p2-r1-7', (45, 4), (51, 28))
        self.add_bezier('p2-r1-8', (51, 28), ((51, 29.333333333333332), (51.333333333333336, 30), (52, 30)))
        self.add_bezier('p2-r1-9', (52, 30), ((52, 30), (52.333333333333336, 29.333333333333332), (53, 28)))
        self.add_line('p2-r1-10', (53, 28), (59, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.add_line('p3-r1-1', (2, 2), (10, 2))
        self.add_bezier('p3-r1-2', (10, 2), ((18, 2), (21, 9), (21, 16)))
        self.add_bezier('p3-r1-3', (21, 16), ((21, 23), (18, 30), (10, 30)))
        self.add_line('p3-r1-4', (10, 30), (2, 30))
        self.add_line('p3-r1-5', (2, 30), (2, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
