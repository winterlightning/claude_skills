"""A molar with a central orthodontic bracket and a wire across its crown.

Symbol plan: the tooth is a mirrored two-root contour about x=24. The bracket
owns equal left and right walls; the wire is split at each real attachment.
The horizontal wire owns the HRECT_L extremes (4, 44), while the tooth owns
the vertical extremes (8, 40). Lucide's braces reference informed the clear
orthodontic wire and small central bracket, not the tooth silhouette.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "dd72327b-af72-492c-b3df-5ebc0cb31774"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tooth-with-brace-bracket/20260927T155415Z-thuan-mac-1/reference/dental brace_dd72327b-af72-492c-b3df-5ebc0cb31774.svg"
AUTHOR = "gpt-6"


class ToothWithBraceBracket(Solo48):
    icon_id = "tooth-with-brace-bracket"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ("dental brace",)
    keywords = ("tooth", "bracket", "braces", "orthodontics")

    def build(self) -> None:
        # Crown crests and root lobes mirror around the tooth's vertical axis.
        self.add_bezier(
            "crown-right", (24, 9),
            ((27, 8), (29, 8), (32, 8)),
            ((37, 8), (40, 12), (40, 18)),
        )
        self.add_line("wall-right", (40, 18), (40, 22))
        self.add_bezier(
            "roots", (40, 22),
            ((40, 27), (37, 30), (39, 34)),
            ((40, 38), (39, 40), (36, 40)),
            ((32, 40), (30, 38), (30, 37)),
            ((30, 34), (27, 34), (24, 34)),
            ((21, 34), (18, 34), (18, 37)),
            ((18, 38), (16, 40), (12, 40)),
            ((9, 40), (8, 38), (9, 34)),
            ((11, 30), (8, 27), (8, 22)),
        )
        self.add_line("wall-left", (8, 22), (8, 18))
        self.add_bezier(
            "crown-left", (8, 18),
            ((8, 12), (11, 8), (16, 8)),
            ((19, 8), (21, 8), (24, 9)),
        )
        self.add_contour("tooth", "crown-right", "wall-right", "roots", "wall-left", "crown-left", closed=True)

        # Round joins soften the rectangular attachment at native size.
        self.add_polyline("bracket", (17, 18), (31, 18), (31, 22), (31, 26),
                          (17, 26), (17, 22), closed=True)
        self.add_line("wire-left-tip", (4, 22), (8, 22))
        self.add_line("wire-left", (8, 22), (17, 22))
        self.add_line("wire-right", (31, 22), (40, 22))
        self.add_line("wire-right-tip", (40, 22), (44, 22))
        self.relate("connect", "wire-left-tip", "tooth")
        self.relate("connect", "wire-left", "tooth")
        self.relate("connect", "wire-right", "tooth")
        self.relate("connect", "wire-right-tip", "tooth")
        self.relate("connect", "wire-left", "bracket")
        self.relate("connect", "wire-right", "bracket")
        self.relate("connect", "wire-left-tip", "wire-left")
        self.relate("connect", "wire-right", "wire-right-tip")
