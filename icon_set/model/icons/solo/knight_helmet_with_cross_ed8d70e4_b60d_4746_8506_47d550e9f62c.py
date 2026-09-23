"""A pointed crusader helmet with a brow seam and central faceplate cross.

VRECT_L extrema (8,4)-(40,44). Crown and lower faceplate mirror about x=24;
cross arms share a center node. Lucide hard-hat informed the clear brow seam;
the source supplies the pointed full-face helmet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "ed8d70e4-b60d-4746-8506-47d550e9f62c"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/crusader_ed8d70e4-b60d-4746-8506-47d550e9f62c.svg"
AUTHOR = "gpt-6"


class KnightHelmetWithCross(Solo48):
    icon_id = "knight-helmet-with-cross"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/armor"
    aliases = ("crusader helmet", "cross helmet")
    keywords = ("knight", "faceplate", "crest", "medieval")

    def build(self) -> None:
        self.add_bezier("crown-right",(24,4),((33,7),(40,13),(40,19)))
        self.add_line("side-right",(40,19),(40,36))
        self.add_bezier("chin-right",(40,36),((34,40),(27,44),(24,44)))
        self.add_bezier("chin-left",(24,44),((21,44),(14,40),(8,36)))
        self.add_line("side-left",(8,36),(8,19))
        self.add_bezier("crown-left",(8,19),((8,13),(15,7),(24,4)))
        self.add_contour("helmet","crown-right","side-right","chin-right","chin-left","side-left","crown-left",closed=True)
        self.add_line("brow",(8,19),(40,19))
        self.relate("connect","brow","helmet")
        self.add_line("cross-v-top",(24,28),(24,31))
        self.add_line("cross-v-bottom",(24,31),(24,35))
        self.add_contour("cross-vertical","cross-v-top","cross-v-bottom")
        self.add_line("cross-h-left",(19,31),(24,31))
        self.add_line("cross-h-right",(24,31),(29,31))
        self.add_contour("cross-horizontal","cross-h-left","cross-h-right")
        self.relate("connect","cross-vertical","cross-horizontal")
