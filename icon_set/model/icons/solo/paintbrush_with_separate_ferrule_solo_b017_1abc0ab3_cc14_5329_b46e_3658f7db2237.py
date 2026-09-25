"""Diagonal paintbrush with curved handle, distinct wide ferrule and a soft bristle tip. Shared diagonal attachment nodes keep the three parts coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1abc0ab3-cc14-5329-b46e-3658f7db2237'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/brush_1abc0ab3-cc14-5329-b46e-3658f7db2237.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='paintbrush-with-separate-ferrule-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Diagonal paintbrush with curved handle, distinct wide ferrule and a soft bristle tip. Shared diagonal attachment nodes keep the three parts coherent.

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

        path('handle',(22,16),[('L',(32,8)),('C',(36,6),(33,6),(34,6)),('A',(42,12),6,6,True),('C',(40,16),(42,14),(42,15)),('L',(36,30))])
        self.add_polyline('ferrule',(16,22),(22,16),(36,30),(30,36),closed=True);join('handle','ferrule')
        path('bristles',(16,22),[('C',(10,30),(11,22),(10,26)),('C',(6,42),(10,36),(9,40)),('C',(26,38),(15,42),(22,42)),('C',(30,36),(28,37),(30,36))]);join('bristles','ferrule')
