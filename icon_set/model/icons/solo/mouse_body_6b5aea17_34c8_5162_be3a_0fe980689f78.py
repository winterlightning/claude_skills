"""A seated mouse facing right, with two round ears, smooth muzzle, pear-shaped haunch and a curved tail. Envelope (8,4)-(40,44).
Construction reference: Lucide rat: round ears, continuous organic silhouette and curling tail.
Omissions: Small eye and haunch crease omitted to protect clear interior."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6b5aea17-34c8-5162-be3a-0fe980689f78'
SOURCE_PATH = 'pictographic-primitives/animals/mouse body_6b5aea17-34c8-5162-be3a-0fe980689f78.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='sitting-mouse'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases=()
    keywords=('mouse', 'body')
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
        path('mouse',(17,16),[('A',(11,10),6,6,True),('A',(17,4),6,6,True),('A',(23,10),6,6,True),('A',(29,4),6,6,True),('A',(35,10),6,6,True),('A',(31,16),6,6,True),('C',(36,21),(34,17),(36,18)),('C',(29,24),(36,24),(32,24)),('L',(29,32)),('C',(28,34),(29,33),(29,34)),('C',(18,44),(27,41),(24,44)),('C',(8,34),(11,44),(8,40)),('C',(17,24),(8,28),(11,26)),('L',(17,16))],True)
        path('tail',(28,34),[('C',(40,44),(38,32),(40,38))]);join('tail','mouse')
