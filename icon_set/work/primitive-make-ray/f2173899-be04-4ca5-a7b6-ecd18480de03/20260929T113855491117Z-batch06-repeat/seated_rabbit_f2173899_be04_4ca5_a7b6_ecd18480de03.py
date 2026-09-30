"""The rejected rabbit had two rigid vertical antenna-like ears. Tilted and rounded the ears to follow the reference direction while retaining its broad seated body and muzzle. Omitted the eye and small hind-leg loop.
Plan: Lucide rabbit: backward-leaning rounded ears and seated haunch. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='f2173899-be04-4ca5-a7b6-ecd18480de03'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seated-rabbit/20260929T112716Z-thuan-mac/reference/leveret_f2173899-be04-4ca5-a7b6-ecd18480de03.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='seated-rabbit'
    keyshape=Keyshape.SQUARE
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

        path('rabbit',(14,22),[('L',(10,11)),('A',(20,11),5,5,True),('L',(22,20)),('L',(31,20)),('L',(29,11)),('A',(39,11),5,5,True),('L',(40,22)),('A',(42,26),2,4,True),('L',(42,30)),('L',(34,34)),('L',(38,42)),('L',(14,42)),('A',(6,34),8,8,True),('A',(14,22),8,12,True)],True)
