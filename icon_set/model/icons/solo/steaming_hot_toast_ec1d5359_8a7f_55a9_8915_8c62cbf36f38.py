"""Steaming Hot Toast Slice."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec1d5359-8a7f-55a9-8915-8c62cbf36f38'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/breakfast bread toast_ec1d5359-8a7f-55a9-8915-8c62cbf36f38.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-hot-toast'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('steaming', 'hot', 'toast')

    def build(self):
        # Plan: Plain toast with a broad rounded crown, straight sides and two steam curls. Mirrored bread profile with no added interior crust; no useful exact Lucide match.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('toast',(12,42),[('L',(36,42)),('A',(40,38),4,4,False),('L',(40,29)),('C',(42,24),(40,27),(42,27)),('C',(24,18),(42,18),(33,18)),('C',(6,24),(15,18),(6,18)),('C',(8,29),(6,27),(8,27)),('L',(8,38)),('A',(12,42),4,4,False)],True)
        for j,x in enumerate((18,30)):path('steam-'+str(j),(x,6),[('C',(x,10),(x-2,7),(x+2,9))])
