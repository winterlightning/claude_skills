"""A rounded land plot with a low rolling terrain line.

Symbol plan: one rounded square border, split at the two points where the
terrain curve meets it. The SQUARE centerline bounds are x/y 6..42.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "483287c6-632d-4cf2-b138-65092aeced18"
SOURCE_PATH = "pictographic-primitives/_uncategorized_24/land_483287c6-632d-4cf2-b138-65092aeced18.svg"
AUTHOR = "gpt-6"


class RollingTerrainLandPlot(Solo48):
    icon_id = "rolling-terrain-land-plot"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/landscape"
    aliases = ("land parcel", "rolling terrain")
    keywords = ("land", "terrain", "plot", "hills", "field")

    def build(self) -> None:
        self.add_line("top", (12, 6), (36, 6))
        self.add_arc("top-right", (36, 6), (42, 12), radius_x=6)
        self.add_line("right-upper", (42, 12), (42, 30))
        self.add_line("right-lower", (42, 30), (42, 36))
        self.add_arc("bottom-right", (42, 36), (36, 42), radius_x=6)
        self.add_line("bottom", (36, 42), (12, 42))
        self.add_arc("bottom-left", (12, 42), (6, 36), radius_x=6)
        self.add_line("left-lower", (6, 36), (6, 34))
        self.add_line("left-upper", (6, 34), (6, 12))
        self.add_arc("top-left", (6, 12), (12, 6), radius_x=6)
        self.add_contour("plot-border", "top", "top-right", "right-upper", "right-lower", "bottom-right", "bottom", "bottom-left", "left-lower", "left-upper", "top-left", closed=True)
        self.add_bezier("terrain", (6, 34), ((14, 36), (19, 34), (26, 31)), ((32, 28), (37, 28), (42, 30)))
        self.relate("connect", "terrain", "plot-border")
