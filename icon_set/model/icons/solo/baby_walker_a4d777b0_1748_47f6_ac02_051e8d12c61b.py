"""Baby walker with tray, hanging seat and wide floor base; tray thickness simplified to one line."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4d777b0-1748-47f6-ac02-051e8d12c61b'
SOURCE_PATH = 'pictographic-primitives/babies/walker waling car_a4d777b0-1748-47f6-ac02-051e8d12c61b.svg'
AUTHOR = 'gpt-6'


class BabyWalker(Solo48):
    icon_id = 'baby-walker'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby"
    aliases = ()
    keywords = ('baby', 'walker', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        # Centerline keyshape: HRECT_L; Baby walker with tray, hanging seat and wide floor base; tray thickness simplified to one line.
        self.add_polyline('tray', (2, 8), (8, 8), (18, 8), (34, 8), (46, 8), closed=False)
        self.add_polyline('frame', (8, 8), (8, 40), (2, 40), closed=False)
        self.relate("connect", 'frame', 'tray')
        self.add_polyline('base', (8, 40), (38, 40), (46, 40), closed=False)
        self.relate("connect", 'frame', 'base')
        self.add_line('front-leg', (38, 28), (38, 40))
        self.relate("connect", 'front-leg', 'base')
        self.add_line('seat-left', (18, 8), (18, 16))
        self.add_arc('seat-curve', (18, 16), (30, 28), radius_x=12, radius_y=12, sweep=False)
        self.add_line('seat-bottom', (30, 28), (38, 28))
        self.add_contour('seat', 'seat-left', 'seat-curve', 'seat-bottom', closed=False)
        self.relate("connect", 'seat', 'tray')
        self.relate("connect", 'seat', 'front-leg')
