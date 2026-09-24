"""A rounded outlined right arrow with semicircular shaft end and rounded diagonal wing ends. Bounds (6,6)-(42,42). Upper and lower wings mirror around y24.
Construction reference: Lucide arrow-big-right: single coherent outlined arrow; source rounded wings preserved.
Omissions: None."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b2073574-d0d3-43f8-97ff-2d6bdaf914e5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/caret right_b2073574-d0d3-43f8-97ff-2d6bdaf914e5.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='arrow-right-rounded-outline'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('caret', 'right')
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
        path('arrow',(10,20),[('L',(26,20)),('L',(19,13)),('C',(18,10),(18,12),(18,11)),('A',(22,6),4,4,True),('C',(25,7),(23,6),(24,6)),('L',(40,21)),('C',(42,24),(42,22),(42,23)),('C',(40,27),(42,25),(42,26)),('L',(25,41)),('C',(22,42),(24,42),(23,42)),('A',(18,38),4,4,True),('C',(19,35),(18,37),(18,36)),('L',(26,28)),('L',(10,28)),('A',(10,20),4,4,True)],True)
