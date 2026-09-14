"""Inset the dome and base; widened the cuff band to eight centerline units. Right thumb remains asymmetric.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: No useful exact match.
"""
# Independent repair of winter-mitten; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4cb19115-7411-4033-89f0-b2908f1c0ea6'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/winter gloves_4cb19115-7411-4033-89f0-b2908f1c0ea6.svg'
AUTHOR = 'gpt-6'

class WinterMitten(Solo48):
    icon_id = 'winter-mitten'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('mitten', 'glove', 'winter', 'cold', 'hand', 'knit', 'clothing', 'snow')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_arc('dome', (8, 15), (30, 15), radius_x=11, radius_y=11, sweep=True)
        self.add_line('palm-right', (30, 15), (30, 24))
        self.add_line('thumb-rise', (30, 24), (34, 20))
        self.add_arc('thumb-tip', (34, 20), (40, 26), radius_x=6, radius_y=6, sweep=True)
        self.add_line('thumb-return', (40, 26), (30, 36))
        self.add_line('palm-base', (30, 36), (8, 36))
        self.add_line('palm-left', (8, 36), (8, 15))
        self.add_contour('mitten', 'dome', 'palm-right', 'thumb-rise', 'thumb-tip', 'thumb-return', 'palm-base', 'palm-left', closed=True)
        self.add_line('cuff-1', (8, 36), (8, 44))
        self.add_line('cuff-2', (8, 44), (30, 44))
        self.add_line('cuff-3', (30, 44), (30, 36))
        self.add_contour('cuff', 'cuff-1', 'cuff-2', 'cuff-3', closed=False)
        self.relate('connect', 'mitten', 'cuff')
