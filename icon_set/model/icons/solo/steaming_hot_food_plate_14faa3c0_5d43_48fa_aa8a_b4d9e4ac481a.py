"""Steaming Hot Food Plate."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14faa3c0-5d43-48fa-aa8a-b4d9e4ac481a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pasta plate warm_14faa3c0-5d43-48fa-aa8a-b4d9e4ac481a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-hot-food-plate'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('steaming', 'hot', 'food', 'plate')

    def build(self):
        # Plan: Shallow dish of mounded food with three rising steam wisps. Mirrored bowl and generous repeated steam spacing. Lucide soup and cooking-pot inform the rim and bowl; smaller source food lobes simplified.
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

        path('dish',(6,31),[('L',(42,31)),('L',(37,39)),('C',(31,42),(36,41),(34,42)),('L',(17,42)),('C',(11,39),(14,42),(12,41)),('L',(6,31))],True)
        path('food',(6,31),[('C',(24,22),(6,25),(17,22)),('C',(42,31),(31,22),(42,25))]);join('food','dish')
        for j,x in enumerate((14,24,34)):path('steam-'+str(j),(x,6),[('C',(x,13),(x-3,8),(x+3,11))])
