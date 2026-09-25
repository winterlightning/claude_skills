"""Clock. Retains the seven-o’clock hands and four cardinal ticks; joins the ticks to the rim to keep the dial clear.

CIRCLE visible extremes (2, 2, 46, 46); centerlines (4, 4, 44, 44).
Lucide clock: circular face and a single joined hand contour; source determines seven o’clock.
Four true quarter-circle arcs share the dial center (24,24) and radius 20.
The asymmetry of the hands preserves seven o’clock.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b96f8e9f-bba3-4327-81b8-dca4c7232949'
SOURCE_PATH = 'pictographic-primitives/symbol/clock 1_b96f8e9f-bba3-4327-81b8-dca4c7232949.svg'
AUTHOR = 'gpt-6'


class ClockSeven(Solo48):
    icon_id = 'clock-seven'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('clock', 'time', 'hour', 'watch', 'schedule', 'minutes', 'wall-clock')

    def build(self) -> None:
        self.add_arc('face-ne', (24, 4), (44, 24), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('face-se', (44, 24), (24, 44), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('face-sw', (24, 44), (4, 24), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('face-nw', (4, 24), (24, 4), radius_x=20, radius_y=20, sweep=True)
        self.add_contour('face', 'face-ne', 'face-se', 'face-sw', 'face-nw', closed=True)
        self.add_polyline('hands', (24, 16), (24, 24), (18, 30))
        self.add_line('tick-top', (24, 4), (24, 7))
        self.relate("connect", 'face', 'tick-top')
        self.add_line('tick-right', (44, 24), (41, 24))
        self.relate("connect", 'face', 'tick-right')
        self.add_line('tick-bottom', (24, 44), (24, 41))
        self.relate("connect", 'face', 'tick-bottom')
        self.add_line('tick-left', (4, 24), (7, 24))
        self.relate("connect", 'face', 'tick-left')
