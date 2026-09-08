"""A bow tie: two wings flaring from a rounded square centre knot, on SOLO48.

Matched to the supplied batch-05 bow-tie reference; source identity retained.

Construction reference: Lucide ``hourglass``.  Its two halves flare from a
shared waist as straight diagonals closed by a short axis-aligned run, with the
corner radius doing all the softening.  The same idea is used here rotated a
quarter turn: each wing is three straight runs -- a diagonal out, a vertical
tip, a diagonal back -- and the knot's own side wall closes it, so the wing is a
flaring triangle whose fourth side is the knot.

The source's two short wing-fold strokes are omitted for clearance.  What is deliberately *not* drawn is a
seam, crease or centre fold inside the knot: a 12-unit knot has one 8-unit
interior and a second level of detail inside it does not survive 48 pixels.

Symmetric about x=24 by construction; the right wing is the left wing's
coordinates reflected through ``x_right = 48 - x_left``.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8df920a-b5e4-42ca-a8cb-d0665fd4de17'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/ribbon tie_a8df920a-b5e4-42ca-a8cb-d0665fd4de17.svg'
AUTHOR = 'astra-chatgpt'


class BowTie(Solo48):
    """A front-facing bow tie, wings spread level."""

    icon_id = "bow-tie"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/clothing"
    aliases = ("bowtie", "dickie-bow", "black-tie")
    keywords = (
        "bow tie", "bowtie", "tie", "necktie", "knot", "formal", "black tie",
        "tuxedo", "dress code", "clothing", "accessory",
    )

    # One symmetry axis and one knot half-size drive every number below.
    AXIS = 24
    KNOT = 6  # knot centreline half-size: x,y in 18..30
    KNOT_RADIUS = 3  # leaves a 6-unit straight run on each wall
    TIP_X = 2  # HRECT_M centreline left edge
    TIP_TOP = 11  # HRECT_M centreline top edge
    TIP_BOTTOM = 37  # HRECT_M centreline bottom edge

    def build(self) -> None:
        axis, half, radius = self.AXIS, self.KNOT, self.KNOT_RADIUS
        left, right = axis - half, axis + half
        top, bottom = axis - half, axis + half
        # The straight runs stop short of each corner by the corner radius, so
        # every wall is 4 long and every corner is a true quarter circle.
        near, far = axis - (half - radius), axis + (half - radius)

        # The knot: one closed clockwise contour, walls and quarter-circle
        # corners.  Its left and right walls double as the wings' inner sides,
        # which is why the wings need no fourth segment of their own.
        self.add_line("knot-top", (near, top), (far, top))
        self.add_arc("knot-corner-top-right", (far, top), (right, near), radius_x=radius, radius_y=radius)
        self.add_line("knot-right", (right, near), (right, far))
        self.add_arc("knot-corner-bottom-right", (right, far), (far, bottom), radius_x=radius, radius_y=radius)
        self.add_line("knot-bottom", (far, bottom), (near, bottom))
        self.add_arc("knot-corner-bottom-left", (near, bottom), (left, far), radius_x=radius, radius_y=radius)
        self.add_line("knot-left", (left, far), (left, near))
        self.add_arc("knot-corner-top-left", (left, near), (near, top), radius_x=radius, radius_y=radius)
        self.add_contour(
            "knot",
            "knot-top", "knot-corner-top-right", "knot-right",
            "knot-corner-bottom-right", "knot-bottom", "knot-corner-bottom-left",
            "knot-left", "knot-corner-top-left",
            closed=True,
        )

        # Each wing starts and ends on a knot wall endpoint, so the contact is a
        # shared drawn point rather than a stroke laid across a curve.  The
        # diagonals leave the knot at 32 degrees and the tip is a plain vertical
        # run, so the wing reads as a triangle flaring outward from the knot.
        # The knot is 12 across rather than the 10 first drawn: at 10 it read as
        # a bead rather than a tied square, and the 6-unit wall it now offers
        # leaves a clean 2-unit waist channel between knot and wing.
        self.add_polyline(
            "wing-left",
            (left, near), (self.TIP_X, self.TIP_TOP),
            (self.TIP_X, self.TIP_BOTTOM), (left, far),
        )
        mirror = 2 * axis - self.TIP_X
        self.add_polyline(
            "wing-right",
            (right, near), (mirror, self.TIP_TOP),
            (mirror, self.TIP_BOTTOM), (right, far),
        )

        self.relate("connect", "knot", "wing-left")
        self.relate("connect", "knot", "wing-right")
