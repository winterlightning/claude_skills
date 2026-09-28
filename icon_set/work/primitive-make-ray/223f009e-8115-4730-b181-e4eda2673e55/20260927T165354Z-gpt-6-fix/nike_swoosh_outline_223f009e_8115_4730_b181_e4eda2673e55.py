"""Outlined Nike swoosh with an open hooked heel and a long rising tail.
Plan: a single continuous contour uses a broad lower sweep, concave upper cutout, and tapering tip. Deliberate asymmetry preserves the directional mark.
Keyshape HRECT_M centerline (4,10)-(44,38). No useful Lucide counterpart for this brand silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "223f009e-8115-4730-b181-e4eda2673e55"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__nike-swoosh-outline-223f009e/20260927T164305Z-thuan-mac-1/reference/nike logo_223f009e-8115-4730-b181-e4eda2673e55.svg"
AUTHOR = "gpt-6"
class NikeSwooshOutline(Solo48):
 icon_id = "nike-swoosh-outline-223f009e"
 keyshape = Keyshape.HRECT_M
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "logos"
 aliases = ("nike-swoosh",)
 keywords = ("nike", "swoosh", "logo")
 def build(self):
  self.add_bezier("heel-outer",(10,10),(((6,16),(4,22),(4,27))))
  self.add_bezier("lower-hook",(4,27),(((4,34),(7,38),(12,38))))
  self.add_bezier("tail-outer",(12,38),(((20,38),(36,18),(44,10))))
  self.add_bezier("tail-inner",(44,10),(((34,14),(23,23),(16,24))))
  self.add_bezier("heel-inner",(16,24),(((7,27),(7,17),(10,10))))
  self.add_contour("swoosh","heel-outer","lower-hook","tail-outer","tail-inner","heel-inner",closed=True)
