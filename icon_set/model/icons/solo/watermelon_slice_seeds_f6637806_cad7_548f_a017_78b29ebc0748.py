"""Sliced Watermelon with Seeds."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6637806-cad7-548f-a017-78b29ebc0748'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/watermelon_f6637806-cad7-548f-a017-78b29ebc0748.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'watermelon-slice-seeds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('watermelon', 'slice', 'seeds')

    def build(self):
        # Plan: Quarter-sector watermelon slice with two seed dots. Omit the secondary rind stripe to preserve open flesh at 48 pixels; the sector silhouette and seeds carry recognition.
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

        path('slice',(6,6),[('L',(33,6)),('L',(42,6)),('A',(6,42),36,36,True),('L',(6,33)),('L',(6,6))],True)
        for j,p in enumerate(((15,15),(24,18))):self.add_dot('seed-'+str(j),p)
