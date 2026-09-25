from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "52c32e39-3bac-4a0f-8904-0928470decff"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gesture expand 1_52c32e39-3bac-4a0f-8904-0928470decff.svg"
AUTHOR = "gpt-6"

class HandExpansionTouchGesture(Solo48):
    icon_id = "hand-expansion-touch-gesture"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("expand gesture", "three-way drag")
    keywords = ("hand", "finger", "arrows", "spread")

    def build(self) -> None:
        # A raised index finger sits below up/left/right directional arrowheads.
        self.add_polyline("hand", (16, 40), (16, 32), (22, 32), (22, 24), (30, 24), (30, 40), (16, 40), closed=True)
        self.add_polyline("arrow-up", (20, 12), (24, 8), (28, 12))
        self.add_line("arrow-up-shaft", (24, 8), (24, 16))
        self.relate("connect", "arrow-up", "arrow-up-shaft")
        self.add_polyline("arrow-left", (8, 24), (4, 28), (8, 32))
        self.add_polyline("arrow-right", (40, 24), (44, 28), (40, 32))
