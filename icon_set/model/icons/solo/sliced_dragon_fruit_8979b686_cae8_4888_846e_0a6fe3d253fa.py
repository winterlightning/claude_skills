"""Sliced Dragon Fruit."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8979b686-cae8-4888-846e-0a6fe3d253fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/dragon fruit slice_8979b686-cae8-4888-846e-0a6fe3d253fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sliced-dragon-fruit'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('sliced', 'dragon', 'fruit')

    def build(self):
        # Plan: Rounded cut fruit with three broad crown scales and three separated seed dots. Reduced scale count and omitted inner rim preserve the defining crown and seeded flesh without narrow gaps.
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

        path('fruit',(6,24),[('L',(6,10)),('L',(18,18)),('L',(24,6)),('L',(30,18)),('L',(42,10)),('L',(42,28)),('C',(24,42),(42,36),(34,42)),('C',(6,24),(14,42),(6,35))],True)
        for j,p in enumerate(((20,26),(28,26),(24,33))):self.add_dot('seed-'+str(j),p)
