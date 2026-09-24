"""A smiling boy with side-swept hair, round cheek/jaw, and two ears. Envelope (6,6)-(42,42). Facial dots share y24; smile is centered. Human user reference informs circular face, no body is present.
Construction reference: icon_set/references/human_ref/user.svg: rounded face vocabulary; no useful exact Lucide portrait match.
Omissions: Tiny ear interior omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0673820c-38b2-4d6f-9b2a-49663f3a128f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/kids/boy head_0673820c-38b2-4d6f-9b2a-49663f3a128f.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='smiling-boy-face'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="kids"
    aliases=()
    keywords=('boy', 'head')
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
        path('head',(10,24),[('L',(10,16)),('C',(12,12),(10,14),(11,13)),('C',(24,6),(15,6),(21,6)),('C',(36,12),(31,6),(36,7)),('L',(38,18)),('L',(38,24)),('A',(42,28),4,4,True),('A',(38,32),4,4,True),('C',(24,42),(36,38),(30,42)),('C',(10,32),(18,42),(12,38)),('A',(6,28),4,4,True),('A',(10,24),4,4,True)],True)
        path('hair',(10,16),[('C',(27,10),(17,16),(23,15)),('C',(38,18),(29,15),(33,18))]);join('hair','head')
        for x in (19,29): self.add_dot('eye-'+str(x),(x,25))
        path('smile',(21,33),[('C',(27,33),(23,34),(25,34))])
