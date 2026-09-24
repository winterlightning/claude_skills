"""Counterclockwise circular arrow: three tangent quarter circles and a clean open head. Lucide undo-2 informs the circular arc and shared arrowhead node; intentional directional asymmetry."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='567f7df5-55ba-4b86-8f69-4c5a4f43e848'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__counterclockwise-circular-arrow-batch-021-03/20260924T083211Z-thuan-mac/reference/go backward_567f7df5-55ba-4b86-8f69-4c5a4f43e848.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='counterclockwise-circular-arrow-batch-021-03'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Counterclockwise circular arrow: three tangent quarter circles and a clean open head. Lucide undo-2 informs the circular arc and shared arrowhead node; intentional directional asymmetry.

        def path(n,start,commands,closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                m=f'{n}-{i}'
                if kind=='L': self.add_line(m,start,end)
                elif kind=='A': self.add_arc(m,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,start,(args[0],args[1],end))
                members.append(m);start=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry=None):
            ry=rx if ry is None else ry
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        path('arc',(24,42),[('A',(42,24),18,18,False),('A',(24,6),18,18,False),('A',(6,24),18,18,False)])
        self.add_polyline('arrowhead',(6,14),(6,24),(16,24));join('arc','arrowhead')
