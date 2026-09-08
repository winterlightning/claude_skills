"""Sleeveless A-line dress reconstructed on SOLO48.

The outline retains the two straps, scooped neckline, narrow waist and flared
skirt.  The reference's small folds and scallops are replaced by one broad hem
curve that remains legible under the four-unit stroke.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class Dress(Solo48):
    icon_id = "dress"
    keyshape = Keyshape.VRECT_L
    category = "objects/clothing"
    aliases = ("sleeveless-dress", "a-line-dress", "sleeveless-woman-dress")
    keywords = (
        "dress", "clothing", "fashion", "garment", "apparel",
        "womenswear", "skirt", "sleeveless",
    )

    def build(self) -> None:
        # VRECT_L's centreline envelope is (8,2)-(40,46).  The two six-unit
        # straps frame a circular scoop whose lower point lands at y=13, then
        # the bodice narrows symmetrically to the waist at y=22.
        self.add_line("strap-left-top", (13, 2), (19, 2))
        self.add_line("strap-left-inner", (19, 2), (19, 8))
        self.add_arc(
            "neckline", (19, 8), (29, 8), radius_x=5, sweep=False
        )
        self.add_line("strap-right-inner", (29, 8), (29, 2))
        self.add_line("strap-right-top", (29, 2), (35, 2))
        self.add_line("strap-right-outer", (35, 2), (35, 12))
        self.add_line("bodice-right-upper", (35, 12), (34, 17))
        self.add_line("bodice-right-lower", (34, 17), (31, 22))
        self.add_line("skirt-right-upper", (31, 22), (36, 31))
        self.add_line("skirt-right-lower", (36, 31), (40, 44))
        self.add_arc(
            "hem", (40, 44), (8, 44), radius_x=16, radius_y=2
        )
        self.add_line("skirt-left-lower", (8, 44), (12, 31))
        self.add_line("skirt-left-upper", (12, 31), (17, 22))
        self.add_line("bodice-left-lower", (17, 22), (14, 17))
        self.add_line("bodice-left-upper", (14, 17), (13, 12))
        self.add_line("strap-left-outer", (13, 12), (13, 2))
        self.add_contour(
            "outline",
            "strap-left-top", "strap-left-inner", "neckline",
            "strap-right-inner", "strap-right-top", "strap-right-outer",
            "bodice-right-upper", "bodice-right-lower", "skirt-right-upper",
            "skirt-right-lower", "hem", "skirt-left-lower",
            "skirt-left-upper", "bodice-left-lower", "bodice-left-upper",
            "strap-left-outer",
            closed=True,
        )

        self.add_line("waist-seam", (17, 22), (31, 22))
        self.relate("connect", "outline", "waist-seam")
