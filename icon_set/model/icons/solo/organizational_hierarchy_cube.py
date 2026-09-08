"""Parent cube distributed through a hierarchy to three child nodes."""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class OrganizationalHierarchyCube(Solo48):
    """An isometric cube feeding an even row of three circular children."""

    icon_id = "organizational-hierarchy-cube"
    keyshape = Keyshape.SQUARE
    category = "objects/organization"
    aliases = ("hierarchy-cube", "organization-chart", "org-chart")
    keywords = (
        "hierarchy", "organization", "structure", "node", "tree",
        "distribute", "cube", "network",
    )

    def build(self) -> None:
        # The cube reaches the square keyshape at y=2. Its six-sided outline
        # and three-way centre join retain the reference's isometric read.
        self.add_polyline(
            "cube-outline",
            (24, 2), (34, 8), (34, 19), (24, 25), (14, 19), (14, 8),
            closed=True,
        )
        self.add_line("cube-y-left", (14, 8), (24, 14))
        self.add_line("cube-y-right", (34, 8), (24, 14))
        self.add_line("cube-y-down", (24, 14), (24, 25))

        # A straight stem and bus distribute to exactly three equal children.
        # Every junction shares an authored endpoint, including the top of
        # each child circle, so the drawing is one connected hierarchy.
        self.add_line("parent-stem", (24, 25), (24, 31))
        self.add_line("bus-left", (5, 31), (24, 31))
        self.add_line("bus-right", (24, 31), (43, 31))
        # The outer children carry three of the four extremes: their circles
        # reach x 2 and x 46 on the sides and y 46 at the foot, so the bus ends
        # sit inside them rather than defining the width.
        for name, x in (("left", 5), ("centre", 24), ("right", 43)):
            self.add_line(f"child-{name}-stem", (x, 31), (x, 40))
            self.add_arc(
                f"child-{name}-circle-right", (x, 40), (x, 46), radius_x=3,
            )
            self.add_arc(
                f"child-{name}-circle-left", (x, 46), (x, 40), radius_x=3,
            )
            self.add_contour(
                f"child-{name}-circle",
                f"child-{name}-circle-right", f"child-{name}-circle-left",
                closed=True,
            )

        # Record each genuine inter-path contact narrowly. The geometry uses
        # exact shared endpoints throughout; these relations preserve that
        # topology in the serialized model instead of relying on inference.
        for first, second in (
            ("cube-outline", "cube-y-left"),
            ("cube-outline", "cube-y-right"),
            ("cube-outline", "cube-y-down"),
            ("cube-outline", "parent-stem"),
            ("cube-y-left", "cube-y-right"),
            ("cube-y-left", "cube-y-down"),
            ("cube-y-right", "cube-y-down"),
            ("cube-y-down", "parent-stem"),
            ("parent-stem", "bus-left"),
            ("parent-stem", "bus-right"),
            ("parent-stem", "child-centre-stem"),
            ("bus-left", "bus-right"),
            ("bus-left", "child-left-stem"),
            ("bus-left", "child-centre-stem"),
            ("bus-right", "child-centre-stem"),
            ("bus-right", "child-right-stem"),
            ("child-left-stem", "child-left-circle"),
            ("child-centre-stem", "child-centre-circle"),
            ("child-right-stem", "child-right-circle"),
        ):
            self.relate("connect", first, second)
