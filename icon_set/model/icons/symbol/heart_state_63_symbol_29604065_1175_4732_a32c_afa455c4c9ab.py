"""Heart: A symmetrical heart has two rounded upper lobes, a central notch, and sides tapering into one lower point. Generate this component alone; exclude Circle Frame.

Construction: Two round lobes meet a pointed lower tip; the surrounding circle is excluded.
Keyshape: HRECT_XL; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '29604065-1175-4732-a32c-afa455c4c9ab'
SOURCE_PATH = 'pictographic-primitives/state/circle heart_29604065-1175-4732-a32c-afa455c4c9ab.svg'
AUTHOR = 'gpt-6'

class HeartState63ContainerSymbol(Sub32):
    icon_id = 'heart-state-63-symbol'
    related_origin_icon_id = 'heart-state-63'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/heart-state-63'
    counterpart_icon_id = 'heart-state-63'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('heart', 'symmetrical', 'rounded', 'upper', 'lobes', 'central', 'notch', 'sides')

    def build(self):
        self.add_arc('lobe-left-inner', (16, 8), (10, 4), radius_x=6, radius_y=4, sweep=False)
        self.add_arc('lobe-left-outer', (10, 4), (2, 12), radius_x=8, sweep=False)
        self.add_arc('shoulder-left', (2, 12), (6, 20), radius_x=10, sweep=False)
        self.add_line('side-left', (6, 20), (16, 28))
        self.add_line('side-right', (16, 28), (26, 20))
        self.add_arc('shoulder-right', (26, 20), (30, 12), radius_x=10, sweep=False)
        self.add_arc('lobe-right-outer', (30, 12), (22, 4), radius_x=8, sweep=False)
        self.add_arc('lobe-right-inner', (22, 4), (16, 8), radius_x=6, radius_y=4, sweep=False)
        self.add_contour('outline', 'lobe-left-inner', 'lobe-left-outer', 'shoulder-left', 'side-left', 'side-right', 'shoulder-right', 'lobe-right-outer', 'lobe-right-inner', closed=True)
