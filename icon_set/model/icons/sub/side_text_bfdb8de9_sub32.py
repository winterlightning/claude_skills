"""Independent 32px profile of side-text-bfdb8de9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0'
SOURCE_PATH = 'icon_set/dist/text32/side-text-bfdb8de9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0', 'icon_set/dist/gallery/combination-originals/bfdb8de9-05a8-4a32-a4cf-47cecb08dfc0.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-bfdb8de9',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-c-uppercase', 'letter-p-uppercase', 'letter-a-uppercase')
REFERENCE_EXPORT_SHA256 = 'ecffe1ed2f8f656c3322c409cc2a94b2e3e17dd1ab9092606cec7857b39c0dda'

class Drawing(TextSub32):
    icon_id = 'side-text-bfdb8de9-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 101
    text_ink_bounds = (0.001457877762348403, 0.0, 101.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (78, 30), (87, 3))
        self.add_bezier('p1-r1-2', (87, 3), ((87.66666666666667, 2.3333333333333335), (88, 2), (88, 2)))
        self.add_bezier('p1-r1-3', (88, 2), ((88.66666666666667, 2), (89, 2.3333333333333335), (89, 3)))
        self.add_line('p1-r1-4', (89, 3), (99, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (82, 18), (94, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (51, 30), (51, 2))
        self.add_line('p3-r1-2', (51, 2), (61, 2))
        self.add_bezier('p3-r1-3', (61, 2), ((67, 2), (70, 6), (70, 9)))
        self.add_bezier('p3-r1-4', (70, 9), ((70, 13), (67, 17), (61, 17)))
        self.add_line('p3-r1-5', (61, 17), (51, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_arc('p4-r1-1', (44, 6), (44, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_arc('p5-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
