from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="b3607490-ea3a-409f-a7b1-8386a80c0b93"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__tags-double/20260926T163748Z-thuan-mac/reference/tags double_b3607490-ea3a-409f-a7b1-8386a80c0b93.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="tags-double"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="interface-essential"
 aliases=()
 keywords=("double tags","price labels","tags")
 def build(self):
  self.add_polyline("front-tag",(6,14),(22,14),(38,30),(32,34),(28,42),(6,32),closed=True)
  self.add_polyline("rear-tag",(12,6),(26,6),(42,22),(42,26),(38,30))
  self.relate("connect","front-tag","rear-tag")
  self.add_arc("eyelet-left",(15,25),(19,25),radius_x=2,sweep=True)
  self.add_arc("eyelet-right",(19,25),(15,25),radius_x=2,sweep=True)
  self.add_contour("eyelet","eyelet-left","eyelet-right",closed=True)
