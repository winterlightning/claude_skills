"""Cherry ice-cream sundae: a stemmed bowl with two scoops, a cherry on top and a spoon.

Revision of the disapproved drawing, where scoops, cherry and spoon crowded into a
blob. Plan (VRECT_L, centerline (8,4)-(40,44)): rim (8,20)-(40,20) with a half-circle
bowl r16 below (bottom 36, 8 above the foot), stem to the foot line at y=44; two r8 scoops on the rim; a r3 cherry
sitting on the right scoop's apex with a short stem to (36,4); the spoon is a line from
(8,4) down to the left scoop's apex. Lucide `ice-cream-bowl` informs the bowl and
scoops; the spoon and cherry give deliberate asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "0cd29f28-935b-4556-948b-8d74f8ec867e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cherry-ice-cream-sundae/20260927T150749Z-thuan-mac-1/reference/ice cream bowl_0cd29f28-935b-4556-948b-8d74f8ec867e.svg"
AUTHOR = "claude-fable-5-1"


class CherryIceCreamSundae(Solo48):
    icon_id = "cherry-ice-cream-sundae"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("ice cream bowl", "sundae")
    keywords = ("cherry", "ice cream", "sundae", "dessert", "bowl", "scoop", "spoon")

    def build(self) -> None:
        # bowl
        self.add_line("rim-l", (8, 20), (24, 20))
        self.add_line("rim-r", (24, 20), (40, 20))
        self.add_arc("bowl-r", (40, 20), (24, 36), radius_x=16)
        self.add_arc("bowl-l", (24, 36), (8, 20), radius_x=16)
        self.add_contour("bowl", "rim-l", "rim-r", "bowl-r", "bowl-l", closed=True)
        self.add_line("stem", (24, 36), (24, 44))
        self.add_polyline("foot", (16, 44), (24, 44), (32, 44))
        self.relate("connect", "stem", "bowl")
        self.relate("connect", "stem", "foot")
        # scoops
        self.add_arc("scoop-l-1", (8, 20), (16, 12), radius_x=8)
        self.add_arc("scoop-l-2", (16, 12), (24, 20), radius_x=8)
        self.add_contour("scoop-l", "scoop-l-1", "scoop-l-2")
        self.add_arc("scoop-r-1", (24, 20), (32, 12), radius_x=8)
        self.add_arc("scoop-r-2", (32, 12), (40, 20), radius_x=8)
        self.add_contour("scoop-r", "scoop-r-1", "scoop-r-2")
        self.relate("connect", "scoop-l", "bowl")
        self.relate("connect", "scoop-r", "bowl")
        self.relate("connect", "scoop-l", "scoop-r")
        # cherry on the right scoop
        self.add_arc("cherry-1", (32, 12), (32, 6), radius_x=3)
        self.add_arc("cherry-2", (32, 6), (32, 12), radius_x=3)
        self.add_contour("cherry", "cherry-1", "cherry-2", closed=True)
        self.relate("connect", "cherry", "scoop-r")
        self.add_line("cherry-stem", (32, 6), (34, 4))
        self.relate("connect", "cherry-stem", "cherry")
        # spoon into the left scoop
        self.add_line("spoon", (8, 4), (16, 12))
        self.relate("connect", "spoon", "scoop-l")
