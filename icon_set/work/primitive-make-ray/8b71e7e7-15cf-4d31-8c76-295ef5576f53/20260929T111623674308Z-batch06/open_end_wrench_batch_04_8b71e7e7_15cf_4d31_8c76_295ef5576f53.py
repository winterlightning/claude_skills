"""The rejected wrench omitted the lightning bolt visible in the reference. Restored the bolt beside an open diagonal wrench outline and kept the fork recognizable.
Plan: Lucide wrench: coherent fork and rounded handle contour. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='8b71e7e7-15cf-4d31-8c76-295ef5576f53'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__open-end-wrench-batch-04/20260929T111229Z-thuan-mac/reference/flash wrench_8b71e7e7-15cf-4d31-8c76-295ef5576f53.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='open-end-wrench-batch-04'
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

        path('wrench',(32,6),[('L',(24,14)),('L',(34,24)),('L',(42,16)),('C',(34,30),(42,24),(39,28))])
        path('handle',(32,6),[('C',(18,18),(23,6),(16,10)),('L',(6,30)),('C',(10,38),(6,34),(6,38))])
        join('wrench','handle')
        poly('bolt',(26,26),(18,36),(38,34),(30,42))
