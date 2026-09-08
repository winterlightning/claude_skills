"""A two-tier stone bridge with paired round arches and water below. Lucide bridge informs deck/support hierarchy; the source tiers are retained with two broad arches per tier."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/bridge_8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192.svg'
AUTHOR = 'gpt-6'


class ArchedStoneBridge(Solo48):
    icon_id = 'arched-stone-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('bridge', 'arch', 'viaduct', 'river', 'water', 'crossing', 'stone', 'landmark', 'infrastructure')

    def build(self) -> None:
        # Centerline extremes (2,2)-(46,46).
        self.add_line("deck-top", (2,2), (46,2))
        self.add_line("deck-middle", (2,24), (46,24))
        for level, cy, ry, bottom in (("upper",16,6,17),("lower",36,5,37)):
            self.add_line(level+"-pier-left", (2,bottom), (2,cy))
            self.add_arc(level+"-arch-left", (2,cy), (24,cy), radius_x=11, radius_y=ry)
            self.add_arc(level+"-arch-right", (24,cy), (46,cy), radius_x=11, radius_y=ry)
            self.add_line(level+"-pier-right", (46,cy), (46,bottom))
            self.add_contour(level, level+"-pier-left", level+"-arch-left", level+"-arch-right", level+"-pier-right")
            self.add_line(level+"-pier-middle", (24,cy), (24,bottom))
            self.relate("connect", level, level+"-pier-middle")
        self.add_arc("water-left", (2,44), (24,44), radius_x=11, radius_y=2, sweep=False)
        self.add_arc("water-right", (24,44), (46,44), radius_x=11, radius_y=2, sweep=False)
        self.add_contour("water", "water-left", "water-right")
