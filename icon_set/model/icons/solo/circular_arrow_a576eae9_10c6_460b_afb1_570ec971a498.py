"""Clockwise circular arrow with a full rounded sweep and an upper-right open head; fewer coherent arcs remove the rejected kink."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a576eae9-10c6-460b-afb1-570ec971a498'
SOURCE_PATH = 'pictographic-primitives/state/circular arrow_a576eae9-10c6-460b-afb1-570ec971a498.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='circular-arrow'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="state"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Clockwise circular arrow with a full rounded sweep and an upper-right open head; fewer coherent arcs remove the rejected kink.

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

        path('arc',(42,28),[('C',(24,42),(40,37),(33,42)),('A',(6,24),18,18,True),('A',(24,6),18,18,True),('C',(40,16),(31,6),(36,10))])
        self.add_polyline('head',(40,6),(40,16),(30,16));join('head','arc')
