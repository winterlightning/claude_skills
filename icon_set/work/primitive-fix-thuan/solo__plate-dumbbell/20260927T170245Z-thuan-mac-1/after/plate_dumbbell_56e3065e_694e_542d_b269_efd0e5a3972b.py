"""Symmetric plate dumbbell with two matching rounded weights, a shaft, and end caps.
Plan: the plate definition is repeated at two positions; all attachments reuse wall midpoint nodes.
Keyshape HRECT_L centerline (4,8)-(44,40). Lucide dumbbell informed the shared bar and repeated weight structure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "56e3065e-694e-542d-b269-efd0e5a3972b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__plate-dumbbell/20260927T170245Z-thuan-mac-1/reference/fitness grip weights_56e3065e-694e-542d-b269-efd0e5a3972b.svg"
AUTHOR = "gpt-6"
class PlateDumbbell(Solo48):
 icon_id = "plate-dumbbell"
 keyshape = Keyshape.HRECT_L
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "sports"
 aliases = ()
 keywords = ("dumbbell", "plate", "weight", "fitness")
 def build(self):
  def plate(label,x):
   pts=((x+2,8),(x+6,8),(x+8,10),(x+8,24),(x+8,38),(x+6,40),(x+2,40),(x,38),(x,24),(x,10))
   parts=[]
   for j,a in enumerate(pts):
    b=pts[(j+1)%len(pts)];n=f"{label}-{j}";parts.append(n)
    if j in (1,4,6,9):self.add_arc(n,a,b,radius_x=2,sweep=True)
    else:self.add_line(n,a,b)
   self.add_contour(label,*parts,closed=True)
  plate("left-plate",10)
  plate("right-plate",30)
  self.add_line("shaft",(18,24),(30,24))
  self.add_line("left-cap",(4,24),(10,24))
  self.add_line("right-cap",(38,24),(44,24))
  for a,b in (("shaft","left-plate"),("shaft","right-plate"),("left-cap","left-plate"),("right-cap","right-plate")):self.relate("connect",a,b)
