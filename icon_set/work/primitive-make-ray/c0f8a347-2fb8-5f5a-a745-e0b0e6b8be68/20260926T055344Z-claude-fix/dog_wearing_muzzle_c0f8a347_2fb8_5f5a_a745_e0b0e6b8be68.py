"""A dog's head in profile, facing left, wearing a basket muzzle over its snout.

Symbol plan: the muzzle is a closed basket over the snout, x 6..24, y 26..42, with r4
rounded front corners, split by one vertical bar (x 15) and one horizontal bar (y 34)
into four cells 9 wide and 8 tall. The head is one contour that leaves the basket's top at
the bar (15, 26): the forehead climbs to the front ear, two pointed ears stand on the
skull (tips (19, 6) and (31, 6)), the back of the skull reaches (36, 18), and the cheek
runs diagonally back down into the basket's back side at the bar (24, 34), closing the
head. The neck runs from the back of the skull down to (42, 36). A first version with an
open head (attempts/v1-open-head.svg) read as an 'M' over a grid; a higher basket
(attempts/v2-high-muzzle.svg) left the head too thin. The reference's throat line is
dropped: the basket now sits on the canvas bottom. Shared end points are declared.
Lucide construction: no Lucide muzzle; a rounded rectangle with grid bars as in Lucide's
'grid' icons, pointed ears as in Lucide's 'cat'/'dog' heads.
Keyshape SQUARE: centerline x 6..42 (basket front, neck end), y 6..42 (ear tips, basket bottom).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c0f8a347-2fb8-5f5a-a745-e0b0e6b8be68"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dog-wearing-muzzle/20260926T055140Z-thuan-mac/reference/dog mouth protection_c0f8a347-2fb8-5f5a-a745-e0b0e6b8be68.svg"
AUTHOR = "claude-opus-5-5"


class DogWearingMuzzle(Solo48):
    icon_id = "dog-wearing-muzzle"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/dog"
    aliases = ("dog mouth protection", "dog muzzle", "basket muzzle")
    keywords = ("dog", "muzzle", "safety", "pet", "bite", "protection", "training", "vet", "restraint")

    def build(self) -> None:
        l, r, t, b, bar_x, bar_y = 6, 24, 26, 42, 15, 34
        self.add_line("basket-top-front", (l + 4, t), (bar_x, t))
        self.add_line("basket-top-back", (bar_x, t), (r, t))
        self.add_line("basket-back-upper", (r, t), (r, bar_y))
        self.add_line("basket-back-lower", (r, bar_y), (r, b))
        self.add_line("basket-bottom-back", (r, b), (bar_x, b))
        self.add_line("basket-bottom-front", (bar_x, b), (l + 4, b))
        self.add_arc("basket-corner-low", (l + 4, b), (l, b - 4), radius_x=4)
        self.add_line("basket-front-lower", (l, b - 4), (l, bar_y))
        self.add_line("basket-front-upper", (l, bar_y), (l, t + 4))
        self.add_arc("basket-corner-high", (l, t + 4), (l + 4, t), radius_x=4)
        self.add_contour("basket", "basket-top-front", "basket-top-back", "basket-back-upper",
                         "basket-back-lower", "basket-bottom-back", "basket-bottom-front",
                         "basket-corner-low", "basket-front-lower", "basket-front-upper",
                         "basket-corner-high", closed=True)
        self.add_line("bar-vertical", (bar_x, t), (bar_x, b))
        self.add_line("bar-horizontal", (l, bar_y), (r, bar_y))
        self.relate("connect", "basket", "bar-vertical")
        self.relate("connect", "basket", "bar-horizontal")
        self.relate("connect", "bar-vertical", "bar-horizontal")
        self.add_polyline("head", (bar_x, t), (18, 14), (19, 6), (24, 11), (31, 6), (36, 18), (r, bar_y))
        self.relate("connect", "basket", "head")
        self.relate("connect", "bar-vertical", "head")
        self.relate("connect", "bar-horizontal", "head")
        self.add_line("neck", (36, 18), (42, 36))
        self.relate("connect", "head", "neck")
