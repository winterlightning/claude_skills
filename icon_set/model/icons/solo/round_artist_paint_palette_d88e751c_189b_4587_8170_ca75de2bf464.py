"""A circular palette-like disc with three round openings, one above two.

CIRCLE radius 20 about (24,24). Repeated holes use one radius and mirror the
lower pair about x=24. The source has no thumb notch, so none is invented.
Lucide palette confirms circular paint-well rhythm, though its edge differs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "d88e751c-189b-4587-8170-ca75de2bf464"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/color painting palette 1_d88e751c-189b-4587-8170-ca75de2bf464.svg"
AUTHOR = "gpt-6"


class RoundArtistPaintPalette(Solo48):
    icon_id = "round-artist-paint-palette"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("three-hole disc", "round palette")
    keywords = ("paint", "openings", "artist", "color")

    def build(self) -> None:
        def circle(name: str, x: int, y: int, radius: int) -> None:
            members = []
            points = ((x-radius,y), (x,y-radius), (x+radius,y), (x,y+radius), (x-radius,y))
            for i in range(4):
                part = f"{name}-{i}"
                self.add_arc(part, points[i], points[i+1], radius_x=radius, radius_y=radius, sweep=True)
                members.append(part)
            self.add_contour(name, *members, closed=True)

        circle("disc", 24, 24, 20)
        hole_radius = 3
        for name, x, y in (("hole-top",24,16), ("hole-left",16,28), ("hole-right",32,28)):
            circle(name, x, y, hole_radius)
