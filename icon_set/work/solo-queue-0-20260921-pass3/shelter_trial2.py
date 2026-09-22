from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID="8d2595e2-135f-48bd-8886-08c5da475869"
SOURCE_PATH="pictographic-primitives/_uncategorized_16/earthquake hiding proof table_8d2595e2-135f-48bd-8886-08c5da475869.svg"
AUTHOR="gpt-6-astra"
class Drawing(Solo48):
 icon_id="person-sheltering-beneath-shaking-table"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="Uncategorized"
 aliases=("Earthquake Shelter Under Table",)
 keywords=("earthquake","shelter","person","table","crouching","safety","shaking")
 def build(self):
  self.add_polyline("table",(6,42),(6,16),(42,16),(42,42))
  for index,left in enumerate([8,32]):
   self.add_polyline(f"vibration-{index}",(left,8),(left+3,6),(left+6,8))
  self.add_arc("head-top",(26,28),(34,28),radius_x=4)
  self.add_arc("head-bottom",(34,28),(26,28),radius_x=4)
  self.add_contour("head","head-top","head-bottom",closed=True)
  self.add_line("torso",(18,28),(14,28))
  self.add_bezier("leg-bend",(14,28),((14,34),(18,38),(22,42)))
  self.add_line("foot",(22,42),(14,42))
  self.add_contour("legs","leg-bend","foot")
  self.relate("connect","torso","legs")
  self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")
