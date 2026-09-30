"""The rejected diagonal pad was almost circular, with a short central opening. Reoriented it upright and elongated both the outer pad and inset absorbent panel so it reads as a pad.
Plan: Lucide pill: tangent capsule ends; supplied reference: nested absorbent panel. Keyshape VRECT_M; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='31816e20-325b-4b31-8b23-a9a4d37a4bdf'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__sanitary-pad/20260929T112716Z-thuan-mac/reference/sanitary pad_31816e20-325b-4b31-8b23-a9a4d37a4bdf.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='sanitary-pad'
    keyshape=Keyshape.VRECT_M
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

        path('pad',(10,18),[('A',(38,18),14,14,True),('L',(38,30)),('A',(10,30),14,14,True),('L',(10,18))],True)
        path('panel',(20,18),[('A',(28,18),4,4,True),('L',(28,30)),('A',(20,30),4,4,True),('L',(20,18))],True)
