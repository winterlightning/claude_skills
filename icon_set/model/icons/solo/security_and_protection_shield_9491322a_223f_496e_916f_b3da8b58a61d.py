"""A plain symmetric shield with a peaked crown and pointed base.

VRECT_L extrema (8,4)-(40,44). Both halves mirror around x=24; the straight
sides flow into broad lower curves. Lucide shield informed the continuous
protective silhouette, while the source supplies both pointed extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "9491322a-223f-496e-916f-b3da8b58a61d"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/crest_9491322a-223f-496e-916f-b3da8b58a61d.svg"
AUTHOR = "gpt-6"


class SecurityAndProtectionShield(Solo48):
    icon_id = "security-and-protection-shield"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("crest", "shield outline")
    keywords = ("safe", "guard", "defense", "badge")

    def build(self) -> None:
        self.add_bezier("crown-right",(24,4),((29,8),(35,11),(40,10)))
        self.add_line("right",(40,10),(40,24))
        self.add_bezier("base-right",(40,24),((40,34),(32,40),(24,44)))
        self.add_bezier("base-left",(24,44),((16,40),(8,34),(8,24)))
        self.add_line("left",(8,24),(8,10))
        self.add_bezier("crown-left",(8,10),((13,11),(19,8),(24,4)))
        self.add_contour("shield","crown-right","right","base-right","base-left","left","crown-left",closed=True)
