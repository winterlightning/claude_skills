"""A clapping hand: an open hand with fingers up, a shorter thumb at the right, and a motion arc at the top left.

Symbol plan: the hand is one closed outline built from a column series (step 8): three
fingers and the thumb, each with a semicircular (r4) tip at its own height (middle
finger tallest, thumb lowest), then a straight left wall, a rounded U palm (one cubic
whose lowest point lands exactly on y=42) and the straight right wall. Finger
separators hang from the tip junctions into the palm, 8 apart like the columns.
A small quarter arc in the top-left corner is the clapping motion mark.
The reference's fourth finger and its tilt are dropped: four fingers plus a thumb need
40 units of 8-wide columns, and a tilted column series cannot keep integer joins.
Lucide construction: 'hand' - finger columns with round tips and a U palm.
Keyshape SQUARE: centerline x 6..42 (motion arc, thumb), y 6..42 (motion arc, palm).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cdbf5cfc-c77a-43ac-925c-d8a3a7e49753"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__clapping-hand/20260926T034135Z-thuan-mac/reference/clap_cdbf5cfc-c77a-43ac-925c-d8a3a7e49753.svg"
AUTHOR = "claude-opus-5-5"


class ClappingHand(Solo48):
    icon_id = "clapping-hand"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gesture"
    aliases = ("clap", "applause", "waving hand")
    keywords = ("clap", "applause", "hand", "wave", "high five", "cheer", "gesture", "palm")

    def build(self) -> None:
        left, step, tip_r = 10, 8, 4
        tips = (20, 12, 14, 24)  # tip centre y for finger 1..3 and the thumb
        palm_top, palm_bot, sep_end = 32, 42, 30
        xs = [left + step * i for i in range(len(tips) + 1)]  # 10, 18, 26, 34, 42
        members = []
        # left wall up to the first tip
        self.add_line("wall-l", (left, palm_top), (left, tips[0]))
        members.append("wall-l")
        for i, cy in enumerate(tips):
            x0, x1 = xs[i], xs[i + 1]
            self.add_arc(f"tip{i}", (x0, cy), (x1, cy), radius_x=tip_r)
            members.append(f"tip{i}")
            if i + 1 < len(tips):
                nxt = tips[i + 1]
                if nxt != cy:
                    self.add_line(f"side{i}", (x1, cy), (x1, nxt))
                    members.append(f"side{i}")
                # separator from the lower tip junction into the palm
                self.add_line(f"sep{i}", (x1, max(cy, nxt)), (x1, sep_end))
        right = xs[-1]
        self.add_line("wall-r", (right, tips[-1]), (right, palm_top))
        members.append("wall-r")
        k = (palm_bot - palm_top) / 0.75
        self.add_bezier("palm", (right, palm_top), ((right, palm_top + k), (left, palm_top + k), (left, palm_top)))
        members.append("palm")
        self.add_contour("hand", *members, closed=True)
        for i in range(len(tips) - 1):
            self.relate("connect", "hand", f"sep{i}")
        # motion mark
        self.add_arc("motion", (6, 10), (10, 6), radius_x=4)
