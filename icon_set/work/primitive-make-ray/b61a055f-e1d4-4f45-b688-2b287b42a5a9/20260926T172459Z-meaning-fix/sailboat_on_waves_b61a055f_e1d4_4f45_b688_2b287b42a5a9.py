from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="b61a055f-e1d4-4f45-b688-2b287b42a5a9"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__sailboat-on-waves/20260926T163748Z-thuan-mac/reference/boat_b61a055f-e1d4-4f45-b688-2b287b42a5a9.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="sailboat-on-waves"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="transportation"
 aliases=()
 keywords=("sailing","boat","sail","waves")
 def build(self):
  self.add_line("sail-leading-edge",(32,6),(12,20))
  self.add_line("sail-foot",(12,16),(32,16))
  self.add_line("mast",(32,6),(32,24))
  self.add_line("hull-top-left",(6,24),(32,24))
  self.add_line("hull-top-right",(32,24),(42,24))
  self.add_line("hull-right",(42,24),(36,32))
  self.add_line("hull-bottom",(36,32),(12,32))
  self.add_line("hull-left",(12,32),(6,24))
  self.add_contour("hull","hull-top-left","hull-top-right","hull-right","hull-bottom","hull-left",closed=True)
  self.add_polyline("waves",(6,42),(12,40),(18,42),(24,42),(30,40),(36,42),(42,42))
  self.relate("connect","sail-leading-edge","mast")
  self.relate("connect","sail-foot","mast")
  self.relate("connect","mast","hull-top-left")
  self.relate("connect","mast","hull-top-right")
