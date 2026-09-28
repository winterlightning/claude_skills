from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="b70b7993-149f-4dd9-95d6-fe029f2c8b42"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__saving-bear-increase/20260926T163748Z-thuan-mac/reference/saving bear increase_b70b7993-149f-4dd9-95d6-fe029f2c8b42.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="saving-bear-increase"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="finance"
 aliases=()
 keywords=("savings","bear","increase","growth")
 def build(self):
  self.add_polyline("growth-trend",(6,20),(18,8),(30,10),(42,6))
  self.add_line("arrow-upper",(34,6),(42,6))
  self.add_line("arrow-side",(42,6),(42,14))
  self.relate("connect","growth-trend","arrow-upper")
  self.relate("connect","growth-trend","arrow-side")
  self.relate("connect","arrow-upper","arrow-side")
  self.add_polyline("bear-head",(12,33),(12,29),(14,27),(18,27),(20,29),(28,29),(30,27),(34,27),(36,29),(36,33),(34,35),(33,39),(29,42),(19,42),(15,39),(14,35),(12,33),closed=True)
