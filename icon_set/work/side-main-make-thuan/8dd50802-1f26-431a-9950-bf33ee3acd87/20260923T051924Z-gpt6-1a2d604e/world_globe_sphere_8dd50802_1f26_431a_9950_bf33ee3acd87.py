"""A world globe with open central space and polar meridians."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8dd50802-1f26-431a-9950-bf33ee3acd87"
SOURCE_PATH = "pictographic-primitives/container/globe_8dd50802-1f26-431a-9950-bf33ee3acd87.svg"
AUTHOR = "gpt-6"


class WorldGlobeSphere(Solo48):
    icon_id = "world-globe-sphere"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/geography"
    aliases = ("globe", "world sphere")
    keywords = ("earth", "latitude", "longitude", "network")

    def build(self) -> None:
        # Root symbol: an almost circular sphere about (24, 24). The bands
        # sit farther from the poles than in the large source to keep the
        # polar openings visible under SOLO48's 4-unit stroke.
        # Each quarter is built from two tangent cubics; all control points
        # mirror about both axes. The middle stays open as in the reference.
        center = 24
        band_offset = 9
        band_inner = 7
        sections = [
            ((24, 4), (32, 4), (38, 9), (41, 15)),
            ((41, 15), (43, 19), (44, 22), (44, 24)),
            ((44, 24), (44, 26), (43, 29), (41, 33)),
            ((41, 33), (38, 39), (32, 44), (24, 44)),
            ((24, 44), (16, 44), (10, 39), (7, 33)),
            ((7, 33), (5, 29), (4, 26), (4, 24)),
            ((4, 24), (4, 22), (5, 19), (7, 15)),
            ((7, 15), (10, 9), (16, 4), (24, 4)),
        ]
        outline = []
        for i, (start, control1, control2, end) in enumerate(sections):
            name = f"sphere-{i}"
            self.add_bezier(name, start, (control1, control2, end))
            outline.append(name)
        self.add_contour("sphere", *outline, closed=True)

        for y, name in ((center-band_offset, "north"), (center+band_offset, "south")):
            self.add_line(f"{name}-latitude", (band_inner, y), (2*center-band_inner, y))

        for side, sign in (("west", -1), ("east", 1)):
            x = center + sign*7
            self.add_bezier(f"{side}-north-meridian", (center, 4),
                            ((center+sign*4, 6), (x, 11), (x, 15)))
            self.add_bezier(f"{side}-south-meridian", (x, 33),
                            ((x, 37), (center+sign*4, 42), (center, 44)))

        # Every contact is represented by an identical endpoint.
        for band, left, right in (("north", 7, 1), ("south", 5, 3)):
            latitude = f"{band}-latitude"
            self.relate("connect", latitude, f"sphere-{left}")
            self.relate("connect", latitude, f"sphere-{right}")
        for side in ("west", "east"):
            for band in ("north", "south"):
                self.relate("connect", f"{side}-{band}-meridian", f"{band}-latitude")
                self.relate("connect", f"{side}-{band}-meridian", "sphere-0" if band == "north" else "sphere-3")
