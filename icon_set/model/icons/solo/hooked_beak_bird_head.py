"""Hooked-beak bird head in right profile; extremes (6,6)-(42,42). Smooth crown and heavy beak; solid eye dot, deliberately asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79a4190f-e22e-5e6a-b9b2-2509c13da3ff'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird head_79a4190f-e22e-5e6a-b9b2-2509c13da3ff.svg'
AUTHOR = 'gpt-6'

class HookedBeakBirdHead(Solo48):
    icon_id = 'hooked-beak-bird-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('bird', 'head', 'beak', 'hooked', 'parrot', 'falcon', 'profile', 'raptor')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('neck-back', (6, 42), (6, 24))
        self.add_arc('crown-left', (6, 24), (27, 6), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_bezier('crown-right', (27, 6), *(((31.27520963, 6), (35.29858844, 8.06218191), (37, 12)),))
        self.add_arc('face', (37, 12), (29, 29), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_line('neck-front', (29, 29), (29, 42))
        self.add_bezier('beak-upper', (37, 12), *(((39.91841996, 13.39685011), (42, 20.61480748), (42, 29)),))
        self.add_line('beak-lower', (42, 29), (29, 29))
        self.add_line('eye', (24, 15), (24, 15))
        self.add_contour('head', *('neck-back', 'crown-left', 'crown-right', 'face', 'neck-front'), closed=False)
        self.add_contour('beak', *('beak-upper', 'beak-lower'), closed=False)
        self.relate('connect', *('beak', 'head'))
