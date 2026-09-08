"""Mitten with zigzag band and cuff. VRECT_XL (5,2)-(43,46) leaves room for the right thumb. One clear zigzag replaces two dense bands. Asymmetry follows the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf673e64-b56c-5df3-9a71-85add7bf8e53'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/winter gloves_bf673e64-b56c-5df3-9a71-85add7bf8e53.svg'
AUTHOR = 'astra-chatgpt'


class PatternedWinterMitten(Solo48):
    icon_id = 'patterned-winter-mitten'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('mitten', 'glove', 'winter', 'knit', 'pattern', 'zigzag', 'cold', 'clothing', 'snow')

    def build(self) -> None:
        self.add_line('side-l', (5, 37), (5, 24))
        self.add_line('side-upper', (5, 24), (5, 15))
        self.add_arc('dome', (5, 15), (31, 15), radius_x=13, radius_y=13, sweep=True, large_arc=False)
        self.add_line('finger-side', (31, 15), (31, 24))
        self.add_line('thumb-root', (31, 24), (35, 20))
        self.add_arc('thumb-cap', (35, 20), (43, 24), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('thumb-side', (43, 24), (43, 27))
        self.add_line('palm', (43, 27), (31, 37))
        self.add_line('base', (31, 37), (5, 37))
        self.add_contour('mitten', 'side-l', 'side-upper', 'dome', 'finger-side', 'thumb-root', 'thumb-cap', 'thumb-side', 'palm', 'base', closed=True)
        self.add_polyline('cuff', (5, 37), (5, 46), (31, 46), (31, 37), closed=False)
        self.relate("connect", 'mitten', 'cuff')
        self.add_polyline('knit', (5, 24), (12, 20), (20, 25), (27, 21), (31, 24), closed=False)
        self.relate("connect", 'mitten', 'knit')
