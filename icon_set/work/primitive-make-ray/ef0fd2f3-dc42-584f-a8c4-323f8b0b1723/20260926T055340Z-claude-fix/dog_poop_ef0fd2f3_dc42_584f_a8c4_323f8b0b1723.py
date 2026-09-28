"""A pile of dog poop: a three-tier swirl with a pointed tip and a wisp of smell rising beside it.

Symbol plan: the pile is one closed outline, nearly symmetric about x = 24 with its tip
leaning right. The bottom tier is two r5 semicircles (centres (11, 37) and (37, 37))
joined by the flat base y 42; the middle tier is two r5 arcs (centres (14, 28) and
(34, 28)) that meet the bottom tier at concave notches (11, 32) and (37, 32); the top tier
is an onion dome of two cubics rising from notches (14, 23) and (34, 23) to the pointed tip
(25, 6), both vertical at the notches. The smell is one S-shaped cubic from (40, 6) to
(40, 14), 9+ from the dome.
Lucide construction: no Lucide poop; stacked-arc tiers follow Lucide's 'cloud' lobes.
Keyshape SQUARE: centerline x 6..42 (bottom tier), y 6..42 (tip and wisp, base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ef0fd2f3-dc42-584f-a8c4-323f8b0b1723"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dog-poop/20260926T055140Z-thuan-mac/reference/dog poop_ef0fd2f3-dc42-584f-a8c4-323f8b0b1723.svg"
AUTHOR = "claude-opus-5-5"


class DogPoop(Solo48):
    icon_id = "dog-poop"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/pet"
    aliases = ("dog poop", "poo", "pet waste")
    keywords = ("poop", "poo", "dog", "waste", "mess", "pet", "clean", "scoop", "smell")

    def build(self) -> None:
        self.add_arc("tier-bottom-left", (11, 42), (11, 32), radius_x=5)
        self.add_arc("tier-middle-left", (11, 32), (14, 23), radius_x=5)
        self.add_bezier("dome-left", (14, 23), ((14, 15), (22, 15), (25, 6)))
        self.add_bezier("dome-right", (25, 6), ((26, 15), (34, 15), (34, 23)))
        self.add_arc("tier-middle-right", (34, 23), (37, 32), radius_x=5)
        self.add_arc("tier-bottom-right", (37, 32), (37, 42), radius_x=5)
        self.add_line("base", (37, 42), (11, 42))
        self.add_contour("pile", "tier-bottom-left", "tier-middle-left", "dome-left", "dome-right",
                         "tier-middle-right", "tier-bottom-right", "base", closed=True)
        self.add_bezier("smell", (40, 6), ((37, 8), (43, 12), (40, 14)))
