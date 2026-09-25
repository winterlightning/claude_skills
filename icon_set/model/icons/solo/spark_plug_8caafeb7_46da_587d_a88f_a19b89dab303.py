"""An upright spark plug with axial terminal, rounded insulator, broad collar, threaded shank and hook electrode. Bounds (10,4)-(38,44).
Construction reference: Lucide plug: shared axial construction and rounded joints.
Omissions: Tiny thread striations omitted; terminal simplified to one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8caafeb7-46da-587d-a88f-a19b89dab303'
SOURCE_PATH = 'pictographic-primitives/transportation/car tool spark plug_8caafeb7-46da-587d-a88f-a19b89dab303.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='spark-plug'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "transportation"
    aliases=()
    keywords=('car', 'tool', 'spark', 'plug')
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
        path('insulator',(16,20),[('L',(16,14)),('A',(20,10),4,4,True),('L',(28,10)),('A',(32,14),4,4,True),('L',(32,20))])
        path('collar',(14,20),[('L',(16,20)),('L',(32,20)),('L',(34,20)),('A',(38,24),4,4,True),('A',(34,28),4,4,True),('L',(30,28)),('L',(18,28)),('L',(14,28)),('A',(10,24),4,4,True),('A',(14,20),4,4,True)],True);join('collar','insulator')
        line('terminal',(24,4),(24,10));join('terminal','insulator')
        poly('shank',(18,28),(18,36),(30,36),(30,28));join('shank','collar')
        path('electrode',(26,36),[('L',(26,41)),('A',(29,44),3,3,False),('L',(32,44))]);join('electrode','shank')
