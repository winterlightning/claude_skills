"""Two swords crossed in an X, points up, each with a crossguard above its grip.

Symbol plan: mirrored about x=24. Each sword is one straight stroke on a diagonal from
its point at a top corner to its pommel at the opposite bottom corner, the two crossing
square at the centre. A crossguard crosses each sword at right angles 8 (diagonal) from
the pommel, as in the reference where the guards sit near the grips.
Lucide construction: 'swords' - straight diagonal blades with short square guards.
Keyshape SQUARE: centerline x 6..42, y 6..42 (points and pommels).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "267b73de-82b1-4ce3-8f55-d126ce956c5c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__crossed-swords/20260926T035939Z-thuan-mac/reference/swords_267b73de-82b1-4ce3-8f55-d126ce956c5c.svg"
AUTHOR = "claude-opus-5-5"


class CrossedSwords(Solo48):
    icon_id = "crossed-swords"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weapons"
    aliases = ("swords", "crossed-blades", "battle")
    keywords = ("swords", "crossed", "battle", "fight", "combat", "war", "fencing", "duel", "game", "attack")

    def build(self) -> None:
        self.add_line("sword-left", (6, 6), (42, 42))
        self.add_line("sword-right", (42, 6), (6, 42))
        self.add_line("guard-left", (30, 38), (38, 30))
        self.add_line("guard-right", (18, 38), (10, 30))
        self.relate("connect", "sword-left", "sword-right")
        self.relate("connect", "sword-left", "guard-left")
        self.relate("connect", "sword-right", "guard-right")
