"""Round piggy bank with pointed ear, projecting snout, two feet, slot and a short tail.
Plan: one flowing body contour owns the back, face and feet; the short tail and slot are small secondary strokes.
Keyshape HRECT_L centerline (4,8)-(44,40). Lucide piggy-bank informed the smooth back and snout transition.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "dd9a8ecf-ec10-4cd5-8df9-6f2d1088bffa"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__plain-slotted-piggy-bank-dd9a8ecf/20260927T170245Z-thuan-mac-1/reference/piggy bank_dd9a8ecf-ec10-4cd5-8df9-6f2d1088bffa.svg"
AUTHOR = "gpt-6"
class PlainSlottedPiggyBank(Solo48):
 icon_id = "plain-slotted-piggy-bank-dd9a8ecf-solo"
 keyshape = Keyshape.HRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "objects"
 aliases = ("piggy-bank",)
 keywords = ("pig", "bank", "coin", "slot", "savings")
 def build(self):
  self.add_bezier("back",(12,16),(((17,9),(24,9),(30,12))))
  self.add_line("ear-up",(30,12),(36,8))
  self.add_line("ear-down",(36,8),(36,18))
  self.add_bezier("face",(36,18),(((39,19),(42,20),(42,22))))
  self.add_line("snout-top",(42,22),(44,22))
  self.add_line("snout-front",(44,22),(44,28))
  self.add_line("snout-bottom",(44,28),(40,30))
  self.add_bezier("chest",(40,30),(((39,32),(38,33),(38,34))))
  self.add_line("right-leg",(38,34),(38,40))
  self.add_line("right-foot",(38,40),(30,40))
  self.add_line("right-leg-inner",(30,40),(28,34))
  self.add_line("belly",(28,34),(20,34))
  self.add_line("left-leg-inner",(20,34),(20,40))
  self.add_line("left-foot",(20,40),(12,40))
  self.add_line("left-leg",(12,40),(12,34))
  self.add_bezier("rump-lower",(12,34),(((10,32),(8,29),(8,26))))
  self.add_bezier("rump-upper",(8,26),(((8,22),(9,18),(12,16))))
  self.add_contour("pig","back","ear-up","ear-down","face","snout-top","snout-front","snout-bottom","chest","right-leg","right-foot","right-leg-inner","belly","left-leg-inner","left-foot","left-leg","rump-lower","rump-upper",closed=True)
  self.add_line("slot",(20,20),(26,20))
  self.add_line("tail",(8,26),(4,26))
  self.relate("connect","tail","pig")
