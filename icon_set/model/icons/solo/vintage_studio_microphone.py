"""Retro broadcast microphone on a desk stand, reconstructed on SOLO48.

The reference's capsule, three split grille bars, stem, and wide foot survive
at native size.  Its small side gaps and any mounting furniture are omitted.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class VintageStudioMicrophone(Solo48):
    """A rounded broadcast microphone capsule on a stem and flat base."""

    icon_id = "vintage-studio-microphone"
    keyshape = Keyshape.VRECT_S
    category = "objects/media"
    aliases = ("vintage-microphone", "studio-microphone", "broadcast-microphone")
    keywords = (
        "microphone", "mic", "podcast", "audio", "recording", "broadcast",
        "voice", "studio", "radio",
    )

    def build(self) -> None:
        # A 16-unit-wide capsule uses two semicircular ends.  Both are split at
        # their axis extrema: the top reaches VRECT_S's y=2 centreline and the
        # bottom exposes an exact endpoint for the stand attachment.
        self.add_arc("capsule-top-left", (16, 10), (24, 2), radius_x=8)
        self.add_arc("capsule-top-right", (24, 2), (32, 10), radius_x=8)
        self.add_line("capsule-right-upper", (32, 10), (32, 16))
        self.add_line("capsule-right-lower", (32, 16), (32, 22))
        self.add_arc("capsule-bottom-right", (32, 22), (24, 30), radius_x=8)
        self.add_arc("capsule-bottom-left", (24, 30), (16, 22), radius_x=8)
        self.add_line("capsule-left-lower", (16, 22), (16, 16))
        self.add_line("capsule-left-upper", (16, 16), (16, 10))
        self.add_contour(
            "capsule",
            "capsule-top-left", "capsule-top-right",
            "capsule-right-upper", "capsule-right-lower",
            "capsule-bottom-right", "capsule-bottom-left",
            "capsule-left-lower", "capsule-left-upper",
            closed=True,
        )

        # Three evenly spaced grille rows attach directly to the capsule wall,
        # eliminating the reference's tiny side gaps.  Their open centre keeps
        # the retro slotted-grille read instead of turning into a ladder.
        for row, y in (("top", 10), ("middle", 16), ("bottom", 22)):
            left = f"grille-{row}-left"
            right = f"grille-{row}-right"
            self.add_line(left, (16, y), (20, y))
            self.add_line(right, (28, y), (32, y))
            self.relate("connect", "capsule", left)
            self.relate("connect", "capsule", right)

        # The stem shares the capsule's lower apex and the split base's centre.
        # The base reaches x=14/34 and y=46, exactly completing VRECT_S.
        self.add_line("stem", (24, 30), (24, 46))
        self.add_line("base-left", (14, 46), (24, 46))
        self.add_line("base-right", (24, 46), (34, 46))
        self.add_contour("base", "base-left", "base-right")
        self.relate("connect", "capsule", "stem")
        self.relate("connect", "stem", "base")
