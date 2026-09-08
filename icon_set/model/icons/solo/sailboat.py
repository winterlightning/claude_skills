"""Single-sail boat reconstructed on SOLO48.

The drawing keeps only the reference's three-part read: a flat-topped hull, a
central mast and one wind-filled sail.  Rigging, a second sail, water and the
mast tip above the sail are omitted at native size.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class Sailboat(Solo48):
    icon_id = "sailboat"
    keyshape = Keyshape.SQUARE
    category = "objects/transport"
    aliases = ("sailing-boat", "sailing-boat-with-single-sail")
    keywords = (
        "boat", "sailboat", "sail", "sailing", "ship", "nautical",
        "travel", "sea",
    )

    def build(self) -> None:
        # The sail rises from the masthead and opens into a broad triangular
        # panel.  A shallow circular arc gives its leech a wind-filled belly
        # without turning the panel into a rectangular block at native size.
        self.add_arc("sail-leech", (24, 2), (41, 24), radius_x=28)
        self.add_line("sail-foot", (41, 24), (24, 24))
        self.add_line("sail-luff", (24, 24), (24, 2))
        self.add_contour(
            "sail",
            "sail-leech", "sail-foot", "sail-luff",
            closed=True,
        )

        # Nine centreline units separate sail and gunwale, leaving real margin
        # beyond SOLO48's minimum even though both neighbouring shapes curve.
        # The mast extension bridges that opening and shares an endpoint with
        # both contours.
        self.add_line("mast", (24, 24), (24, 34))

        # SQUARE's centreline envelope is (2, 2)-(46, 46).  The gunwale is split
        # at the mast, and two mirrored quarter ellipses give the hull a broad
        # U profile while reaching the side and bottom extremes exactly.
        self.add_line("gunwale-left", (2, 34), (24, 34))
        self.add_line("gunwale-right", (24, 34), (46, 34))
        self.add_arc(
            "hull-starboard", (46, 34), (36, 46),
            radius_x=10, radius_y=12,
        )
        self.add_line("hull-keel", (36, 46), (12, 46))
        self.add_arc(
            "hull-port", (12, 46), (2, 34),
            radius_x=10, radius_y=12,
        )
        self.add_contour(
            "hull",
            "gunwale-left", "gunwale-right", "hull-starboard",
            "hull-keel", "hull-port",
            closed=True,
        )
        self.relate("connect", "sail", "mast")
        self.relate("connect", "mast", "hull")
