# Variant of hooked-beak-bird-head; parent file remains unchanged.
"""Hooked-beak bird head in right profile; extremes (5,2)-(43,46). Smooth crown and heavy beak; solid eye dot, deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79a4190f-e22e-5e6a-b9b2-2509c13da3ff'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird head_79a4190f-e22e-5e6a-b9b2-2509c13da3ff.svg'
AUTHOR = 'gpt-6'

class HookedBeakBirdHeadVariant2(Solo48):
    icon_id = 'hooked-beak-bird-head-v2'
    variant_of = 'hooked-beak-bird-head'
    variant_label = 'Solid eye dot'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('bird', 'head', 'beak', 'hooked', 'parrot', 'falcon', 'profile', 'raptor')

    def build(self) -> None:
        self.add_line('neck-back', (5, 46), (5, 24))
        self.add_arc('crown-left', (5, 24), (27, 2), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('crown-right', (27, 2), (37, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('face', (37, 12), (29, 29), radius_x=20, radius_y=20, sweep=True)
        self.add_line('neck-front', (29, 29), (29, 46))
        self.add_contour('head', 'neck-back', 'crown-left', 'crown-right', 'face', 'neck-front', closed=False)
        self.add_arc('beak-upper', (37, 12), (43, 29), radius_x=6, radius_y=17, sweep=True)
        self.add_line('beak-lower', (43, 29), (29, 29))
        self.add_contour('beak', 'beak-upper', 'beak-lower', closed=False)
        self.relate('connect', 'beak', 'head')
        self.add_dot('eye', (24, 14))
