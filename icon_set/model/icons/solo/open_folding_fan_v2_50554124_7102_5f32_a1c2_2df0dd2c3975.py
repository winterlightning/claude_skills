# Variant of open-folding-fan; parent file remains unchanged.
"""Open folding fan without the small pivot circle. HRECT_M centers the remaining fan leaf and central rib. No useful local Lucide fan match was found."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '50554124-7102-5f32-a1c2-2df0dd2c3975'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/hand fan_50554124-7102-5f32-a1c2-2df0dd2c3975.svg'
AUTHOR = 'gpt-6'

class OpenFoldingFanVariant2(Solo48):
    icon_id = 'open-folding-fan-v2'
    variant_of = 'open-folding-fan'
    variant_label = 'Remove pivot circle'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('open', 'folding', 'fan')

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
        arc('leaf-left', (2, 26), (24, 11), 22, 15)
        arc('leaf-right', (24, 11), (46, 26), 22, 15)
        line('edge-right', (46, 26), (24, 37))
        line('edge-left', (24, 37), (2, 26))
        contour('leaf', 'leaf-left', 'leaf-right', 'edge-right', 'edge-left', closed=True)
        line('rib', (24, 11), (24, 37))
        connect('leaf', 'rib')
