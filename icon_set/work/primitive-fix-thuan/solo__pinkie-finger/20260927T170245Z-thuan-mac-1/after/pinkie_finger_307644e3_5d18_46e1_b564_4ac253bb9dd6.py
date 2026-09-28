"""Open hand with four stepped fingers and a raised rightmost pinkie.
Plan: four equal-width rounded tips rise in sequence; one smooth palm joins the outer sides. The long rightmost finger follows the source's deliberate asymmetry.
Keyshape VRECT_L centerline (8,4)-(40,44). Shared human_ref/user.svg and full_body_ref.png informed spare hand anatomy; Lucide hand informed round fingertips.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "307644e3-5d18-46e1-b564-4ac253bb9dd6"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__pinkie-finger/20260927T170245Z-thuan-mac-1/reference/pinkie finger_307644e3-5d18-46e1-b564-4ac253bb9dd6.svg"
AUTHOR = "gpt-6"
class PinkieFinger(Solo48):
 icon_id = "pinkie-finger"
 keyshape = Keyshape.VRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "wayfinding"
 aliases = ()
 keywords = ("pinkie", "finger", "hand", "gesture")
 def build(self):
  self.add_line("left-side",(8,32),(8,24))
  self.add_arc("tip-one",(8,24),(16,24),radius_x=4,sweep=True)
  self.add_line("rise-two",(16,24),(16,20))
  self.add_arc("tip-two",(16,20),(24,20),radius_x=4,sweep=True)
  self.add_line("rise-three",(24,20),(24,18))
  self.add_arc("tip-three",(24,18),(32,18),radius_x=4,sweep=True)
  self.add_line("rise-four",(32,18),(32,8))
  self.add_arc("tip-four",(32,8),(40,8),radius_x=4,sweep=True)
  self.add_line("right-side",(40,8),(40,32))
  self.add_arc("palm",(40,32),(8,32),radius_x=16,radius_y=12,sweep=True)
  self.add_contour("hand","left-side","tip-one","rise-two","tip-two","rise-three","tip-three","rise-four","tip-four","right-side","palm",closed=True)
  for x,y in ((16,24),(24,20),(32,18)):
   n=f"crease-{x}";self.add_line(n,(x,y),(x,y+7));self.relate("connect","hand",n)
