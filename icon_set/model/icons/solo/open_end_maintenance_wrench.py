"""Diagonal open-end maintenance wrench on SOLO48.

Reconstructed from ``(pictoicon) - Open End Maintenance Wrench.svg`` as one
closed silhouette.  The source's jaw fillets and handle taper are reduced to a
round inner jaw and two parallel shaft edges, preserving the native-size read.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class OpenEndMaintenanceWrench(Solo48):
    """A constant-width wrench rising from lower-left to upper-right."""

    icon_id = "open-end-maintenance-wrench"
    keyshape = Keyshape.SQUARE
    category = "objects/tool"
    aliases = ("open-end-wrench", "wrench", "spanner")
    keywords = ("wrench", "spanner", "tool", "maintenance", "repair", "settings", "fix")

    def build(self) -> None:
        # Start at the upper jaw tip and travel around the jaw recess, head,
        # parallel-sided shaft, angled butt, and back around the head.  The two
        # jaw tips stay unbridged while the outline itself remains closed.
        # Each head side is a belly arc plus a small fillet arc so the head
        # meets the shaft tangentially: a kink mid-contour is what makes an
        # otherwise-correct icon read wrong.  The upper belly is elliptical
        # (rx 7, ry 6) so its crest lands exactly on the tip endpoint instead
        # of overshooting the keyshape.
        # Widen the upper jaw band: the former inner corner at (30,10)
        # crowded the outer head. Move it to (33,10), with a longer upper tip,
        # so the opposing curves retain visible white space under stroke 4.
        self.add_line("jaw-upper-inner", (40, 2), (33, 10))
        self.add_arc("jaw-recess", (33, 10), (38, 18), radius_x=8, sweep=False)
        self.add_line("jaw-lower-inner", (38, 18), (46, 10))
        self.add_line("jaw-lower-tip", (46, 10), (46, 18))
        self.add_arc("head-lower-belly", (46, 18), (36, 24), radius_x=7)
        self.add_arc("head-lower-fillet", (36, 24), (30, 25), radius_x=5, sweep=False)
        self.add_line("shaft-lower", (30, 25), (9, 46))
        # Rounded butt: an r6 arc reads as a full handle end instead of a
        # pointed corner.  Tighter radii would overshoot the keyshape, so the
        # corners stay on the bounds and the arc gives what roundness fits.
        self.add_arc("butt", (9, 46), (2, 39), radius_x=7)
        self.add_line("shaft-upper", (2, 39), (25, 16))
        self.add_arc("head-upper-fillet", (25, 16), (26, 11), radius_x=5, sweep=False)
        self.add_arc(
            "head-upper-belly", (26, 11), (33, 2),
            radius_x=8, radius_y=7,
        )
        self.add_line("jaw-upper-tip", (33, 2), (40, 2))
        self.add_contour(
            "wrench-outline",
            "jaw-upper-inner", "jaw-recess", "jaw-lower-inner",
            "jaw-lower-tip", "head-lower-belly", "head-lower-fillet",
            "shaft-lower", "butt", "shaft-upper",
            "head-upper-fillet", "head-upper-belly", "jaw-upper-tip",
            closed=True,
        )
