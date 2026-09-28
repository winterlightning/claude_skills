"""A-shaped mast with crossbar and signal arcs. Lucide radio-tower informs the mast and paired curves. Reduced two wave pairs to one pair to preserve clearance around the mast.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'eb0a1297-ca44-44fa-a815-5e5ae09e5934'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__antenna-signal/20260926T064521Z-thuan-mac/reference/signal antenna_eb0a1297-ca44-44fa-a815-5e5ae09e5934.svg'
AUTHOR = "claude-opus-5-5"


class AntennaSignal(Solo48):
    icon_id = 'antenna-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('antenna', 'signal', 'broadcast', 'radio', 'tower', 'wireless', 'transmission', 'hotspot')

    def build(self) -> None:
        # Revision per review: symmetric about x 24. The mast apex moves down to (24, 26) with
        # legs to (16, 42) and (32, 42); the crossbar is lower, (19, 36)-(29, 36). Each side now
        # has two signal arcs: a short inner arc (18, 8)-(18, 20) bulging to x 16 (rx 2, ry 6) and
        # a taller outer arc (9, 6)-(9, 34) bulging to x 6 (rx 3, ry 14) that reaches further
        # down. Arcs keep 9+ from each other and from the mast.
        self.add_polyline('mast', (16, 42), (19, 36), (24, 26), (29, 36), (32, 42))
        self.add_line('crossbar', (19, 36), (29, 36))
        self.relate('connect', 'mast', 'crossbar')
        self.add_arc('wave-inner-left', (18, 8), (18, 20), radius_x=2, radius_y=6, sweep=False)
        self.add_arc('wave-inner-right', (30, 8), (30, 20), radius_x=2, radius_y=6)
        self.add_arc('wave-outer-left', (9, 6), (9, 34), radius_x=3, radius_y=14, sweep=False)
        self.add_arc('wave-outer-right', (39, 6), (39, 34), radius_x=3, radius_y=14)
