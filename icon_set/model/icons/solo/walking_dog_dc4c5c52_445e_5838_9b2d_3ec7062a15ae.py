"""A dog walking right with a drooping ear, raised tail and staggered paws. Bounds (4,8)-(44,40). Rounded neck and back preserve the source pose.
Construction reference: Lucide dog: smooth hanging ear and organic contour; source owns full walking pose.
Omissions: Far legs simplified to avoid a crowded underbody."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dc4c5c52-445e-5838-9b2d-3ec7062a15ae'
SOURCE_PATH = 'pictographic-primitives/pets/dog walk_dc4c5c52-445e-5838-9b2d-3ec7062a15ae.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='walking-dog'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "pets"
    aliases=()
    keywords=('dog', 'walk')
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
        path('dog',(10,40),[('L',(8,30)),('C',(10,22),(11,28),(10,25)),('A',(16,16),6,6,True),('L',(29,16)),('C',(35,8),(29,10),(31,8)),('C',(40,12),(38,8),(39,11)),('L',(44,13)),('C',(38,21),(44,19),(41,21)),('L',(36,30)),('L',(35,40)),('L',(42,40))])
        path('belly',(35,40),[('L',(28,40)),('L',(28,28)),('L',(18,27)),('C',(16,32),(18,29),(18,31)),('L',(18,40)),('L',(10,40))]);join('belly','dog')
        path('tail',(10,22),[('C',(4,8),(5,17),(4,14))]);join('tail','dog')
        path('raised-paw',(36,30),[('C',(44,33),(40,28),(44,29))]);join('raised-paw','dog')
        path('ear',(35,8),[('L',(34,17)),('C',(29,20),(34,20),(31,21))]);join('ear','dog')
