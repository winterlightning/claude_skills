"""A pelican floating on water with the short underline beneath its folded wing removed. SQUARE extremes (6,6)-(42,42) preserve the bill, neck and water. Lucide bird informs the sparse curved profile. Left-facing asymmetry is intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a64f3ff4-3dac-4e77-9941-a21f45a74c31'
SOURCE_PATH = 'pictographic-primitives/animals/pelican_a64f3ff4-3dac-4e77-9941-a21f45a74c31.svg'
AUTHOR = 'gpt-6'

class PelicanOnWaterVariant2(Solo48):
    icon_id = 'pelican-on-water-v2'
    variant_of = 'pelican-on-water'
    variant_label = 'Remove underline beneath wing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ('pelican',)
    keywords = ('pelican', 'water', 'bird', 'pouch', 'beak', 'sea', 'float', 'waterfowl')

    def build(self) -> None:
        self.add_arc('head-left', (20, 14), (28, 6), radius_x=8)
        self.add_arc('head-right', (28, 6), (36, 14), radius_x=8)
        self.add_arc('neck-back', (36, 14), (30, 24), radius_x=12)
        self.add_line('wing-root', (30, 24), (26, 26))
        self.add_arc('wing-upper', (26, 26), (42, 22), radius_x=16, radius_y=4, sweep=False)
        self.add_arc('wing-lower', (42, 22), (32, 32), radius_x=10)
        self.add_contour('outline', 'head-left', 'head-right', 'neck-back', 'wing-root', 'wing-upper', 'wing-lower')
        self.add_line('bill-top', (6, 14), (20, 14))
        self.add_arc('bill-pouch', (20, 14), (6, 14), radius_x=7, radius_y=6)
        self.add_contour('pouch', 'bill-top', 'bill-pouch', closed=True)
        self.add_line('neck-front', (20, 14), (15, 26))
        self.add_arc('breast', (15, 26), (17, 32), radius_x=6, sweep=False)
        self.add_contour('neck', 'neck-front', 'breast')
        self.relate('connect', 'outline', 'pouch')
        self.relate('connect', 'outline', 'neck')
        self.relate('connect', 'pouch', 'neck')
        self.add_arc('wave-up', (6, 41), (24, 41), radius_x=9, radius_y=1)
        self.add_arc('wave-down', (24, 41), (42, 41), radius_x=9, radius_y=1, sweep=False)
        self.add_contour('water', 'wave-up', 'wave-down')
