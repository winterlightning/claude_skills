from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID="8d2595e2-135f-48bd-8886-08c5da475869"
SOURCE_PATH="pictographic-primitives/_uncategorized_16/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg"
AUTHOR="gpt-6-astra"
class Drawing(Solo48):
 icon_id="person-sheltering-beneath-shaking-table"
 keyshape=Keyshape.HRECT_L
 semantic_role="MAIN"
 semantic_kind="noun"
 category="Uncategorized"
 aliases=("Earthquake Shelter Under Table",)
 keywords=("earthquake","shelter","person","table","crouching","safety","shaking")
 def build(self):
  self.add_polyline("table",(4,40),(4,20),(44,20),(44,40))
  for index,left in enumerate([8,32]):
   self.add_polyline(f"vibration-{index}",(left,12),(left+4,8),(left+8,12))
  self.add_arc("head-top",(28,32),(36,32),radius_x=4)
  self.add_arc("head-bottom",(36,32),(28,32),radius_x=4)
  self.add_contour("head","head-top","head-bottom",closed=True)
  self.add_line("torso",(20,32),(14,32))
  self.add_polyline("legs",(14,32),(22,40),(14,40))
  self.relate("connect","torso","legs")
  self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")
