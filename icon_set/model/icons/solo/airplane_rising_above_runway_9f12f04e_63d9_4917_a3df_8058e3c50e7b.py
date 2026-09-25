"""An airplane rising diagonally above a horizontal runway, retaining both wings and a rounded nose. Bounds (4,8)-(44,40).
Construction reference: Lucide plane-takeoff: unified ascending silhouette and detached runway.
Omissions: None."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9f12f04e-63d9-4917-a3df-8058e3c50e7b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plane arrival_9f12f04e-63d9-4917-a3df-8058e3c50e7b.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='airplane-rising-above-runway'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('plane', 'arrival')
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
        path('plane',(4,21),[('L',(8,19)),('L',(13,22)),('L',(21,18)),('L',(12,9)),('L',(16,8)),('L',(28,15)),('L',(36,11)),('C',(44,14),(40,10),(44,10)),('C',(41,18),(44,16),(43,17)),('L',(31,24)),('L',(27,31)),('L',(23,32)),('L',(23,26)),('L',(15,31)),('C',(9,29),(12,32),(10,31)),('L',(4,21))],True)
        line('runway',(4,40),(44,40))
