"""Steaming Traditional Hotpot."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6da20e17-a48a-5a6e-a021-affa5f56ce8d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hotpot shabushabu_6da20e17-a48a-5a6e-a021-affa5f56ce8d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-traditional-hotpot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('steaming', 'traditional', 'hotpot')

    def build(self):
        # Plan: Traditional hotpot with a tall central chimney, round bowl, raised foot and paired steam trails. Mirrored chimney and shared bowl junctions. Elliptical top and extra rim reduced to single edges; no useful exact Lucide match.
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

        path('bowl',(6,26),[('L',(16,26)),('L',(32,26)),('L',(42,26)),('C',(30,34),(42,32),(36,34)),('L',(18,34)),('C',(6,26),(12,34),(6,32))],True)
        poly('chimney',(16,26),(18,10),(30,10),(32,26));join('chimney','bowl')
        poly('foot',(18,34),(16,42),(32,42),(30,34));join('foot','bowl')
        for j,x in enumerate((8,40)):path('steam-'+str(j),(x,6),[('C',(x,15),(x+2,9),(x-2,12))])
