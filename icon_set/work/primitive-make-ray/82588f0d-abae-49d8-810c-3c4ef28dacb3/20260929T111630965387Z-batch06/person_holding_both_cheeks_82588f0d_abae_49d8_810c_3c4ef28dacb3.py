"""The rejected hands were square-ended pillars against a stretched head. Rebuilt the head with circular arcs and rounded both cupping fingertips symmetrically. Kept the blank face of the source.
Plan: Human user.svg: circular head vocabulary; source hands cup both cheeks. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='82588f0d-abae-49d8-810c-3c4ef28dacb3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-holding-both-cheeks/20260929T111229Z-thuan-mac/reference/screamer_82588f0d-abae-49d8-810c-3c4ef28dacb3.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-holding-both-cheeks'
    keyshape=Keyshape.VRECT_L
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

        path('head',(8,24),[('A',(24,8),16,16,True),('A',(40,24),16,16,True)])
        path('left-hand',(8,44),[('L',(8,28)),('A',(16,28),4,4,True),('L',(16,44))]);join('head','left-hand')
        path('right-hand',(40,44),[('L',(40,28)),('A',(32,28),4,4,False),('L',(32,44))]);join('head','right-hand')
        path('chin',(16,32),[('A',(32,32),10,10,False)]);join('chin','left-hand');join('chin','right-hand')
