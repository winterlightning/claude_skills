"""Two mountain peaks, one pine, and a descending dashed trail form a compact landscape. SQUARE extremes (6,6)-(42,42); intentional scene asymmetry.
Reduction: Removed one repeated pine, reduced the remaining pine to one triangular tier, and shortened the trail to two broad dashes.
Lucide construction: mountain, tree-pine, route
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eadab1c1-488b-4bcd-b945-526f25489491'
SOURCE_PATH = 'pictographic-primitives/nature/outdoors landscape_eadab1c1-488b-4bcd-b945-526f25489491.svg'
AUTHOR = 'gpt-6'


class MountainForestTrail(Solo48):
    icon_id = 'mountain-forest-trail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-02"
    aliases = ()
    keywords = ('landscape', 'mountains', 'trail', 'pine', 'forest', 'hiking', 'outdoors', 'path')

    def build(self) -> None:
        self.add_polyline("peaks",(6,22),(12,6),(18,16),(24,6),(30,22),closed=True)
        self.add_polyline("pine",(6,40),(12,30),(18,40),(12,40),closed=True)
        self.add_line("trunk",(12,40),(12,42))
        self.relate("connect","trunk","pine-3")
        self.relate("connect","trunk","pine-4")
        self.add_line("trail-upper",(42,14),(42,22))
        self.add_line("trail-lower",(34,30),(42,38))
