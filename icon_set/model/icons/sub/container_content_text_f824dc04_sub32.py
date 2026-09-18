"""Independent 32px profile of container-content-text-f824dc04.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/dist/text44/container-content-text-f824dc04.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = ()
PROFILE_SOURCE_KEYS = ('text/container-content-text-f824dc04',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '99885a6ed5fd2441663da07948d3eb43f391a7d27c68916aee5a9146c47acd1c'

class Drawing(TextSub32):
    icon_id = 'container-content-text-f824dc04-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 59
    text_ink_bounds = (0.0, 0.0, 59.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (57, 8), ((56, 6), (53, 5), (50, 5)))
        self.add_bezier('p1-r1-2', (50, 5), ((47, 5), (43, 7), (43, 11)))
        self.add_bezier('p1-r1-3', (43, 11), ((43, 11), (43, 11), (43, 11)))
        self.add_bezier('p1-r1-4', (43, 11), ((43, 18), (57, 14), (57, 21)))
        self.add_bezier('p1-r1-5', (57, 21), ((57, 22), (57, 22), (57, 22)))
        self.add_bezier('p1-r1-6', (57, 22), ((57, 26), (53, 28), (50, 28)))
        self.add_bezier('p1-r1-7', (50, 28), ((46, 28), (43, 27), (42, 25)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (50, 2), (50, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (4, 11), (5, 11))
        self.add_line('p3-r1-2', (5, 11), (27, 11))
        self.add_line('p3-r1-3', (27, 11), (28, 11))
        self.add_arc('p3-r1-4', (28, 11), (30, 13), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-5', (30, 13), (30, 18))
        self.add_line('p3-r1-6', (30, 18), (30, 24))
        self.add_arc('p3-r1-7', (30, 24), (28, 25), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-8', (28, 25), (27, 25))
        self.add_line('p3-r1-9', (27, 25), (22, 25))
        self.add_line('p3-r1-10', (22, 25), (10, 25))
        self.add_line('p3-r1-11', (10, 25), (5, 25))
        self.add_line('p3-r1-12', (5, 25), (4, 25))
        self.add_arc('p3-r1-13', (4, 25), (2, 24), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('p3-r1-14', (2, 24), (2, 18))
        self.add_line('p3-r1-15', (2, 18), (2, 13))
        self.add_arc('p3-r1-16', (2, 13), (4, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', 'p3-r1-12', 'p3-r1-13', 'p3-r1-14', 'p3-r1-15', 'p3-r1-16', closed=False)
        self.add_line('p4-r1-1', (5, 11), (10, 2))
        self.add_line('p4-r1-2', (10, 2), (22, 2))
        self.add_line('p4-r1-3', (22, 2), (27, 11))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (5, 25), (5, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (27, 25), (27, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-3')
        self.relate("connect", 'p3-r1-3', 'p4-r1-3')
        self.relate("connect", 'p3-r1-8', 'p6-r1-1')
        self.relate("connect", 'p3-r1-9', 'p6-r1-1')
        self.relate("connect", 'p3-r1-11', 'p5-r1-1')
        self.relate("connect", 'p3-r1-12', 'p5-r1-1')
