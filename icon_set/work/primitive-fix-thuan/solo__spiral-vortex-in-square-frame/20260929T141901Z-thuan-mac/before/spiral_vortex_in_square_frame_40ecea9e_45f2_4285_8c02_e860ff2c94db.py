from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "40ecea9e-45f2-4285-8c02-e860ff2c94db"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/houdini logo_40ecea9e-45f2-4285-8c02-e860ff2c94db.svg"
AUTHOR = "gpt-6"

class SpiralVortexInSquareFrame(Solo48):
    icon_id = "spiral-vortex-in-square-frame"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Houdini spiral", "vortex frame")
    keywords = ("spiral", "square", "curl")

    def build(self) -> None:
        # Broken square frame feeds a circular outer turn and tight central curl.
        self.add_polyline("frame-main", (6, 20), (6, 6), (42, 6), (42, 42), (30, 42))
        self.add_polyline("frame-corner", (6, 32), (6, 42), (14, 42))
        self.add_line("entry", (6, 20), (14, 24))
        self.add_arc("turn-1", (14, 24), (24, 14), radius_x=10, sweep=True)
        self.add_arc("turn-2", (24, 14), (34, 24), radius_x=10, sweep=True)
        self.add_arc("turn-3", (34, 24), (24, 34), radius_x=10, sweep=True)
        self.add_arc("turn-4", (24, 34), (14, 24), radius_x=10, sweep=True)
        self.add_line("inward", (14, 24), (22, 24))
        self.add_arc("curl", (22, 24), (26, 24), radius_x=2, sweep=True)
        self.add_contour("vortex", "entry", "turn-1", "turn-2", "turn-3", "turn-4", "inward", "curl")
        self.relate("connect", "frame-main", "vortex")
