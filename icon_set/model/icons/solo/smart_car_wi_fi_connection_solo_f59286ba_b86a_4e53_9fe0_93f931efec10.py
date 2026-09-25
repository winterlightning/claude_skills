"""A frontal car under two wireless arcs, restoring the two wheel strokes. Bounds (6,6)-(42,42). Shared bilateral construction.
Construction reference: Lucide car-front: cabin/body stacking and short wheel strokes.
Omissions: Minor corner variations simplified."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f59286ba-b86a-4e53-9fe0-93f931efec10'
SOURCE_PATH = 'pictographic-primitives/other/car wifi_f59286ba-b86a-4e53-9fe0-93f931efec10.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='smart-car-wi-fi-connection-solo'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('car', 'wifi')
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
        path('signal-outer',(6,10),[('C',(24,6),(12,7),(18,6)),('C',(42,10),(30,6),(36,7))])
        path('signal-inner',(18,15),[('C',(30,15),(21,14),(27,14))])
        path('body',(10,31),[('L',(38,31)),('A',(42,35),4,4,True),('A',(38,39),4,4,True),('L',(10,39)),('A',(6,35),4,4,True),('A',(10,31),4,4,True)],True)
        poly('cabin',(12,31),(16,23),(32,23),(36,31));join('cabin','body')
        for x in (12,36):
         line('wheel-'+str(x),(x,39),(x,42));join('wheel-'+str(x),'body')
