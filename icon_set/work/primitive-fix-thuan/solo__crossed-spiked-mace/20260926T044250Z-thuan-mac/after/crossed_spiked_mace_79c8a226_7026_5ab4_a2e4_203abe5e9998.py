"""Two crossed maces: spiked ball heads at the top left and top right on long handles crossing in an X.

Symbol plan: symmetric about x=24. Each head is one closed six-pointed star outline
(tips at radius about 8, valleys on the 3-4-5 points of radius 5), so its spikes are one
contour. The two heads' side tips are exactly 8 apart. Each handle is a 45-degree line
from its head's bottom tip to the opposite bottom corner; the handles cross at the exact
node (24,33), where both are split and joined.
Lucide construction: 'swords' - crossed handles; star outline for the spiked head.
Keyshape SQUARE: centerline x 6..42 (side tips, handle ends), y 6..42 (top tips, handle ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "79c8a226-7026-5ab4-a2e4-203abe5e9998"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__crossed-spiked-mace/20260926T044250Z-thuan-mac/reference/antique mace double_79c8a226-7026-5ab4-a2e4-203abe5e9998.svg"
AUTHOR = "claude-opus-5-5"

STAR = [(0, -8), (3, -4), (7, -4), (5, 0), (7, 4), (3, 4), (0, 8), (-3, 4), (-7, 4), (-5, 0), (-7, -4), (-3, -4)]


class CrossedSpikedMace(Solo48):
    icon_id = "crossed-spiked-mace"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weapon"
    aliases = ("antique mace double", "crossed maces", "morning star")
    keywords = ("mace", "morning star", "weapon", "medieval", "crossed", "battle", "spiked", "knight")

    def build(self) -> None:
        cross = (24, 33)
        for side, (cx, cy), end in (("l", (13, 14), (33, 42)), ("r", (35, 14), (15, 42))):
            pts = [(cx + dx, cy + dy) for dx, dy in STAR]
            self.add_polyline(f"head-{side}", *pts, closed=True)
            bottom = (cx, cy + 8)
            self.add_line(f"handle-{side}-a", bottom, cross)
            self.add_line(f"handle-{side}-b", cross, end)
            self.add_contour(f"handle-{side}", f"handle-{side}-a", f"handle-{side}-b")
            self.relate("connect", f"head-{side}", f"handle-{side}")
        self.relate("connect", "handle-l", "handle-r")
