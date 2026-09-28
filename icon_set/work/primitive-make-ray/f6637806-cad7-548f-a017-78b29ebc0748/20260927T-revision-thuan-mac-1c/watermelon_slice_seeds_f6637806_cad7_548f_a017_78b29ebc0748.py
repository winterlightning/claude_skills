"""Sliced Watermelon with Seeds."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f6637806-cad7-548f-a017-78b29ebc0748'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__watermelon-slice-seeds/20260927T145855Z-thuan-mac-1/reference/watermelon_f6637806-cad7-548f-a017-78b29ebc0748.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'watermelon-slice-seeds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
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

        path('slice',(38,6),[('C',(42,24),(42,10),(42,18)),('C',(24,42),(42,34),(34,42)),('C',(6,38),(18,42),(10,42)),('L',(38,6))],True)
        for j,p in enumerate(((31,27),(23,33))):self.add_dot('seed-'+str(j),p)
