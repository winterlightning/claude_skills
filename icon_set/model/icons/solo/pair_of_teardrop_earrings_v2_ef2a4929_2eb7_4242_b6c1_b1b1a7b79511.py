# Variant of pair-of-teardrop-earrings; parent file remains unchanged.
"""Paired teardrop earrings with enlarged radius-five studs. SQUARE preserves equal spacing and full drop width; no exact useful Lucide match was found."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ef2a4929-2eb7-4242-b6c1-b1b1a7b79511'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/earrings oriental_ef2a4929-2eb7-4242-b6c1-b1b1a7b79511.svg'
AUTHOR = 'gpt-6'

class PairOfTeardropEarringsVariant2(Solo48):
    icon_id = 'pair-of-teardrop-earrings-v2'
    variant_of = 'pair-of-teardrop-earrings'
    variant_label = 'Larger round studs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('pair', 'of', 'teardrop', 'earrings')

    def build(self) -> None:

        def line(n, a, b):
            self.add_line(n, a, b)

        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def contour(n, *parts, closed=False):
            self.add_contour(n, *parts, closed=closed)

        def connect(a, b):
            self.relate('connect', a, b)

        def circle(n, x, y, r, ry=None):
            arc(n + '-top', (x - r, y), (x + r, y), r, ry)
            arc(n + '-bottom', (x + r, y), (x - r, y), r, ry)
            contour(n, n + '-top', n + '-bottom', closed=True)
        for n, x in (('left', 11), ('right', 37)):
            circle(n + '-stud', x, 7, 5)
            line(n + '-post', (x, 12), (x, 21))
            line(n + '-side-r', (x, 21), (x + 8, 33))
            arc(n + '-lower-r', (x + 8, 33), (x + 9, 37), 9)
            arc(n + '-base', (x + 9, 37), (x - 9, 37), 9)
            arc(n + '-lower-l', (x - 9, 37), (x - 8, 33), 9)
            line(n + '-side-l', (x - 8, 33), (x, 21))
            contour(n + '-drop', n + '-side-r', n + '-lower-r', n + '-base', n + '-lower-l', n + '-side-l', closed=True)
            connect(n + '-stud', n + '-post')
            connect(n + '-post', n + '-drop')
