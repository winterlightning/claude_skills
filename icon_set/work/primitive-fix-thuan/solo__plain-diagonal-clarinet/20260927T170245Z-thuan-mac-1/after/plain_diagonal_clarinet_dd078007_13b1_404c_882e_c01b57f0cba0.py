"""Plain clarinet angled from a flared lower bell to a rounded upper mouthpiece.
Plan: one tapered outline owns the bell, shaft and mouthpiece; one seam marks the mouthpiece; the bell flare carries the lower section change.
Keyshape SQUARE centerline (6,6)-(42,42). No exact Lucide clarinet match; diagonal tube follows the reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "dd078007-13b1-404c-882e-c01b57f0cba0"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__plain-diagonal-clarinet/20260927T170245Z-thuan-mac-1/reference/clarinet_dd078007-13b1-404c-882e-c01b57f0cba0.svg"
AUTHOR = "gpt-6"
class PlainDiagonalClarinet(Solo48):
 icon_id = "plain-diagonal-clarinet"
 keyshape = Keyshape.SQUARE
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "music"
 aliases = ("clarinet",)
 keywords = ("clarinet", "instrument", "woodwind")
 def build(self):
  self.add_line("mouth-upper",(30,6),(38,6))
  self.add_arc("mouth-round",(38,6),(42,10),radius_x=4,sweep=True)
  self.add_line("mouth-right",(42,10),(36,18))
  self.add_line("shaft-right",(36,18),(18,36))
  self.add_line("bell-right",(18,36),(16,42))
  self.add_line("bell-rim",(16,42),(6,32))
  self.add_bezier("bell-left",(6,32),(((9,33),(10,31),(12,30))))
  self.add_line("shaft-left",(12,30),(28,12))
  self.add_line("mouth-left",(28,12),(30,6))
  self.add_contour("clarinet","mouth-upper","mouth-round","mouth-right","shaft-right","bell-right","bell-rim","bell-left","shaft-left","mouth-left",closed=True)
  self.add_line("mouth-seam",(28,12),(36,18))
  self.relate("connect","clarinet","mouth-seam")
