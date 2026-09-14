"""A small uneven house stands on the raised left edge of a broken ground section. A deep zigzag fissure cuts downward beside it, separating the two sides of the ground.

Reduced the fissure to one zigzag and omitted facade details; house remains perched on the left bank.
Construction reference: Lucide house pitched outline; no exact earthquake match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4d8b67a-7434-5e2f-9aa0-1b27bb3d2482'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake ground crack_b4d8b67a-7434-5e2f-9aa0-1b27bb3d2482.svg'
AUTHOR = 'gpt-6'

class HouseGroundFissure(Solo48):
    icon_id = 'house-ground-fissure'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('house', 'earthquake', 'fissure', 'crack', 'ground', 'disaster')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_polyline('house', (6, 25), (6, 17), (16, 8), (26, 17), (26, 25), closed=True)
        self.add_polyline('bank-left', (6, 40), (6, 25), (26, 25), (22, 32), (28, 35), (22, 40), closed=False)
        self.relate("connect", 'house', 'bank-left')
        self.add_polyline('bank-right', (42, 40), (42, 25), (36, 25), closed=False)
