"""A toaster enclosure with a risen bread slice and a right-hand lever.

Keyshape SQUARE: centerline extremes recorded in build below.
Lucide smartphone informs the rounded appliance shell; no useful Lucide bread-slice match was found. The source provides the bread crown and deliberate side-lever asymmetry.
Hosting (compose.py): plus valid, heart review, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class KitchenToasterWithBreadSlice(Container64):
    icon_id = 'kitchen-toaster-with-bread-slice'
    keyshape = Keyshape.SQUARE
    aliases = ('toaster',)
    keywords = ('kitchen', 'toaster', 'with', 'bread', 'slice')

    def build(self) -> None:
        # SQUARE centerline extremes: (2,2)-(62,62).
        self.add_line("body-0", (5, 22), (55, 22))
        self.add_arc("body-1", (55, 22), (58, 25), radius_x=3)
        self.add_line("body-2", (58, 25), (58, 59))
        self.add_arc("body-3", (58, 59), (55, 62), radius_x=3)
        self.add_line("body-4", (55, 62), (5, 62))
        self.add_arc("body-5", (5, 62), (2, 59), radius_x=3)
        self.add_line("body-6", (2, 59), (2, 25))
        self.add_arc("body-7", (2, 25), (5, 22), radius_x=3)
        self.add_contour("body", "body-0", "body-1", "body-2", "body-3", "body-4", "body-5", "body-6", "body-7", closed=True)
        self.add_line("bread-left", (10,22), (10,14))
        self.add_arc("bread-crown-left", (10,14), (10,2), radius_x=6)
        self.add_line("bread-top", (10,2), (48,2))
        self.add_arc("bread-crown-right", (48,2), (48,14), radius_x=6)
        self.add_line("bread-right", (48,14), (48,22))
        self.add_contour("bread", "bread-left", "bread-crown-left", "bread-top", "bread-crown-right", "bread-right")
        self.relate("connect", "bread", "body")
        self.add_line("lever", (58,50), (62,50))
        self.relate("connect", "lever", "body")
