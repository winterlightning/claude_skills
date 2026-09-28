"""Street Food Stall with Stools."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cfc6e31-cca6-4892-bfd9-394a469977b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/kiosk_1cfc6e31-cca6-4892-bfd9-394a469977b1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'street-food-stall-stools'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('street', 'food', 'stall', 'stools')

    def build(self):
        # Plan: Street stall with three scalloped awning panels, open counter and two stools. Lucide store informs the repeated canopy. Countertop props and stool crossbars omitted; each stool is a single connected seat-and-leg contour.
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

        path('awning',(6,6),[('L',(18,6)),('L',(30,6)),('L',(42,6)),('L',(42,12)),('A',(30,12),6,6,True),('A',(18,12),6,6,True),('A',(6,12),6,6,True),('L',(6,6))],True)
        for j,x in enumerate((18,30)):line('panel-'+str(j),(x,6),(x,12));join('panel-'+str(j),'awning')
        for j,x in enumerate((6,42)):line('post-'+str(j),(x,12),(x,28));join('post-'+str(j),'awning')
        line('counter',(6,28),(42,28));join('counter','post-0');join('counter','post-1')
        for j,x in enumerate((14,34)):
         line('seat-'+str(j),(x-4,36),(x+4,36))
         poly('legs-'+str(j),(x-5,42),(x-4,36),(x+4,36),(x+5,42))
