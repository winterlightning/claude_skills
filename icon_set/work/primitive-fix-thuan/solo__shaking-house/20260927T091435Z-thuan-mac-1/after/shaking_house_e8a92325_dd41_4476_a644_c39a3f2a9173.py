"""A front-facing house has a pitched roof and a rounded doorway centered in its square body. Four detached angular tremor strokes surround the corners of the building.

Restored the doorway and set two separated side tremors around a clear central house.
Construction reference: Lucide house: continuous pitched outline.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e8a92325-dd41-4476-a644-c39a3f2a9173'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shaking-house/20260927T091435Z-thuan-mac-1/reference/earthquake house shaking_e8a92325-dd41-4476-a644-c39a3f2a9173.svg'
AUTHOR = 'gpt-6'

class ShakingHouse(Solo48):
    icon_id = 'shaking-house'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    categories = ("weather", "primitives")
    aliases = ()
    keywords = ('house', 'earthquake', 'shaking', 'tremor', 'vibration', 'disaster')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        # The door and broken corner vibration strokes carry the earthquake reading.
        self.add_polyline('house', (12, 40), (12, 22), (24, 8), (36, 22), (36, 40), closed=False)
        self.add_polyline('base-left', (12, 40), (20, 40))
        self.add_polyline('door', (20, 40), (20, 31), (24, 27), (28, 31), (28, 40))
        self.add_polyline('base-right', (28, 40), (36, 40))
        self.relate('connect','house','base-left')
        self.relate('connect','house','base-right')
        self.relate('connect','base-left','door')
        self.relate('connect','base-right','door')
        self.add_polyline('tremor-left', (4, 20), (4, 32))
        self.add_polyline('tremor-right', (44, 20), (44, 32))
