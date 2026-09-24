"""Three repeated smoke strokes above a curved bowl on mirrored splayed legs; lengthen wisps and make bowl curvature continuous.
Construction: Lucide soup: coherent bowl and repeated curved steam.
Omissions: Lower leg crossbar omitted to avoid a narrow band under the bowl.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b55f60b7-bd1e-53bf-a79a-b549edab3c92'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smoking-barbecue-grill/20260924T071425Z-thuan-mac/reference/barbecue grill_b55f60b7-bd1e-53bf-a79a-b549edab3c92.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smoking-barbecue-grill-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('barbecue', 'grill')

    def build(self):
        # Symbol plan: Three repeated smoke strokes above a curved bowl on mirrored splayed legs; lengthen wisps and make bowl curvature continuous.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('bowl',(6,23),[('L',(42,23)),('C',(32,32),(42,27),(37,31)),('C',(24,34),(29,34),(27,34)),('C',(16,32),(21,34),(19,34)),('C',(6,23),(11,31),(6,27))],True)
        line('left-leg',(16,32),(11,42));line('right-leg',(32,32),(37,42))
        join('left-leg','bowl');join('right-leg','bowl')
        for i,x in enumerate((14,24,34)):
         p(f'smoke-{i}',(x,6),[('C',(x,15),(x-4,9),(x+4,12))])

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            n=f'{name}-{i}'
            if kind=='L': self.add_line(n,start,end)
            elif kind=='A': self.add_arc(n,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(n,start,(args[0],args[1],end))
            members.append(n);start=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def mirror(self,n,start,commands,closed=True):
        axis=24
        m=lambda p:(2*axis-p[0],p[1])
        nodes=[start]+[c[1] for c in commands]
        rev=[]
        for i,c in reversed(list(enumerate(commands))):
            k,end,*args=c
            if k=='C':rev.append((k,m(nodes[i]),m(args[1]),m(args[0])))
            elif k=='A':rev.append((k,m(nodes[i]),*args))
            else:rev.append((k,m(nodes[i])))
        self.path(n,start,commands+rev,closed)
