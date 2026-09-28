"""Two rounded clouds over a visibly rolling hill, retaining the source's landscape.
Plan: paired clouds use a shared lobe construction; the small third cloud is omitted for SOLO48 clearance so the hill can rise clearly.
Keyshape HRECT_L centerline (4,8)-(44,40). Lucide cloud informs the rounded lobe flow; the source supplies the landscape composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "0e89c2b1-20c5-4992-9ea7-afbe744daa99"
SOURCE_PATH = "icon_set/work/primitive-make-ray/0e89c2b1-20c5-4992-9ea7-afbe744daa99/20260927T165820Z-gpt-6-fix/veldt_0e89c2b1-20c5-4992-9ea7-afbe744daa99.svg"
AUTHOR = "gpt-6"
class CloudsOverRollingHill(Solo48):
 icon_id = "clouds-over-rolling-hill"
 keyshape = Keyshape.HRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "landscape"
 aliases = ("veldt",)
 keywords = ("cloud", "hill", "landscape", "sky")
 def build(self):
  def cloud(label,left):
   p=lambda x,y:(left+x,y)
   self.add_bezier(label+"-shoulder-left",p(0,20),((p(0,17),p(1,15),p(3,15))))
   self.add_bezier(label+"-dome-left",p(3,15),((p(3,11),p(5,8),p(8,8))))
   self.add_bezier(label+"-dome-right",p(8,8),((p(11,8),p(13,11),p(13,15))))
   self.add_bezier(label+"-shoulder-right",p(13,15),((p(15,15),p(16,17),p(16,20))))
   self.add_line(label+"-base",p(16,20),p(0,20))
   self.add_contour(label,*(label+"-"+part for part in ("shoulder-left","dome-left","dome-right","shoulder-right","base")),closed=True)
  cloud("cloud-left",4)
  cloud("cloud-right",28)
  self.add_bezier("hill",(4,40),(((16,34),(32,34),(44,40))))
