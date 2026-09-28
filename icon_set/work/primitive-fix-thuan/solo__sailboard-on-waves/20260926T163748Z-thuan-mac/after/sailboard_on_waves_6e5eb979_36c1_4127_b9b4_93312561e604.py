from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="6e5eb979-36c1-4127-b9b4-93312561e604"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__sailboard-on-waves/20260926T163748Z-thuan-mac/reference/nautic sports sailing_6e5eb979-36c1-4127-b9b4-93312561e604.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="sailboard-on-waves"
 keyshape=Keyshape.VRECT_L
 semantic_role="MAIN"
 semantic_kind="noun"
 category="recreation"
 aliases=()
 keywords=("windsurfing","sailboard","sailing","waves")
 def build(self):
  self.add_line("sail-leading-edge",(32,4),(8,26))
  self.add_line("sail-foot",(8,26),(32,26))
  self.add_line("mast",(32,4),(32,34))
  self.add_line("board-left",(8,34),(32,34))
  self.add_line("board-nose",(32,34),(40,30))
  self.add_polyline("waves",(8,44),(14,42),(20,44),(26,42),(32,44),(38,42),(40,44))
  self.relate("connect","sail-leading-edge","mast")
  self.relate("connect","sail-foot","mast")
  self.relate("connect","mast","board-left")
