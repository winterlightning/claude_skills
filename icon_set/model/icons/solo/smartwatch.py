"""Square smartwatch with an open strap, reconstructed on SOLO48.

Traced from `(pictoicon) - Square Smartwatch Device.svg`, then re-authored on
the 48 canvas. This is a new drawing of the same subject, not a scaled copy of
the earlier 64-unit one: SOLO48's grid, its centerline minimum of 8 and its
SQUARE keyshape (5,5)-(43,43) centerline each set their own numbers.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = 'dcd267cd-6f18-4751-b281-118f4c4d05e0'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/watch_dcd267cd-6f18-4751-b281-118f4c4d05e0.svg'
AUTHOR = 'astra-chatgpt'


class Smartwatch(Solo48):
    """A square smartwatch case with an open strap sweeping right.

    The source draws four separate runs of sampled points: two long outer strap
    edges sweeping from the case's left side around to the right, and two short
    inner edges that converge with them at each strap tip. The case keeps the
    source's proportions -- half the canvas wide, corner radius one sixth of
    its width -- and its position left of centre so the strap has room.

    Each strap edge begins on a case wall and the two edges of a strap share
    their tip, so the whole drawing is one connected component, exactly as in
    the source. That is also what keeps the spacing engine from reading a
    strap's own width as a clearance failure.
    """

    icon_id = "smartwatch"
    keyshape = Keyshape.SQUARE
    category = "objects/device"
    aliases = ("watch", "wearable", "smart-watch")
    keywords = ("watch", "wearable", "device", "strap", "band", "time")

    def build(self) -> None:
        # Case: centreline (2, 9)-(30, 39), corner radius 4. The top and bottom
        # edges are split at the strap attachments so each strap *shares* an
        # endpoint with the case. Attaching mid-edge instead leaves an arc
        # merely touching a line, which the spacing engine will not certify as
        # a connection -- it proves only shared endpoints and straight-straight
        # intersections -- and the whole drawing comes back `review`.
        self.add_line("case-top-left", (7, 9), (8, 9))
        self.add_line("case-top", (8, 9), (23, 9))
        self.add_line("case-top-right", (23, 9), (25, 9))
        self.add_arc("case-corner-ne", (25, 9), (30, 14), radius_x=5)
        self.add_line("case-right", (30, 14), (30, 34))
        self.add_arc("case-corner-se", (30, 34), (25, 39), radius_x=5)
        self.add_line("case-bottom-right", (25, 39), (23, 39))
        self.add_line("case-bottom", (23, 39), (8, 39))
        self.add_line("case-bottom-left", (8, 39), (7, 39))
        self.add_arc("case-corner-sw", (7, 39), (2, 34), radius_x=5)
        self.add_line("case-left", (2, 34), (2, 14))
        self.add_arc("case-corner-nw", (2, 14), (7, 9), radius_x=5)
        self.add_contour(
            "case",
            "case-top-left", "case-top", "case-top-right",
            "case-corner-ne", "case-right", "case-corner-se",
            "case-bottom-right", "case-bottom", "case-bottom-left",
            "case-corner-sw", "case-left", "case-corner-nw",
            closed=True,
        )

        # Upper strap. The outer edge leaves the case wall, crests on the
        # keyshape's top edge, runs level, and falls to the keyshape's right
        # edge; the inner edge runs from the case wall to the same tip.
        # Both arcs are chosen so the axis extreme is the endpoint itself,
        # which on the integer grid pins the geometry: for a rise of b units
        # from the case edge to an apex a units along, the only radius whose
        # apex lands on the endpoint is (a*a + b*b) / 2b. From the case top at
        # y 9 to the keyshape top at y 2, b is 7, and a = 7 is the reach that
        # makes that whole -- a quarter circle centred on (15, 9), leaving the
        # case vertically and meeting the crest horizontally. The fall solves
        # the same way at r 15, putting its rightmost point exactly on (46,
        # 17). Neither arc can then bulge past the keyshape.
        self.add_arc("strap-top-outer-rise", (8, 9), (15, 2), radius_x=7)
        self.add_line("strap-top-outer-crest", (15, 2), (31, 2))
        self.add_arc("strap-top-outer-fall", (31, 2), (46, 17), radius_x=15)
        self.add_contour(
            "strap-top-outer",
            "strap-top-outer-rise", "strap-top-outer-crest", "strap-top-outer-fall",
        )
        self.add_arc("strap-top-inner", (23, 9), (31, 2), radius_x=16)

        # Lower strap: the mirror about y = 24. The case sits on the canvas
        # centre here (the source's one-unit drop does not survive the 48
        # grid), so both straps use the same radii.
        self.add_arc("strap-bottom-outer-fall", (8, 39), (15, 46), radius_x=7, sweep=False)
        self.add_line("strap-bottom-outer-trough", (15, 46), (31, 46))
        self.add_arc("strap-bottom-outer-rise", (31, 46), (46, 31), radius_x=15, sweep=False)
        self.add_contour(
            "strap-bottom-outer",
            "strap-bottom-outer-fall", "strap-bottom-outer-trough", "strap-bottom-outer-rise",
        )
        self.add_arc("strap-bottom-inner", (23, 39), (31, 46), radius_x=16, sweep=False)

        for part in ("strap-top-outer", "strap-top-inner",
                     "strap-bottom-outer", "strap-bottom-inner"):
            self.relate("connect", "case", part)
        self.relate("connect", "strap-top-outer", "strap-top-inner")
        self.relate("connect", "strap-bottom-outer", "strap-bottom-inner")
