# Variant of pelican-on-water; parent file remains unchanged.
'A pelican floating on water with the short underline beneath its folded wing removed. SQUARE extremes (2,2)-(46,46) preserve the bill, neck and water. Lucide bird informs the sparse curved profile. Left-facing asymmetry is intentional.'
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
        self.add_line('outline-1', (2, 14), (18, 8))
        self.add_arc('outline-2', (18, 8), (26, 2), radius_x=8, radius_y=6, sweep=True)
        self.add_arc('outline-3', (26, 2), (34, 10), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('outline-4', (34, 10), (30, 22), radius_x=18, radius_y=18, sweep=True)
        self.add_line('outline-5', (30, 22), (25, 28))
        self.add_arc('outline-6', (25, 28), (46, 23), radius_x=12, radius_y=9, sweep=False)
        self.add_arc('outline-7', (46, 23), (33, 36), radius_x=13, radius_y=13, sweep=True)
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=False)
        self.add_line('pouch-1', (2, 14), (20, 14))
        self.add_arc('pouch-2', (20, 14), (2, 14), radius_x=9, radius_y=11, sweep=True)
        self.add_contour('pouch', 'pouch-1', 'pouch-2', closed=False)
        self.add_line('neck-1', (20, 14), (15, 28))
        self.add_arc('neck-2', (15, 28), (17, 35), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('neck', 'neck-1', 'neck-2', closed=False)
        self.add_arc('water-1', (2, 43), (24, 43), radius_x=11, radius_y=3, sweep=False)
        self.add_arc('water-2', (24, 43), (46, 43), radius_x=11, radius_y=3, sweep=False)
        self.add_contour('water', 'water-1', 'water-2', closed=False)
        self.relate("connect", 'outline', 'pouch')
        self.relate("connect", 'pouch', 'neck')
