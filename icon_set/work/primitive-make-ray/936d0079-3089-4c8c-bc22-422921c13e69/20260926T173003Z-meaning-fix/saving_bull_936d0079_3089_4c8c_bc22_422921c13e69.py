from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="936d0079-3089-4c8c-bc22-422921c13e69"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__saving-bull/20260926T163748Z-thuan-mac/reference/saving bull_936d0079-3089-4c8c-bc22-422921c13e69.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="saving-bull"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="finance"
 aliases=()
 keywords=("bull","savings","growth","increase")
 def build(self):
  self.add_polyline("bull-body",(6,28),(12,22),(26,22),(29,20),(28,16),(32,20),(34,22),(38,24),(42,26),(42,30),(36,32),(32,32),(16,32),(6,32),(6,28),closed=True)
  self.add_line("rear-leg",(16,32),(16,42))
  self.add_line("front-leg",(32,32),(32,42))
  self.relate("connect","bull-body","rear-leg")
  self.relate("connect","bull-body","front-leg")
  self.add_polyline("growth-trend",(40,14),(42,6))
  self.add_line("arrow-upper",(34,6),(42,6))
  self.add_line("arrow-side",(42,6),(42,14))
  self.relate("connect","growth-trend","arrow-upper")
  self.relate("connect","growth-trend","arrow-side")
  self.relate("connect","arrow-upper","arrow-side")
