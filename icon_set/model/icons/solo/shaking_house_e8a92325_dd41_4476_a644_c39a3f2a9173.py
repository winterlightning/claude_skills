"""A front-facing house has a pitched roof and a rounded doorway centered in its square body. Four detached angular tremor strokes surround the corners of the building.

Reduced four tremor marks to two side zigzags and omitted doorway; retained central house and shaking motion.
Construction reference: Lucide house: continuous pitched outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8a92325-dd41-4476-a644-c39a3f2a9173'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake house shaking_e8a92325-dd41-4476-a644-c39a3f2a9173.svg'
AUTHOR = 'gpt-6'

class ShakingHouse(Solo48):
    icon_id = 'shaking-house'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('house', 'earthquake', 'shaking', 'tremor', 'vibration', 'disaster')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_polyline('house', (14, 40), (14, 21), (24, 8), (34, 21), (34, 40), closed=True)
        self.add_polyline('tremor-left', (6, 13), (6, 21), (6, 29), closed=False)
        self.add_polyline('tremor-right', (42, 13), (42, 21), (42, 29), closed=False)
