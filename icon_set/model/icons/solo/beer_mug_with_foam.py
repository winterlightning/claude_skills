"""Beer mug with a scalloped foam head on SOLO48.

Reconstructed from ``(pictoicon) - Beer Mug with Foam.svg``.  The two narrow
glass-facet strokes from the source are omitted at native size; the identifying
body, handle, foam cap, separator, and flat base remain.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48


class BeerMugWithFoam(Solo48):
    """A straight-sided beer stein with foam and a right-hand handle."""

    icon_id = "beer-mug-with-foam"
    keyshape = Keyshape.VRECT_XL
    category = "objects/drink"
    aliases = ("beer-mug", "beer-stein", "stein")
    keywords = ("beer", "mug", "stein", "drink", "pub", "bar", "alcohol", "foam")

    def build(self) -> None:
        # The foam is the top of the mug's outer contour.  A small left rise,
        # broad central lobe, and right fall preserve the scalloped read with
        # only the detail that survives at 48 pixels.  The central semicircle
        # reaches VRECT_XL's top centreline at y=2.
        self.add_arc("foam-left", (5, 15), (10, 9), radius_x=6, sweep=False)
        self.add_arc("foam-centre", (10, 9), (24, 9), radius_x=7)
        self.add_arc("foam-right", (24, 9), (34, 15), radius_x=6)

        # Split the right wall at both handle attachments so every attachment
        # is a shared endpoint that the validator can prove.
        self.add_line("wall-right-upper", (34, 15), (34, 24))
        self.add_line("wall-right-handle", (34, 24), (34, 40))
        self.add_arc("corner-se", (34, 40), (28, 46), radius_x=6)
        self.add_line("base", (28, 46), (11, 46))
        self.add_arc("corner-sw", (11, 46), (5, 40), radius_x=6)
        self.add_line("wall-left", (5, 40), (5, 15))
        self.add_contour(
            "mug-outline",
            "foam-left", "foam-centre", "foam-right",
            "wall-right-upper", "wall-right-handle",
            "corner-se", "base", "corner-sw", "wall-left",
            closed=True,
        )

        # The shared foam/body baseline reads as the horizontal separator.
        self.add_line("foam-separator", (5, 15), (34, 15))

        # An open rounded-rectangle handle uses the mug wall as its left side.
        # Its rightmost centreline reaches x=43, completing VRECT_XL.
        self.add_line("handle-top", (34, 24), (39, 24))
        self.add_arc("handle-corner-ne", (39, 24), (43, 28), radius_x=4)
        self.add_line("handle-right", (43, 28), (43, 36))
        self.add_arc("handle-corner-se", (43, 36), (39, 40), radius_x=4)
        self.add_line("handle-bottom", (39, 40), (34, 40))
        self.add_contour(
            "handle",
            "handle-top", "handle-corner-ne", "handle-right",
            "handle-corner-se", "handle-bottom",
        )

        self.relate("connect", "mug-outline", "foam-separator")
        self.relate("connect", "mug-outline", "handle")
