"""The rejected car body floated far above its wheels and the hood was a short stub. Lowered and rounded the body around larger wheels, joined them with the sill, and gave the raised hood a clear hinged angle.
Plan: Lucide car: wheels nested into an open lower body outline. Keyshape HRECT_M; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='de4837e9-fc58-4000-be76-deb74b0a3723'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__side-view-car-with-open-hood/20260929T112716Z-thuan-mac/reference/car hood release_de4837e9-fc58-4000-be76-deb74b0a3723.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='side-view-car-with-open-hood'
    keyshape=Keyshape.HRECT_M
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

        path('body',(8,34),[('L',(4,34)),('L',(4,22)),('A',(8,18),4,4,True),('L',(16,18)),('L',(24,10)),('L',(32,10)),('L',(40,18)),('A',(44,22),4,4,True),('L',(44,34)),('L',(40,34))])
        circle('wheel-left',12,34,4);circle('wheel-right',36,34,4);join('body','wheel-left');join('body','wheel-right')
        line('sill',(16,34),(32,34));join('sill','wheel-left');join('sill','wheel-right')
        poly('hood',(16,18),(8,10),(4,10));join('hood','body')
