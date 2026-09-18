"""Independent 32px profile of text-internal-server-error-alert-9c6caa89.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-internal-server-error-alert-9c6caa89.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-internal-server-error-alert-9c6caa89',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '67cb0b78d377768f13363892710100d9a6c15bc0b965db59ba9b5af0c697ee19'

class Drawing(TextSub32):
    icon_id = 'text-internal-server-error-alert-9c6caa89-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 102
    text_ink_bounds = (0.0, 0.0, 101.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (80, 11), ((80, 7), (85, 3), (90, 3)))
        self.add_bezier('p1-r1-2', (90, 3), ((95, 3), (99, 7), (99, 11)))
        self.add_line('p1-r1-3', (99, 11), (99, 22))
        self.add_bezier('p1-r1-4', (99, 22), ((99, 27), (95, 30), (90, 30)))
        self.add_bezier('p1-r1-5', (90, 30), ((85, 30), (80, 27), (80, 22)))
        self.add_line('p1-r1-6', (80, 22), (80, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_bezier('p2-r1-1', (51, 11), ((51, 7), (56, 3), (61, 3)))
        self.add_bezier('p2-r1-2', (61, 3), ((66, 3), (70, 7), (70, 11)))
        self.add_line('p2-r1-3', (70, 11), (70, 22))
        self.add_bezier('p2-r1-4', (70, 22), ((70, 27), (66, 30), (61, 30)))
        self.add_bezier('p2-r1-5', (61, 30), ((56, 30), (51, 27), (51, 22)))
        self.add_line('p2-r1-6', (51, 22), (51, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (39, 3), (23, 3))
        self.add_bezier('p3-r1-2', (23, 3), ((23, 3), (22, 3), (22, 4)))
        self.add_line('p3-r1-3', (22, 4), (22, 13))
        self.add_bezier('p3-r1-4', (22, 13), ((22, 14), (23, 14), (23, 14)))
        self.add_line('p3-r1-5', (23, 14), (33, 14))
        self.add_bezier('p3-r1-6', (33, 14), ((38, 14), (41, 18), (41, 22)))
        self.add_bezier('p3-r1-7', (41, 22), ((41, 24), (41, 26), (39, 28)))
        self.add_bezier('p3-r1-8', (39, 28), ((37, 29), (35, 30), (33, 30)))
        self.add_line('p3-r1-9', (33, 30), (23, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (2, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
