"""An envelope connected through a branch to three circular recipients. Bounds (6,6)-(42,42); repeated node radius3 and center step15.
Construction reference: Lucide mail and network: rounded envelope and symmetric branching nodes.
Omissions: None."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ee05c5e-5262-4581-b325-c0ad9f515a32'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon simple email service_9ee05c5e-5262-4581-b325-c0ad9f515a32.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='amazon-simple-email-service'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('amazon', 'simple', 'email', 'service')
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
        path('envelope',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,20)),('A',(38,24),4,4,True),('L',(24,24)),('L',(10,24)),('A',(6,20),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        path('flap',(6,10),[('L',(22,16)),('C',(26,16),(23,17),(25,17)),('L',(42,10))]);join('flap','envelope')
        line('stem',(24,24),(24,32));join('stem','envelope')
        path('branch',(9,36),[('L',(9,35)),('A',(12,32),3,3,True),('L',(24,32)),('L',(36,32)),('A',(39,35),3,3,True),('L',(39,36))]);join('branch','stem')
        line('center-link',(24,32),(24,36));join('center-link','stem');join('center-link','branch')
        for x in (9,24,39):
         path('node-'+str(x),(x,36),[('A',(x,42),3,3,True),('A',(x,36),3,3,True)],True)
         join('node-'+str(x),'center-link' if x==24 else 'branch')
