"""Two shallow stacked serving plates with wide straight rims and flat bowl bases.
Plan: repeat one plate definition at y8 and y28, with overhanging rims and curved sides.
Keyshape HRECT_L centerline (4,8)-(44,40). Lucide cup-soda informed smooth bowl transition; the source defines the wide rim.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "45ea99fe-26d3-4c90-807c-75e170dc824c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__plates/20260927T170245Z-thuan-mac-1/reference/plates_45ea99fe-26d3-4c90-807c-75e170dc824c.svg"
AUTHOR = "gpt-6"
class Plates(Solo48):
 icon_id = "plates"
 keyshape = Keyshape.HRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "hotels"
 aliases = ()
 keywords = ("plate", "stack", "dish", "serving")
 def build(self):
  for label,y in (("top",8),("bottom",28)):
   self.add_line(label+"-rim-left",(4,y),(8,y))
   self.add_line(label+"-rim-middle",(8,y),(40,y))
   self.add_line(label+"-rim-right",(40,y),(44,y))
   self.add_contour(label+"-rim",label+"-rim-left",label+"-rim-middle",label+"-rim-right")
   self.add_bezier(label+"-bowl-left",(8,y),(((9,y+7),(13,y+12),(20,y+12))))
   self.add_line(label+"-bowl-bottom",(20,y+12),(28,y+12))
   self.add_bezier(label+"-bowl-right",(28,y+12),(((35,y+12),(39,y+7),(40,y))))
   self.add_contour(label+"-bowl",label+"-bowl-left",label+"-bowl-bottom",label+"-bowl-right")
   self.relate("connect",label+"-rim",label+"-bowl")
