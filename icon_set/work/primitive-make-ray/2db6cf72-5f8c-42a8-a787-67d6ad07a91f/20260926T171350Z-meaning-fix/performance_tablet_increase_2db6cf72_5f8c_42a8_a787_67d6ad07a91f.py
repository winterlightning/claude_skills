from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="2db6cf72-5f8c-42a8-a787-67d6ad07a91f"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__performance-tablet-increase/20260926T163748Z-thuan-mac/reference/performance tablet increase_2db6cf72-5f8c-42a8-a787-67d6ad07a91f.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="performance-tablet-increase"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="business"
 aliases=()
 keywords=("tablet","hand","performance","growth chart")
 def build(self):
  self.add_line("tablet-top",(6,6),(34,6))
  self.add_line("tablet-left",(6,6),(6,42))
  self.add_line("tablet-bottom",(6,42),(34,42))
  self.add_line("tablet-right-top",(34,6),(34,18))
  self.add_line("tablet-right-bottom",(34,38),(34,42))
  self.add_polyline("chart-trend",(14,26),(18,22),(22,24),(26,16))
  self.add_line("chart-arrow-left",(22,16),(26,16))
  self.add_line("chart-arrow-down",(26,16),(26,22))
  self.relate("connect","chart-trend","chart-arrow-left")
  self.relate("connect","chart-trend","chart-arrow-down")
  self.relate("connect","chart-arrow-left","chart-arrow-down")
  self.add_polyline("gripping-hand",(34,18),(42,26),(42,42))
  self.relate("connect","tablet-right-top","gripping-hand")
  self.relate("connect","tablet-right-bottom","gripping-hand")
