"""A whale with rounded body, raised split tail, a curved flipper and detached water spout. Bounds (6,6)-(42,42).
Construction reference: Lucide fish: continuous rounded aquatic silhouette and identifiable appendage.
Omissions: Fine far flipper omitted; spout kept detached."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2977768a-df8d-5260-854a-5df367e6906c'
SOURCE_PATH = 'pictographic-primitives/animals/whale body_2977768a-df8d-5260-854a-5df367e6906c.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='whale-with-spout'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="nature/animals"
    aliases=()
    keywords=('whale', 'body')
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
        path('whale',(6,30),[('C',(20,19),(6,23),(12,19)),('C',(32,25),(26,19),(27,24)),('C',(34,16),(35,25),(34,20)),('L',(33,11)),('L',(38,15)),('L',(42,11)),('L',(42,22)),('C',(23,42),(42,35),(34,42)),('C',(6,30),(13,42),(6,38))],True)
        path('spout',(11,6),[('C',(19,11),(15,6),(17,8)),('C',(26,6),(21,8),(24,6))])
        path('flipper',(10,36),[('C',(22,34),(14,34),(19,33))]);join('flipper','whale')
