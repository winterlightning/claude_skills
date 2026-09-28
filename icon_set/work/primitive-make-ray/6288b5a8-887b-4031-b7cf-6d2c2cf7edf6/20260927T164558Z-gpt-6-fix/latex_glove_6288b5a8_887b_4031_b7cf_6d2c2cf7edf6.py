"""Latex glove with an integrated thumb, four fingers, and a cuff.
Symbol plan: one outline owns each finger crest, the thumb, and the cuff; three interior divisions share the finger valleys.
Keyshape HRECT_L reaches (4,8)-(44,40) on its centerlines.
Lucide hand construction informed the rounded fingertips; the thumb follows the source's asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "6288b5a8-887b-4031-b7cf-6d2c2cf7edf6"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__latex-glove/20260927T164305Z-thuan-mac-1/reference/latex_6288b5a8-887b-4031-b7cf-6d2c2cf7edf6.svg"
AUTHOR = "gpt-6"
class LatexGlove(Solo48):
    icon_id = "latex-glove"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ("latex", "glove", "protective")
    def build(self):
        self.add_line("cuff",(18,40),(38,40))
        self.add_bezier("palm-right",(38,40),((40,36),(44,34),(44,29)))
        self.add_line("pinky-outer",(44,29),(44,18))
        self.add_arc("pinky-tip",(44,18),(36,18),radius_x=4,sweep=False)
        self.add_line("pinky-valley",(36,18),(36,14))
        self.add_arc("ring-tip",(36,14),(28,14),radius_x=4,sweep=False)
        self.add_line("ring-valley",(28,14),(28,12))
        self.add_arc("middle-tip",(28,12),(20,12),radius_x=4,sweep=False)
        self.add_line("middle-valley",(20,12),(20,16))
        self.add_arc("index-tip",(20,16),(12,16),radius_x=4,sweep=False)
        self.add_line("index-outer",(12,16),(12,23))
        self.add_line("thumb-upper",(12,23),(4,13))
        self.add_line("thumb-tip",(4,13),(4,30))
        self.add_line("thumb-lower",(4,30),(12,38))
        self.add_bezier("palm-left",(12,38),((14,39),(16,40),(18,40)))
        self.add_contour("glove","cuff","palm-right","pinky-outer","pinky-tip","pinky-valley","ring-tip","ring-valley","middle-tip","middle-valley","index-tip","index-outer","thumb-upper","thumb-tip","thumb-lower","palm-left",closed=True)
        self.add_line("index-seam",(20,16),(20,26))
        self.add_line("middle-seam",(28,14),(28,26))
        self.add_line("ring-seam",(36,18),(36,26))
        for n in ("index-seam","middle-seam","ring-seam"):
            self.relate("connect","glove",n)
