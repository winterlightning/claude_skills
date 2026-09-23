"""A right-facing fish swimming inside a rimmed aquarium tank."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "4fb53005-bb60-46fd-bc0e-7ea549f599e9"
SOURCE_PATH = "pictographic-primitives/_uncategorized_03/aquarium_4fb53005-bb60-46fd-bc0e-7ea549f599e9.svg"
AUTHOR = "gpt-5"


class FishInAnAquariumTank(Solo48):
    icon_id = "fish-in-an-aquarium-tank"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/aquatic"
    aliases = ("fish-swimming-in-a-tank", "aquarium-fish")
    keywords = ("aquarium", "fish", "tank", "water", "pet", "swimming")

    def build(self) -> None:
        # Plan: one rounded-square tank owns an attached upper rim and lower
        # wave. A compact right-facing fish uses one closed silhouette with a
        # forked tail, leaving nine-unit breathing bands above and below.
        self.add_line("tank-top", (10, 6), (38, 6))
        self.add_arc("tank-top-right", (38, 6), (42, 10), radius_x=4)
        self.add_line("tank-right", (42, 10), (42, 38))
        self.add_arc("tank-bottom-right", (42, 38), (38, 42), radius_x=4)
        self.add_line("tank-bottom", (38, 42), (10, 42))
        self.add_arc("tank-bottom-left", (10, 42), (6, 38), radius_x=4)
        self.add_line("tank-left", (6, 38), (6, 10))
        self.add_arc("tank-top-left", (6, 10), (10, 6), radius_x=4)
        self.add_contour(
            "tank-outline",
            "tank-top",
            "tank-top-right",
            "tank-right",
            "tank-bottom-right",
            "tank-bottom",
            "tank-bottom-left",
            "tank-left",
            "tank-top-left",
            closed=True,
        )

        self.add_line("upper-rim", (6, 14), (42, 14))
        self.relate("connect", "tank-outline", "upper-rim")

        self.add_polyline(
            "lower-wave",
            (6, 38),
            (12, 40),
            (18, 38),
            (24, 40),
            (30, 38),
            (36, 40),
            (42, 38),
        )
        self.relate("connect", "tank-outline", "lower-wave")

        self.add_polyline(
            "fish-outline",
            (33, 26),
            (29, 22),
            (24, 22),
            (20, 24),
            (17, 22),
            (15, 22),
            (17, 26),
            (15, 30),
            (17, 30),
            (20, 28),
            (24, 30),
            (29, 30),
            closed=True,
        )
