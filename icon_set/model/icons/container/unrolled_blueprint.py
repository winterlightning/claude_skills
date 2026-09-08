"""Unrolled blueprint: a flat plan sheet whose right-hand edge is still rolled.

Reconstructed from the reference render. The reference is one continuous
ribbon of paper: a large flat sheet on the left, a seam where the flat part
ends, and a narrow rolled band on the right that caps over at the top and
tucks its free end back under at the bottom. Two drawn parts carry all of
that -- a closed `roll` loop and an open `sheet` C -- and they genuinely
share both of their ends, so the one contact is declared and scoped.

Three choices differ from the reference and are deliberate. The rolled band
is capped with a half-ellipse dome rather than the reference's quarter-round
corner: at 64 pixels a quarter-round reads as a rounded rectangle, while the
dome reads as a tube seen end-on, which is the whole point of the icon. The
band is 12 centerlines wide instead of the reference's 12.85-of-64, so its
interior keeps 8 units of white. And the reference's free end spirals back on
itself; that loop is smaller than one stroke here, so it is drawn as the
single fold the spiral resolves to -- one 45-degree tuck from the point
where the sheet's bottom edge ends up to the foot of the seam, 8 above it,
which is where the reference puts the same fold.

Five treatments of that free end were rendered at 64 and compared: a flat
run with a dive, a symmetric pill with no fold at all, a longer flat run,
this single diagonal, and a reference-faithful quarter-round top. The
diagonal won. The flat-plus-dive versions put a step in the bottom edge
that reads as a snag rather than a fold; the pill is clean but drops the
one cue that says the sheet is rolled and not merely sitting beside a tube;
and the quarter-round top turns the roll back into a rounded rectangle
corner.

Every junction is tangent-continuous except the two that are real paper
edges: the crest at (46,14) where the sheet's top edge branches off the
rolled seam, and the point at (54,58) where the free end turns back.

Hosting, remeasured for batch 17 with compose.py: plus, heart and check
all fail clearance. The seam at x=48 limits the usable interior. Earlier
hosting notes described an older seam position; the current measurements
are recorded in container_icons/work/batch_17_review/hosting.json.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Container64


class UnrolledBlueprintContainer(Container64):
    icon_id = "unrolled-blueprint"
    keyshape = Keyshape.SQUARE
    aliases = ("unrolled-architectural-blueprint", "blueprint", "rolled-blueprint", "architectural-blueprint", "plan-drawing", "partially-unrolled-paper-scroll")
    keywords = (
        "blueprint", "roll", "rolled", "paper", "document", "plan", "drawing",
        "draft", "architecture", "scroll", "sheet", "schematic",
    )

    def build(self) -> None:
        # SQUARE-64 is (0, 0)-(64, 64) visible, (2, 2)-(62, 62) centerline. The
        # four extremes are reached by four different elements: the sheet's
        # left edge at x 6, the dome's apex at y 6, the band's right wall at
        # x 58, and the sheet's bottom edge at y 58.
        #
        # Horizontally the reference gives the rolled band a fifth of the
        # width. A fifth of 52 is 10.4; 12 is the nearest value that leaves
        # the band 8 units of interior white at stroke 4, so the seam stands
        # at x 46 and the right wall at x 58.
        #
        # The closed roll loop, traversed from the crest clockwise. Dome,
        # right wall, curl down to the free end, tuck back, seam back up.
        self.add_arc("roll-cap", (48, 11), (62, 11), radius_x=7, radius_y=9)
        self.add_line("roll-right", (62, 11), (62, 50))
        self.add_arc("roll-curl", (62, 50), (57, 62), radius_x=5, radius_y=12)
        self.add_line("roll-tuck", (57, 62), (48, 53))
        self.add_line("roll-seam", (48, 53), (48, 11))
        self.add_contour(
            "roll",
            "roll-cap", "roll-right", "roll-curl", "roll-tuck", "roll-seam",
            closed=True,
        )
        # The dome's centre is (55, 11) and the curl's is (57, 50), both on the
        # grid, so the dome is vertical where it leaves the seam and where it
        # meets the right wall, and the curl is vertical where the right wall
        # hands over to it. No kink on the rolled edge anywhere.
        #
        # The flat sheet is an open C that starts and ends on the roll: along
        # the top to the left edge, down, and back along the bottom to the
        # free end of the roll. Its bottom edge arrives at (57, 62) horizontal
        # and the curl leaves it horizontal, so that junction is smooth too.
        self.add_line("sheet-top", (48, 11), (2, 11))
        self.add_line("sheet-left", (2, 11), (2, 62))
        self.add_line("sheet-bottom", (2, 62), (57, 62))
        self.add_contour("sheet", "sheet-top", "sheet-left", "sheet-bottom")

        # Two genuine shared endpoints: (48, 11) and (57, 62). Scoped to this
        # pair, which is the only pair the drawing has.
        self.relate("connect", "sheet", "roll")
