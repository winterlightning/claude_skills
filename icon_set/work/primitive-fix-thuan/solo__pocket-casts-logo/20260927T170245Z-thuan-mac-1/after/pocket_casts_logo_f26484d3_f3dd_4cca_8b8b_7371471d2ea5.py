"""Pocket Casts circular badge with two nested open C arcs.
Plan: shared center (24,24), outer radius20, broadcast arcs of radii11 and2, both opening toward the lower right.
Keyshape CIRCLE. No Lucide logo match; repeated circle geometry follows the supplied mark.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "f26484d3-f3dd-4cca-8b8b-7371471d2ea5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__pocket-casts-logo/20260927T170245Z-thuan-mac-1/reference/pocket casts logo_f26484d3-f3dd-4cca-8b8b-7371471d2ea5.svg"
AUTHOR = "gpt-6"
class PocketCastsLogo(Solo48):
 icon_id = "pocket-casts-logo"
 keyshape = Keyshape.CIRCLE
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "logos"
 aliases = ()
 keywords = ("pocket casts", "podcast", "audio", "logo")
 def build(self):
  self.add_arc("outer-top",(4,24),(44,24),radius_x=20,sweep=True)
  self.add_arc("outer-bottom",(44,24),(4,24),radius_x=20,sweep=True)
  self.add_contour("outer","outer-top","outer-bottom",closed=True)
  self.add_arc("broadcast-outer",(35,24),(24,35),radius_x=11,large_arc=True,sweep=False)
  self.add_arc("broadcast-inner",(26,24),(24,26),radius_x=2,large_arc=True,sweep=False)
