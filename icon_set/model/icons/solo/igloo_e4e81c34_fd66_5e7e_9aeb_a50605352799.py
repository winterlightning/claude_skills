"""A snow shelter with rounded shoulders, flat crown, central arched entrance and one block-course mark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4e81c34-fd66-5e7e-9aeb-a50605352799'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/igloo_e4e81c34-fd66-5e7e-9aeb-a50605352799.svg'
AUTHOR = 'gpt-6'


class Igloo(Solo48):
    icon_id = 'igloo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('igloo', 'snow', 'arctic', 'shelter', 'dome', 'winter', 'eskimo', 'ice')

    def build(self) -> None:
        # Centerline extremes (2,8)-(46,40).
        self.add_line("wall-left", (2,40), (2,26))
        self.add_arc("shoulder-left", (2,26), (20,8), radius_x=18)
        self.add_line("crown", (20,8), (28,8))
        self.add_arc("shoulder-right", (28,8), (46,26), radius_x=18)
        self.add_polyline("right-foot", (46,26), (46,40), (31,40), (31,31))
        self.add_arc("entrance", (31,31), (17,31), radius_x=7, sweep=False)
        self.add_polyline("left-foot", (17,31), (17,40), (2,40))
        self.add_line("block-course", (2,26), (10,26))
        self.relate("connect", "wall-left", "shoulder-left")
        self.relate("connect", "shoulder-left", "crown")
        self.relate("connect", "crown", "shoulder-right")
        self.relate("connect", "shoulder-right", "right-foot")
        self.relate("connect", "right-foot", "entrance")
        self.relate("connect", "entrance", "left-foot")
        self.relate("connect", "left-foot", "wall-left")
        self.relate("connect", "block-course", "wall-left")
        self.relate("connect", "block-course", "shoulder-left")
