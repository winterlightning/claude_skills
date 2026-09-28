"""Steaming Hot Soup Ladle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae656065-eaa1-5e15-ad9c-f7c5ef8dbe2b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/ladle hot_ae656065-eaa1-5e15-ad9c-f7c5ef8dbe2b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-hot-soup-ladle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('steaming', 'hot', 'soup', 'ladle')

    def build(self):
        # Plan: Deep ladle at lower left with a hooked sloping handle and two steam trails. Lucide soup informs the curved bowl. Three source trails reduced to two to preserve separation from the handle; directional asymmetry retained.
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

        path('bowl',(6,30),[('L',(28,30)),('A',(6,30),11,12,True)],True)
        path('handle',(28,30),[('L',(32,12)),('C',(42,12),(34,4),(42,4))]);join('handle','bowl')
        for j,x in enumerate((10,20)):path('steam-'+str(j),(x,10),[('C',(x,20),(x-3,13),(x+3,17))])
