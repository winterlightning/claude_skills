"""Round the walker frame foot into the base and shorten the hanging seat wall to enlarge the open space under the tray.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a4d777b0-1748-47f6-ac02-051e8d12c61b'
SOURCE_PATH = 'pictographic-primitives/babies/walker waling car_a4d777b0-1748-47f6-ac02-051e8d12c61b.svg'
AUTHOR = 'gpt-6'

class BabyWalker(Solo48):
    icon_id = 'baby-walker-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby'
    aliases = ()
    keywords = ('baby', 'walker', 'baby', 'nursery', 'toy')

    def build(self) -> None:
        self.add_polyline('tray', (4, 8), (8, 8), (18, 8), (34, 8), (44, 8), closed=False)
        self.add_line('frame', (8, 8), (8, 36))
        self.add_arc('frame-foot', (8, 36), (12, 40), radius_x=4, sweep=False)
        self.relate('connect', 'frame', 'frame-foot')
        self.relate('connect', 'frame-foot', 'base')
        self.relate('connect', 'frame', 'tray')
        self.add_polyline('base', (4, 40), (12, 40), (38, 40), (44, 40), closed=False)
        self.add_line('front-leg', (38, 28), (38, 40))
        self.relate('connect', 'front-leg', 'base')
        self.add_line('seat-left', (18, 8), (18, 16))
        self.add_arc('seat-curve', (18, 16), (30, 28), radius_x=12, radius_y=12, sweep=False)
        self.add_line('seat-bottom', (30, 28), (38, 28))
        self.add_contour('seat', 'seat-left', 'seat-curve', 'seat-bottom', closed=False)
        self.relate('connect', 'seat', 'tray')
        self.relate('connect', 'seat', 'front-leg')
    variant_of = 'baby-walker'
    variant_label = 'Batch 01 centerline repair'
