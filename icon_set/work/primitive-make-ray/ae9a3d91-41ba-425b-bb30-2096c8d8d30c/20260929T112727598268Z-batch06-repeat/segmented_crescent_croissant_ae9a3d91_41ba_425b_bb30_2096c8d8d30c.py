"""The rejected pastry was a thin symmetric arch with pointed tips. Restored a plump asymmetric crescent with rounded tapered ends and curved segment seams, following the reference tilt.
Plan: Lucide croissant: plump segmented body and rounded tapered ends. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='ae9a3d91-41ba-425b-bb30-2096c8d8d30c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__segmented-crescent-croissant/20260929T112544Z-thuan-mac/reference/pastry_ae9a3d91-41ba-425b-bb30-2096c8d8d30c.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='segmented-crescent-croissant'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                members.append(member);here=end
            self.add_contour(name,*members,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*pts): self.add_polyline(name,*pts)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r): path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('pastry',(4,32),[('C',(12,14),(4,24),(8,18)),('C',(27,8),(16,10),(23,8)),('C',(40,18),(34,8),(39,12)),('C',(44,30),(43,22),(44,26)),('A',(38,34),5,5,True),('C',(29,25),(34,32),(33,26)),('C',(19,28),(25,23),(22,25)),('C',(14,40),(18,31),(18,40)),('C',(4,32),(8,40),(4,38))],True)
        path('seam-left',(12,14),[('C',(19,28),(18,16),(21,22))]);join('seam-left','pastry')
        path('seam-right',(34,10),[('C',(29,25),(36,15),(34,22))]);join('seam-right','pastry')
