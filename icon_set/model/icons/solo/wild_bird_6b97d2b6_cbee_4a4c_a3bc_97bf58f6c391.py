"""ostrich: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape SQUARE; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b97d2b6-cbee-4a4c-a3bc-97bf58f6c391'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird_6b97d2b6-cbee-4a4c-a3bc-97bf58f6c391.svg'
AUTHOR = 'gpt-6'


class Ostrich(Solo48):
    icon_id = 'ostrich'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('ostrich', 'emu', 'bird', 'standing', 'neck', 'legs', 'flightless', 'africa')

    def build(self) -> None:
        self.add_arc('head', (32, 9), (39, 2), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('beak-top', (39, 2), (46, 7), radius_x=7, radius_y=5, sweep=True)
        self.add_line('beak-bottom', (46, 7), (38, 12))
        self.add_line('neck-front', (38, 12), (38, 22))
        self.add_arc('breast', (38, 22), (26, 34), radius_x=12, radius_y=12, sweep=True)
        self.add_line('belly', (26, 34), (18, 34))
        self.add_line('leg-left', (18, 34), (18, 46))
        self.add_line('foot-left', (18, 46), (23, 46))
        self.add_contour('front', 'head', 'beak-top', 'beak-bottom', 'neck-front', 'breast', 'belly', 'leg-left', 'foot-left', closed=False)
        self.add_line('neck-back', (32, 9), (32, 21))
        self.add_arc('back', (32, 21), (16, 20), radius_x=15, radius_y=12, sweep=False)
        self.add_line('tail-top', (16, 20), (2, 28))
        self.add_arc('tail-bottom', (2, 28), (17, 29), radius_x=16, radius_y=10, sweep=False)
        self.add_contour('back-wing', 'neck-back', 'back', 'tail-top', 'tail-bottom', closed=False)
        self.relate("connect", 'front', 'back-wing')
        self.add_line('leg-right', (26, 34), (28, 46))
        self.add_line('foot-right', (28, 46), (34, 46))
        self.add_contour('right-leg', 'leg-right', 'foot-right', closed=False)
        self.relate("connect", 'front', 'right-leg')
