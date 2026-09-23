"""A circular world globe with open central space and polar meridians."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "8dd50802-1f26-431a-9950-bf33ee3acd87"
SOURCE_PATH = "pictographic-primitives/container/globe_8dd50802-1f26-431a-9950-bf33ee3acd87.svg"
AUTHOR = "gpt-6"


class WorldGlobeSphere(Solo48):
    icon_id = "world-globe-sphere-solo"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/geography"
    aliases = ("globe", "world sphere")
    keywords = ("earth", "latitude", "longitude", "network")

    def build(self) -> None:
        # Exact radius-20 circle; the four quarters share one center.
        poles = ((24, 4), (40, 12), (44, 24), (40, 36),
                 (24, 44), (8, 36), (4, 24), (8, 12))
        outline = []
        for index, start in enumerate(poles):
            name = f"sphere-{index}"
            self.add_arc(name, start, poles[(index + 1) % len(poles)], radius_x=20)
            outline.append(name)
        self.add_contour("sphere", *outline, closed=True)

        # The band ends attach at exact points on the circle, then ease into
        # straight central runs. Both axes and all curve controls mirror.
        for band, edge_y, middle_y, left_sphere, right_sphere in (
            ("north", 12, 15, "sphere-7", "sphere-1"),
            ("south", 36, 33, "sphere-5", "sphere-3"),
        ):
            direction = 1 if band == "north" else -1
            left = f"{band}-left"
            middle = f"{band}-latitude"
            right = f"{band}-right"
            self.add_bezier(left, (8, edge_y),
                            ((8, edge_y + 2*direction), (9, middle_y), (11, middle_y)))
            self.add_line(middle, (11, middle_y), (37, middle_y))
            self.add_bezier(right, (37, middle_y),
                            ((39, middle_y), (40, edge_y + 2*direction), (40, edge_y)))
            self.add_contour(f"{band}-band", left, middle, right)
            self.relate("connect", left, left_sphere)
            self.relate("connect", right, right_sphere)
        for side, sign in (("west", -1), ("east", 1)):
            x = 24 + sign * 7
            self.add_bezier(f"{side}-north-meridian", (24, 4),
                            ((24 + sign * 4, 6), (x, 11), (x, 15)))
            self.add_bezier(f"{side}-south-meridian", (x, 33),
                            ((x, 37), (24 + sign * 4, 42), (24, 44)))
            self.relate("connect", f"{side}-north-meridian", "north-latitude")
            self.relate("connect", f"{side}-south-meridian", "south-latitude")
            self.relate("connect", f"{side}-north-meridian", "sphere-0")
            self.relate("connect", f"{side}-south-meridian", "sphere-3")
