"""Open smiling mouth with a gently notched upper lip and visible upper and lower teeth.
Plan: one symmetric lip contour, a broad upper tooth row with three short divisions, and two lower teeth around a central seam.
Keyshape HRECT_L centerline (4,8)-(44,40). No close Lucide mouth reference; curve flow follows the supplied lip silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "8c9b5e16-c176-42c7-adbe-fdcaffda9cfc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__open-smiling-mouth-teeth/20260927T164305Z-thuan-mac-1/reference/teeth open_8c9b5e16-c176-42c7-adbe-fdcaffda9cfc.svg"
AUTHOR = "gpt-6"
class OpenSmilingMouthTeeth(Solo48):
 icon_id = "open-smiling-mouth-teeth"
 keyshape = Keyshape.HRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "anatomy"
 aliases = ("smile-with-teeth",)
 keywords = ("mouth", "smile", "teeth", "open")
 def build(self):
  self.add_bezier("upper-left",(4,20),(((8,12),(16,8),(21,8))))
  self.add_bezier("notch-left",(21,8),(((22,8),(23,10),(24,10))))
  self.add_bezier("notch-right",(24,10),(((25,10),(26,8),(27,8))))
  self.add_bezier("upper-right",(27,8),(((32,8),(40,12),(44,20))))
  self.add_bezier("lower-right",(44,20),(((44,31),(33,40),(24,40))))
  self.add_bezier("lower-left",(24,40),(((15,40),(4,31),(4,20))))
  self.add_contour("mouth","upper-left","notch-left","notch-right","upper-right","lower-right","lower-left",closed=True)
  self.add_line("upper-teeth",(4,20),(44,20))
  self.relate("connect","mouth","upper-teeth")
  for x in (16,24,32):
   self.add_line(f"upper-seam-{x}",(x,20),(x,22))
   self.relate("connect","upper-teeth",f"upper-seam-{x}")
  self.add_line("lower-teeth",(18,30),(30,30))
  self.add_line("lower-seam",(24,30),(24,40))
  self.relate("connect","lower-teeth","lower-seam")
  self.relate("connect","mouth","lower-seam")
