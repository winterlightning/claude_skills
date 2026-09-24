"""Seated badger facing right: low back, small ear, long muzzle and curved chest.
HRECT_L preserves the low silhouette. One coherent outer run owns the body;
the hind-leg crease joins the rear-foot baseline. Omit the tiny eye to retain clearance.
The supplied reference establishes posture; no local Lucide badger match exists.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "5bb2d73b-f3a4-43fd-add6-fac9786654ae"
SOURCE_PATH = "pictographic-primitives/_uncategorized_05/badger_5bb2d73b-f3a4-43fd-add6-fac9786654ae.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "seated-badger-in-right-profile"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Badger Side Profile"]
    keywords = ["badger", "animal", "profile", "muzzle", "ear", "seated", "wildlife"]
    def build(self):
        self.add_line("rear-foot",(20,40),(10,40))
        self.add_bezier("back",(10,40),((4,40),(4,34),(4,29)),((4,22),(10,18),(16,18)),((20,18),(23,14),(26,12)))
        self.add_arc("ear",(26,12),(34,12),radius_x=4,sweep=True)
        self.add_bezier("muzzle",(34,12),((38,14),(40,20),(44,22)),((41,28),(34,26),(32,28)),((27,31),(26,36),(30,40)))
        self.add_contour("body","rear-foot","back","ear","muzzle")
