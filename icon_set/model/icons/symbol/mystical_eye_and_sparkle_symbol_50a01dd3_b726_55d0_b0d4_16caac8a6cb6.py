"""A horizontal almond eye with a tall central iris and a small four-point sparkle above/right. Keep both parts as the tarot content motif; exclude the card frame.

Plan: Almond eye with a tall stroke iris and a separate upper-right diamond sparkle. Hollow iris reduced to one stroke at 32. Bounds (2,2)-(30,30).
Construction reference: No close Lucide subject; use simple connected contours."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '50a01dd3-b726-55d0-b0d4-16caac8a6cb6'
SOURCE_PATH = 'pictographic-primitives/other/fortune telling tarot_50a01dd3-b726-55d0-b0d4-16caac8a6cb6.svg'
SOURCE_ICON_IDS = ('50a01dd3-b726-55d0-b0d4-16caac8a6cb6',)
AUTHOR = 'gpt-6'

class MysticalEyeAndSparkleSymbol(Symbol32):
    icon_id = 'mystical-eye-and-sparkle-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('mystical', 'eye', 'and', 'sparkle', 'symbol')

    def build(self) -> None:
        self.add_bezier('eye-top',(2,25),((6,22),(11,20),(16,20)),((21,20),(26,22),(30,25)))
        self.add_bezier('eye-bottom',(30,25),((26,28),(21,30),(16,30)),((11,30),(6,28),(2,25)))
        self.add_contour('eye','eye-top','eye-bottom',closed=True)
        self.add_line('iris',(16,20),(16,30))
        self.relate('connect','eye','iris')
        self.add_polyline('sparkle',(24,2),(30,8),(24,14),(18,8),closed=True)
