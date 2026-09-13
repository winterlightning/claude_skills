"""A plump toy horse on a single curved rocker, facing right."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = "gpt-6"


class RockingHorseToy(Solo48):
    icon_id = "rocking-horse-toy"
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby"
    aliases = ("rocking-horse",)
    keywords = ("horse", "rocker", "toy", "nursery", "play")

    def build(self) -> None:
        # HRECT_XL centerline extremes: (2, 5) to (46, 43).
        # The Lucide rocking-chair suggests one open rocker and two supports.
        self.add_line("back", (18, 19), (26, 19))
        self.add_line("neck", (26, 19), (30, 5))
        self.add_line("ear", (30, 5), (36, 11))
        self.add_line("forehead", (36, 11), (40, 11))
        self.add_arc("muzzle", (40, 11), (40, 23), radius_x=6)
        self.add_line("jaw", (40, 23), (36, 23))
        self.add_line("chest", (36, 23), (36, 25))
        self.add_arc("breast", (36, 25), (30, 31), radius_x=6)
        self.add_line("belly", (30, 31), (14, 31))
        self.add_arc("haunch", (14, 31), (8, 25), radius_x=6)
        self.add_arc("rump", (8, 25), (18, 19), radius_x=10, radius_y=6)
        self.add_contour("horse", "back", "neck", "ear", "forehead",
                         "muzzle", "jaw", "chest", "breast", "belly",
                         "haunch", "rump", closed=True)
        self.add_line("hind-support", (14, 31), (12, 43))
        self.add_line("front-support", (30, 31), (36, 43))
        self.add_arc("rocker-left", (2, 35), (12, 43),
                     radius_x=10, radius_y=8, sweep=False)
        self.add_line("rocker-base", (12, 43), (36, 43))
        self.add_arc("rocker-right", (36, 43), (46, 35),
                     radius_x=10, radius_y=8, sweep=False)
        self.add_contour("rocker", "rocker-left", "rocker-base", "rocker-right")
        self.relate("connect", "horse", "hind-support")
        self.relate("connect", "horse", "front-support")
        self.relate("connect", "rocker", "hind-support")
        self.relate("connect", "rocker", "front-support")
