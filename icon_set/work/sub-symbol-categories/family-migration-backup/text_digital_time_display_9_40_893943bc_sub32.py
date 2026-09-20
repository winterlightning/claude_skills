"""Independent 32px profile of text-digital-time-display-9-40-893943bc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-digital-time-display-9-40-893943bc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-digital-time-display-9-40-893943bc',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '25807ea25a30c0f2b7d0ccbada9080f1bf47c73db88d505bdcc6ba5292cf566f'

class Drawing(TextSub32):
    icon_id = 'text-digital-time-display-9-40-893943bc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 90
    text_ink_bounds = (0.0, 0.0, 90.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (69, 10), (88, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (88, 10), (88, 22))
        self.add_arc('p1-r1-3', (88, 22), (69, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (69, 22), (69, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (37, 2), (37, 20))
        self.add_bezier('p2-r1-2', (37, 20), ((37, 20), (38, 20), (38, 20)))
        self.add_line('p2-r1-3', (38, 20), (61, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (56, 2), (56, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 14), (30, 14))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, 28), (30, 28))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_arc('p6-r1-1', (2, 10), (22, 10), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p6-r1-2', (22, 10), (2, 10), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (22, 10), (22, 20))
        self.add_bezier('p7-r1-2', (22, 20), ((22, 26), (17, 30), (12, 30)))
        self.add_line('p7-r1-3', (12, 30), (5, 30))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', closed=False)
        self.relate("connect", 'p6-r1-1', 'p7-r1-1')
        self.relate("connect", 'p6-r1-2', 'p7-r1-1')
