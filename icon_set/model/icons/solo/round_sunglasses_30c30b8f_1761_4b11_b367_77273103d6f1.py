"""Paired round sunglasses joined by low bridge. HRECT_S extremes (2,14)-(46,34). Lucide glasses informs paired lenses and arched bridge. Short outer stubs omitted to preserve full lenses."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30c30b8f-1761-4b11-b367-77273103d6f1'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/glasses sun circle_30c30b8f-1761-4b11-b367-77273103d6f1.svg'
AUTHOR = 'astra-chatgpt'


class RoundSunglasses(Solo48):
    icon_id = 'round-sunglasses'
    keyshape = Keyshape.HRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('sunglasses', 'glasses', 'eyewear', 'round', 'shades', 'summer', 'sun', 'accessory')

    def build(self) -> None:
        self.add_arc('left-lens-0', (11, 14), (20, 24), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('left-lens-1', (20, 24), (11, 34), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('left-lens-2', (11, 34), (2, 24), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('left-lens-3', (2, 24), (11, 14), radius_x=9, radius_y=10, sweep=True)
        self.add_contour('left-lens', 'left-lens-0', 'left-lens-1', 'left-lens-2', 'left-lens-3', closed=True)
        self.add_arc('right-lens-0', (37, 14), (46, 24), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('right-lens-1', (46, 24), (37, 34), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('right-lens-2', (37, 34), (28, 24), radius_x=9, radius_y=10, sweep=True)
        self.add_arc('right-lens-3', (28, 24), (37, 14), radius_x=9, radius_y=10, sweep=True)
        self.add_contour('right-lens', 'right-lens-0', 'right-lens-1', 'right-lens-2', 'right-lens-3', closed=True)
        self.add_arc('bridge', (20, 24), (28, 24), radius_x=4, radius_y=3, sweep=True)
        self.relate("connect", 'left-lens', 'bridge')
        self.relate("connect", 'right-lens', 'bridge')
