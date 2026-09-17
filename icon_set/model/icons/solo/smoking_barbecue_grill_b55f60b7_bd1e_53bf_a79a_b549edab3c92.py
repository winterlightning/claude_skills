"""Smoking Barbecue Grill."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b55f60b7-bd1e-53bf-a79a-b549edab3c92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/barbecue grill_b55f60b7-bd1e-53bf-a79a-b549edab3c92.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smoking-barbecue-grill'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('smoking', 'barbecue', 'grill')

    def build(self):
        # Plan: Barbecue bowl on two splayed legs with three rising smoke wisps. Shared leg nodes and repeated smoke definition. Crossbar omitted to preserve clearance below the bowl; Lucide soup informs the open bowl.
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

        path('bowl',(6,20),[('L',(42,20)),('C',(32,30),(42,24),(37,29)),('C',(24,32),(29,32),(27,32)),('C',(16,30),(21,32),(19,32)),('C',(6,20),(11,29),(6,24))],True)
        line('leg-left',(16,30),(10,42));line('leg-right',(32,30),(38,42));join('leg-left','bowl');join('leg-right','bowl')
        for j,x in enumerate((14,24,34)):path('smoke-'+str(j),(x,6),[('C',(x,12),(x-2,8),(x+2,10))])
