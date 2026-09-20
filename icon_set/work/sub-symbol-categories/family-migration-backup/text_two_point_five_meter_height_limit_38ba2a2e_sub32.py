"""Independent 32px profile of text-two-point-five-meter-height-limit-38ba2a2e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-two-point-five-meter-height-limit-38ba2a2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-two-point-five-meter-height-limit-38ba2a2e',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'b29d3c159adf05c9dc63533b851e72ea2b78ea41a2a6ab4bbf379d76e85728a2'

class Drawing(TextSub32):
    icon_id = 'text-two-point-five-meter-height-limit-38ba2a2e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 121
    text_ink_bounds = (0.0, 0.0, 121.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (72, 30), (72, 2))
        self.add_line('p1-r1-2', (72, 2), (86, 20))
        self.add_line('p1-r1-3', (86, 20), (99, 2))
        self.add_line('p1-r1-4', (99, 2), (99, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (60, 2), (43, 2))
        self.add_bezier('p2-r1-2', (43, 2), ((43, 2), (42, 2), (42, 3)))
        self.add_line('p2-r1-3', (42, 3), (42, 13))
        self.add_bezier('p2-r1-4', (42, 13), ((42, 13), (43, 14), (43, 14)))
        self.add_line('p2-r1-5', (43, 14), (54, 14))
        self.add_bezier('p2-r1-6', (54, 14), ((59, 14), (62, 18), (62, 22)))
        self.add_bezier('p2-r1-7', (62, 22), ((62, 24), (61, 26), (60, 28)))
        self.add_bezier('p2-r1-8', (60, 28), ((58, 29), (56, 30), (54, 30)))
        self.add_line('p2-r1-9', (54, 30), (43, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', closed=False)
        self.add_line('p3-r1-1', (32, 30), (32, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (16, 2))
        self.add_bezier('p4-r1-2', (16, 2), ((19, 2), (21, 5), (21, 8)))
        self.add_bezier('p4-r1-3', (21, 8), ((21, 9), (21, 11), (19, 12)))
        self.add_line('p4-r1-4', (19, 12), (6, 21))
        self.add_bezier('p4-r1-5', (6, 21), ((3, 23), (2, 25), (2, 28)))
        self.add_line('p4-r1-6', (2, 28), (2, 29))
        self.add_bezier('p4-r1-7', (2, 29), ((2, 29), (3, 30), (3, 30)))
        self.add_line('p4-r1-8', (3, 30), (22, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', 'p4-r1-8', closed=False)
        self.add_line('p5-r1-1', (107, 2), (113, 8))
        self.add_line('p5-r1-2', (113, 8), (119, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (107, 30), (113, 24))
        self.add_line('p6-r1-2', (113, 24), (119, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
