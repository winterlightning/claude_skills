"""An open-hulled sailboat over three small water swells.

Symbol plan: one symmetric sail, a separate open hull, and a repeated water arc.
The reference's hull ends and water are essential to the silhouette. Lucide's
sailboat informed the simple sail construction; the source controls the layout.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6920feca-ba55-4c5c-8e6c-032c49ca2982"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__sailboat-triangle-sail/20260927T091420Z-thuan-mac-1/reference/sailing boat_6920feca-ba55-4c5c-8e6c-032c49ca2982.svg"
AUTHOR = "gpt-6"


class SailboatTriangleSail(Solo48):
    icon_id = "sailboat-triangle-sail"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "outdoors"
    aliases = ()
    keywords = ("sailboat", "sail", "boat", "water")

    def build(self) -> None:
        axis = 24
        sail_half_width = 10
        self.add_polyline("sail", (axis-sail_half_width,18), (axis,6),
                          (axis+sail_half_width,18), closed=True)
        self.add_line("deck", (6,26), (42,26))
        self.add_line("hull-left", (6,26), (10,32))
        self.add_line("hull-right", (42,26), (38,32))
        self.relate("connect", "deck", "hull-left")
        self.relate("connect", "deck", "hull-right")
        for index in range(3):
            x = 6 + index*12
            self.add_arc(f"water-{index+1}", (x,42), (x+12,42),
                         radius_x=6, radius_y=2, sweep=True)
