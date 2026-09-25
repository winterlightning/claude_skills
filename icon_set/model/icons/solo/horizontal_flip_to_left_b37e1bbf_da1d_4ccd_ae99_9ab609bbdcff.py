from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "b37e1bbf-da1d-4ccd-ae99-9ab609bbdcff"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/flip left_b37e1bbf-da1d-4ccd-ae99-9ab609bbdcff.svg"
AUTHOR = "gpt-6"

class HorizontalFlipToLeft(Solo48):
    icon_id = "horizontal-flip-to-left"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("flip left", "mirror horizontally")
    keywords = ("flip", "reflect", "left", "panels")

    def build(self) -> None:
        # Open facing panels leave space for one leftward curved arrow.
        self.add_polyline("right-panel", (28, 8), (42, 8), (44, 10), (44, 38), (42, 40), (28, 40))
        self.add_polyline("left-panel-top", (18, 8), (4, 8), (4, 14))
        self.add_line("left-panel-dash", (4, 22), (4, 26))
        self.add_polyline("left-panel-bottom", (4, 34), (4, 40), (18, 40))
        self.add_arc("motion", (35, 27), (14, 27), radius_x=13, radius_y=8, sweep=False)
        self.add_polyline("arrowhead", (19, 22), (14, 27), (21, 30))
        self.relate("connect", "motion", "arrowhead")
