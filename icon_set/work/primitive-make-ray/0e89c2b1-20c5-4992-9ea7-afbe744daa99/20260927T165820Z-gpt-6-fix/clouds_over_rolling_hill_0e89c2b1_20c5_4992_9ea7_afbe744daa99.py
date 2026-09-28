"""Three varied clouds over a gently rolling horizon.
Plan: two upper cloud contours and a smaller lower cloud, each with rounded lobes; a separate broad hill arc sits underneath.
Keyshape HRECT_L centerline (4,8)-(44,40). Lucide cloud informs the domed lobe construction; the source supplies the three-cloud arrangement and hill.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "0e89c2b1-20c5-4992-9ea7-afbe744daa99"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__clouds-over-rolling-hill/20260927T164305Z-thuan-mac-1/reference/veldt_0e89c2b1-20c5-4992-9ea7-afbe744daa99.svg"
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
  self.add_bezier("left-shoulder",(4,20),(((4,16),(6,14),(8,14))))
  self.add_bezier("left-dome",(8,14),((8,10),(10,8),(12,8)),((15,8),(17,10),(17,14)))
  self.add_bezier("left-right-lobe",(17,14),(((19,14),(20,17),(20,20))))
  self.add_line("left-base",(20,20),(4,20))
  self.add_contour("cloud-left","left-shoulder","left-dome","left-right-lobe","left-base",closed=True)
  self.add_bezier("right-shoulder",(28,20),(((28,16),(30,14),(32,14))))
  self.add_bezier("right-dome",(32,14),((32,10),(34,8),(36,8)),((39,8),(41,10),(41,14)))
  self.add_bezier("right-right-lobe",(41,14),(((43,14),(44,17),(44,20))))
  self.add_line("right-base",(44,20),(28,20))
  self.add_contour("cloud-right","right-shoulder","right-dome","right-right-lobe","right-base",closed=True)
  self.add_bezier("small-left",(20,30),(((20,29),(22,28),(24,28))))
  self.add_bezier("small-dome",(24,28),((24,28),(26,28),(28,28)),((30,28),(32,29),(32,29)))
  self.add_bezier("small-right",(32,29),(((33,29),(34,30),(34,30))))
  self.add_contour("cloud-small","small-left","small-dome","small-right",closed=False)
  self.add_bezier("hill",(4,40),(((16,38),(32,38),(44,40))))
