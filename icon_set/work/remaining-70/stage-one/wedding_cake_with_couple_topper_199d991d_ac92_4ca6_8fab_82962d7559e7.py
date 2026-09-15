# Repair: Move the bride rightward as one figure to separate the couple bodies.
"""A cake carries a two-person topper above scalloped icing; tiny faces and limbs omitted.

Construction references: Lucide heart, hand, sprout, balloon, cake, car and users-round as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '199d991d-ac92-4ca6-8fab-82962d7559e7'
SOURCE_PATH = 'pictographic-primitives/romance/wedding cake couple_199d991d-ac92-4ca6-8fab-82962d7559e7.svg'
AUTHOR = 'gpt-6'

class WeddingCakeWithCoupleTopper(Solo48):
    icon_id = 'wedding-cake-with-couple-topper'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/romance'
    aliases = ()
    keywords = ('cake', 'wedding', 'couple', 'topper', 'icing', 'celebration')

    def build(self) -> None:
        for n, x in [('groom', 16), ('bride', 34)]:
            self.add_arc(n + '-head-r', (x, 8), (x, 16), radius_x=4)
            self.add_arc(n + '-head-l', (x, 16), (x, 8), radius_x=4)
            self.add_contour(n + '-head', n + '-head-r', n + '-head-l', closed=True)
        self.add_polyline('groom-body', (12, 24), (12, 16), (16, 16), (20, 16), (20, 24))
        self.add_polyline('bride-body', (28, 24), (30, 16), (34, 16), (38, 16), (40, 24))
        self.add_polyline('cake', (4, 32), (4, 24), (12, 24), (20, 24), (28, 24), (40, 24), (44, 24), (44, 32), (44, 40), (4, 40), closed=True)
        self.relate('connect', 'groom-body', 'cake')
        self.relate('connect', 'bride-body', 'cake')
        self.relate('connect', 'groom-head', 'groom-body')
        self.relate('connect', 'bride-head', 'bride-body')
        for i, x in enumerate((4, 14, 24, 34)):
            self.add_arc(f'icing-{i}', (x, 32), (x + 10, 32), radius_x=5, radius_y=3, sweep=False)
        self.add_contour('icing', *(f'icing-{i}' for i in range(4)))
        self.relate('connect', 'icing', 'cake')
