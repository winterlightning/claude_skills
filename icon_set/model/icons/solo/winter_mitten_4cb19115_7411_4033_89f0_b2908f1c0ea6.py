"""Winter mitten with right-facing thumb and cuff. VRECT_L extremes (8,2)-(40,46). Deliberate thumb asymmetry; simplified cuff. No useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cb19115-7411-4033-89f0-b2908f1c0ea6'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/winter gloves_4cb19115-7411-4033-89f0-b2908f1c0ea6.svg'
AUTHOR = 'astra-chatgpt'


class WinterMitten(Solo48):
    icon_id = 'winter-mitten'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('mitten', 'glove', 'winter', 'cold', 'hand', 'knit', 'clothing', 'snow')

    def build(self) -> None:
        self.add_arc('dome', (8, 13), (30, 13), radius_x=11, radius_y=11, sweep=True)
        self.add_line('palm-right', (30, 13), (30, 24))
        self.add_line('thumb-rise', (30, 24), (34, 20))
        self.add_arc('thumb-tip', (34, 20), (40, 26), radius_x=6, radius_y=6, sweep=True)
        self.add_line('thumb-return', (40, 26), (30, 39))
        self.add_line('palm-base', (30, 39), (8, 39))
        self.add_line('palm-left', (8, 39), (8, 13))
        self.add_contour('mitten', 'dome', 'palm-right', 'thumb-rise', 'thumb-tip', 'thumb-return', 'palm-base', 'palm-left', closed=True)
        self.add_line('cuff-1', (8, 39), (8, 46))
        self.add_line('cuff-2', (8, 46), (30, 46))
        self.add_line('cuff-3', (30, 46), (30, 39))
        self.add_contour('cuff', 'cuff-1', 'cuff-2', 'cuff-3', closed=False)
        self.relate("connect", 'mitten', 'cuff')
