from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="f3c9dbea-9e4f-4e89-b366-3b67f9116e34"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__text-options/20260926T163748Z-thuan-mac/reference/text options_f3c9dbea-9e4f-4e89-b366-3b67f9116e34.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="text-options"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="interface-essential"
 aliases=()
 keywords=("letter A","dropdown","text formatting")
 def build(self):
  self.add_polyline("capital-A",(12,24),(24,6),(36,24))
  self.add_line("A-crossbar",(18,15),(30,15))
  self.add_polyline("options-field",(10,33),(38,33),(42,37),(42,38),(38,42),(10,42),(6,38),(6,37),(10,33),closed=True)
