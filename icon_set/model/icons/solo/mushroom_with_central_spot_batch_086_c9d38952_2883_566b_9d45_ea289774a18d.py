"""mushroom-with-central-spot: independent batch-086 SOLO48 result.
Plan: Domed cap and rounded stem are one outline. One central circular spot and two eye dots retain power-up identity.
Reference construction: none.
Reduction: Removed the cap-to-stem interior seam to give the eyes space; kept the central round spot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9d38952-2883-566b-9d45-ea289774a18d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/mario mushroom_c9d38952-2883-566b-9d45-ea289774a18d.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/mario mushroom_c9d38952-2883-566b-9d45-ea289774a18d.svg'

class Drawing(Solo48):
    icon_id = 'mushroom-with-central-spot-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('mushroom', 'with', 'central', 'spot')

    def build(self):
        # Exact envelope comes from Keyshape.SQUARE.bounds_for(self.profile).

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{j}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)


        path('mushroom',(10,29),[('C',(6,24),(7,29),(6,27)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(38,29),(42,27),(41,29)),('L',(38,34)),('A',(30,42),8,8,True),('L',(18,42)),('A',(10,34),8,8,True),('L',(10,29))],True)
        oval('spot',24,18,3,3)
        for x in (20,28):dot(f'eye-{x}',(x,32))
