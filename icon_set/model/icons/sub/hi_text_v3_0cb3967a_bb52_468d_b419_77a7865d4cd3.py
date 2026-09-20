"""Compact source composition. User allows stroke and spacing exceptions for the inner characters."""
from ._base import Sub32
from ...keyshapes import Keyshape
SOURCE_ICON_ID='0cb3967a-bb52-468d-b419-77a7865d4cd3'
SOURCE_PATH='pictographic-primitives/state/messages bubble round hi_0cb3967a-bb52-468d-b419-77a7865d4cd3.svg'
AUTHOR="gpt-6"
TYPEFACE_GLYPH_IDS=('letter-h-uppercase', 'letter-i-uppercase')
COMPACT_EXCEPTION = "User requested smaller inner symbols, allowing sub stroke/grid/spacing exceptions instead of enlargement."
class Drawing(Sub32):
    icon_id='hi-text-v3'
    variant_of='hi-text-v2'
    variant_label="Compact inner symbol"
    keyshape=Keyshape.SQUARE
    STROKE_WIDTH=2
    PATH_STROKE_WIDTHS={"frame":4}
    semantic_role="SUB"
    semantic_kind="modifier"
    category="primitives/mark"
    def build(self):
        self.add_bezier('top-left',(16,2),((8,2),(2,7),(2,14)))
        self.add_bezier('lower-left',(2,14),((2,19),(4,22),(8,24)))
        self.add_line('tail-left',(8,24),(4,30))
        self.add_line('tail-right',(4,30),(11,26))
        self.add_bezier('bottom',(11,26),((20,29),(30,24),(30,14)))
        self.add_bezier('top-right',(30,14),((30,7),(24,2),(16,2)))
        self.add_contour('frame','top-left','lower-left','tail-left','tail-right','bottom','top-right',closed=True)
        self.add_line('h-p1-r1-1', (8, 9), (8, 19))
        self.add_contour('h-path-1-1', 'h-p1-r1-1', closed=False)
        self.add_line('h-p2-r1-1', (16, 9), (16, 19))
        self.add_contour('h-path-2-1', 'h-p2-r1-1', closed=False)
        self.add_line('h-p3-r1-1', (8, 14), (16, 14))
        self.add_contour('h-path-3-1', 'h-p3-r1-1', closed=False)
        self.relate('connect','h-path-3-1','h-path-1-1')
        self.relate('connect','h-path-3-1','h-path-2-1')
        self.add_line('plain-i',(21,9),(21,19))

    def to_record(self):
        record=super().to_record()
        record["style"]["path_stroke_widths"]=dict(self.PATH_STROKE_WIDTHS)
        record["compact_exception"]=COMPACT_EXCEPTION
        return record
