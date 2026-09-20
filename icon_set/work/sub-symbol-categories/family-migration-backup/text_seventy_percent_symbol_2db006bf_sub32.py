"""Independent 32px profile of text-seventy-percent-symbol-2db006bf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text28/text-seventy-percent-symbol-2db006bf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/text-seventy-percent-symbol-2db006bf',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'cb8f20f102621418587583cafc4c76860471c67888ffcff94432c562b84ca61f'

class Drawing(TextSub32):
    icon_id = 'text-seventy-percent-symbol-2db006bf-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 82
    text_ink_bounds = (0.0, 0.0, 82.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (59, 30), (80, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (59, 7), ((59, 4), (61, 2), (63, 2)))
        self.add_bezier('p2-r1-2', (63, 2), ((65, 2), (67, 4), (67, 7)))
        self.add_bezier('p2-r1-3', (67, 7), ((67, 10), (65, 13), (63, 13)))
        self.add_bezier('p2-r1-4', (63, 13), ((61, 13), (59, 10), (59, 7)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (72, 25), ((72, 22), (74, 19), (76, 19)))
        self.add_bezier('p3-r1-2', (76, 19), ((78, 19), (80, 22), (80, 25)))
        self.add_bezier('p3-r1-3', (80, 25), ((80, 28), (78, 30), (76, 30)))
        self.add_bezier('p3-r1-4', (76, 30), ((74, 30), (72, 28), (72, 25)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_bezier('p4-r1-1', (30, 11), ((30, 7), (35, 3), (40, 3)))
        self.add_bezier('p4-r1-2', (40, 3), ((45, 3), (49, 7), (49, 11)))
        self.add_line('p4-r1-3', (49, 11), (49, 22))
        self.add_bezier('p4-r1-4', (49, 22), ((49, 27), (45, 30), (40, 30)))
        self.add_bezier('p4-r1-5', (40, 30), ((35, 30), (30, 27), (30, 22)))
        self.add_line('p4-r1-6', (30, 22), (30, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.add_line('p5-r1-1', (2, 3), (19, 3))
        self.add_bezier('p5-r1-2', (19, 3), ((20, 3), (20, 3), (20, 4)))
        self.add_bezier('p5-r1-3', (20, 4), ((20, 4), (20, 4), (20, 4)))
        self.add_line('p5-r1-4', (20, 4), (8, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
