"""Pointed peach with its leaf attached at the stem and a left interior crease.
Plan: mirror the two fruit lobes about x=24; keep the leaf deliberately asymmetric to follow the source.
Keyshape VRECT_L centerline (8,4)-(40,44). Lucide apple informed the rounded fruit sides, while the source determines the pointed base.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "e6a87b3d-94a4-46f8-af27-20389bcf0cab"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__pointed-peach-leaf/20260927T164305Z-thuan-mac-1/reference/peach_e6a87b3d-94a4-46f8-af27-20389bcf0cab.svg"
AUTHOR = "gpt-6"
class PointedPeachLeaf(Solo48):
 icon_id = "pointed-peach-leaf"
 keyshape = Keyshape.VRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "fruit"
 aliases = ("peach",)
 keywords = ("peach", "fruit", "leaf")
 def build(self):
  self.add_bezier("fruit-upper-left",(24,16),(((16,13),(8,20),(8,28))))
  self.add_bezier("fruit-lower-left",(8,28),(((8,37),(18,41),(24,44))))
  self.add_bezier("fruit-lower-right",(24,44),(((30,41),(40,37),(40,28))))
  self.add_bezier("fruit-upper-right",(40,28),(((40,20),(32,13),(24,16))))
  self.add_contour("fruit","fruit-upper-left","fruit-lower-left","fruit-lower-right","fruit-upper-right",closed=True)
  self.add_bezier("leaf-upper",(24,16),(((27,6),(32,4),(38,4))))
  self.add_bezier("leaf-lower",(38,4),(((36,12),(31,16),(24,16))))
  self.add_contour("leaf","leaf-upper","leaf-lower",closed=True)
  self.relate("connect","fruit","leaf")
  self.add_bezier("crease",(24,16),(((20,19),(18,23),(18,28))))
  self.relate("connect","fruit","crease")
