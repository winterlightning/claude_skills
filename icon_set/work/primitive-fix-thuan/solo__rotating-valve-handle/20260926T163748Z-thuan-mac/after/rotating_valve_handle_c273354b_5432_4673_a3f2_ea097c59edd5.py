from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="c273354b-5432-4673-a3f2-ea097c59edd5"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__rotating-valve-handle/20260926T163748Z-thuan-mac/reference/valve_c273354b-5432-4673-a3f2-ea097c59edd5.svg"
AUTHOR="gpt-6"
class Drawing(Solo48):
 icon_id="rotating-valve-handle"
 keyshape=Keyshape.SQUARE
 semantic_role="MAIN"
 semantic_kind="noun"
 category="construction"
 aliases=()
 keywords=("valve","handle","rotation")
 def path(self,name,start,ops):
  at=start;members=[]
  for n,op in enumerate(ops):
   ident=f"{name}-{n}"
   if len(op)==2:self.add_line(ident,at,op);at=op
   else:
    end,rx,ry,sweep=op;self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep);at=end
   members.append(ident)
  self.add_contour(name,*members)
 def build(self):
  self.path("handle",(19,14),[(29,14),((29,22),4,4,True),(24,22),(19,22),((19,14),4,4,True)])
  self.add_line("stem",(24,22),(24,42))
  self.relate("connect","stem","handle")
  self.path("left-rotation",(12,6),[((6,18),15,15,False),(6,30),(12,30)])
  self.add_polyline("left-arrowhead",(6,22),(6,30),(14,30))
  self.relate("connect","left-arrowhead","left-rotation")
  self.path("right-rotation",(36,30),[((42,18),15,15,False),(42,6),(34,6)])
  self.add_polyline("right-arrowhead",(34,6),(42,6),(42,14))
  self.relate("connect","right-arrowhead","right-rotation")
  self.add_line("base",(6,42),(42,42))
  self.relate("connect","stem","base")
