"""A circular smiling face with arched eyes and tongue protruding from the right of its mouth. Radius20 centered24; mirrored eye construction and intentionally asymmetric tongue.
Construction reference: Shared human reference: round heads; original reference owns expression.
Omissions: None."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd331b73b-057f-59d7-923b-6ed15186434b'
SOURCE_PATH = 'pictographic-primitives/smileys/tongue_d331b73b-057f-59d7-923b-6ed15186434b.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='smiling-face-with-side-tongue'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="people/emotions"
    aliases=()
    keywords=('tongue',)
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        oval('face',24,24,20,20)
        for x in (16,28):
         path('eye-'+str(x),(x,18),[('A',(x+4,18),2,2,True)])
        path('mouth',(14,26),[('C',(22,28),(17,29),(20,29)),('L',(22,30)),('A',(30,30),4,4,False),('L',(30,26))])
