"""A steaming round cauldron on two feet; bounds (2,2)-(46,46).

Construction reference: Lucide cooking-pot: strong horizontal rim; source rounded belly, feet and two steam wisps.
Centerline extremes are the declared keyshape's exact bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0575da1b-6796-47d7-acc0-06fde95480bb'
SOURCE_PATH = 'pictographic-primitives/culture/batch-07/witch cauldron_0575da1b-6796-47d7-acc0-06fde95480bb.svg'


class WitchesCauldron(Solo48):
    icon_id = 'witches-cauldron'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('cauldron', 'witch', 'pot', 'potion', 'brew', 'magic', 'halloween', 'spell')

    def build(self) -> None:
        self.add_polyline("rim", (2, 20), (7, 20), (41, 20), (46, 20))
        self.add_arc("bowl-right", (41, 20), (36, 40), radius_x=18, radius_y=16)
        self.add_arc("bowl-base", (36, 40), (12, 40), radius_x=22, radius_y=7)
        self.add_arc("bowl-left", (12, 40), (7, 20), radius_x=18, radius_y=16)
        self.add_contour("bowl", "bowl-right", "bowl-base", "bowl-left")
        self.relate("connect", "rim", "bowl")
        self.add_line("foot-left", (12, 40), (7, 46))
        self.add_line("foot-right", (36, 40), (41, 46))
        self.relate("connect", "bowl", "foot-left")
        self.relate("connect", "bowl", "foot-right")
        for side,x in (("left",17),("right",31)):
            self.add_arc(side+"-steam-top", (x, 2), (x-3, 5), radius_x=3)
            self.add_arc(side+"-steam-bottom", (x-3, 5), (x-6, 8), radius_x=3, sweep=False)
            self.add_line(side+"-steam-stem", (x-6, 8), (x-6, 12))
            self.add_contour(side+"-steam", side+"-steam-top", side+"-steam-bottom", side+"-steam-stem")
