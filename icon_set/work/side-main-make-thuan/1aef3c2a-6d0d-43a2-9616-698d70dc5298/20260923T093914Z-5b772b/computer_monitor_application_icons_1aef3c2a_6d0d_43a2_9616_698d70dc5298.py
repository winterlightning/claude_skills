from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1aef3c2a-6d0d-43a2-9616-698d70dc5298"
SOURCE_PATH = "pictographic-primitives/other/monitor small squares_1aef3c2a-6d0d-43a2-9616-698d70dc5298.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "computer-monitor-application-icons"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "other"
    aliases = ()
    keywords = ("monitor", "computer", "application")

    def build(self):
        # Plan: rounded screen with two equal stacked square tiles and centered stand.
        # SQUARE centerline extremes (6,6)-(42,42).
        # Draft retains both tiles; their spacing needs validation and is expected to fail.
        self.add_line("screen-top", (10,6), (38,6))
        self.add_arc("screen-tr", (38,6), (42,10), radius_x=4)
        self.add_line("screen-right", (42,10), (42,30))
        self.add_arc("screen-br", (42,30), (38,34), radius_x=4)
        self.add_line("screen-bottom-right", (38,34), (24,34))
        self.add_line("screen-bottom-left", (24,34), (10,34))
        self.add_arc("screen-bl", (10,34), (6,30), radius_x=4)
        self.add_line("screen-left", (6,30), (6,10))
        self.add_arc("screen-tl", (6,10), (10,6), radius_x=4)
        self.add_contour("screen", "screen-top", "screen-tr", "screen-right",
                         "screen-br", "screen-bottom-right", "screen-bottom-left",
                         "screen-bl", "screen-left", "screen-tl", closed=True)
        self.add_line("stand", (24,34), (24,42))
        self.add_polyline("foot", (16,42), (24,42), (32,42))
        self.relate("connect", "screen", "stand")
        self.relate("connect", "stand", "foot")
        for i,y in enumerate((12,24)):
            self.add_polyline(f"app-{i}", (14,y), (22,y), (22,y+8), (14,y+8), closed=True)
