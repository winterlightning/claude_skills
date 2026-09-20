"""Compact source composition. User allows stroke and spacing exceptions for the inner characters."""
from ._base import Sub32
from ...keyshapes import Keyshape
SOURCE_ICON_ID='eba39542-9146-4913-b251-ee6a2d0da885'
SOURCE_PATH='pictographic-primitives/state/messages bubble circle bitcoin_eba39542-9146-4913-b251-ee6a2d0da885.svg'
AUTHOR="gpt-6"
TYPEFACE_GLYPH_IDS=('symbol-bitcoin',)
COMPACT_EXCEPTION = "User requested smaller inner symbols, allowing sub stroke/grid/spacing exceptions instead of enlargement."
class Drawing(Sub32):
    icon_id='bitcoin-sign-state-169-v3'
    variant_of='bitcoin-sign-state-169-v2'
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
        self.add_line('glyph-p1-r1-1', (11, 18), (11, 10))
        self.add_line('glyph-p1-r1-2', (11, 10), (17, 10))
        self.add_bezier('glyph-p1-r1-3', (17, 10), ((22.323863636363633, 9.545454545454545), (22.323863636363633, 14), (17, 14)))
        self.add_line('glyph-p1-r1-4', (17, 14), (11, 14))
        self.add_contour('glyph-path-1-1', 'glyph-p1-r1-1', 'glyph-p1-r1-2', 'glyph-p1-r1-3', 'glyph-p1-r1-4', closed=False)
        self.add_bezier('glyph-p2-r1-1', (17, 14), ((22.642045454545453, 14), (22.642045454545453, 18.454545454545453), (17, 18)))
        self.add_line('glyph-p2-r1-2', (17, 18), (11, 18))
        self.add_contour('glyph-path-2-1', 'glyph-p2-r1-1', 'glyph-p2-r1-2', closed=False)
        self.add_line('glyph-p3-r1-1', (12, 7), (12, 10))
        self.add_contour('glyph-path-3-1', 'glyph-p3-r1-1', closed=False)
        self.add_line('glyph-p4-r1-1', (17, 7), (17, 10))
        self.add_contour('glyph-path-4-1', 'glyph-p4-r1-1', closed=False)
        self.add_line('glyph-p5-r1-1', (12, 18), (12, 21))
        self.add_contour('glyph-path-5-1', 'glyph-p5-r1-1', closed=False)
        self.add_line('glyph-p6-r1-1', (17, 18), (17, 21))
        self.add_contour('glyph-path-6-1', 'glyph-p6-r1-1', closed=False)
        self.relate("connect", 'glyph-p1-r1-1', 'glyph-p2-r1-2')
        self.relate("connect", 'glyph-p1-r1-2', 'glyph-p4-r1-1')
        self.relate("connect", 'glyph-p1-r1-3', 'glyph-p2-r1-1')
        self.relate("connect", 'glyph-p1-r1-3', 'glyph-p4-r1-1')
        self.relate("connect", 'glyph-p1-r1-4', 'glyph-p2-r1-1')
        self.relate("connect", 'glyph-p2-r1-1', 'glyph-p6-r1-1')
        self.relate("connect", 'glyph-p2-r1-2', 'glyph-p6-r1-1')
        self.relate('connect','glyph-path-2-1','glyph-path-1-1')
        self.relate('connect','glyph-path-3-1','glyph-path-1-1')
        self.relate('connect','glyph-path-4-1','glyph-path-1-1')
        self.relate('connect','glyph-path-5-1','glyph-path-2-1')
        self.relate('connect','glyph-path-6-1','glyph-path-2-1')
        self.add_line('serif-top',(10,10),(11,10))
        self.add_line('serif-bottom',(10,18),(11,18))

    def to_record(self):
        record=super().to_record()
        record["style"]["path_stroke_widths"]=dict(self.PATH_STROKE_WIDTHS)
        record["compact_exception"]=COMPACT_EXCEPTION
        return record
