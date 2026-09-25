"""Spiky Tropical Rambutan Fruit."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1385615e-fc30-5904-86f0-2450b55f4622'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/rambutan_1385615e-fc30-5904-86f0-2450b55f4622.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spiky-rambutan-fruit'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('spiky', 'rambutan', 'fruit')

    def build(self):
        # Plan: Round rambutan with eight short radiating hairs and two curved surface marks. Shared circular attachment nodes and repeated radial hairs; four interior marks reduced to two. No useful exact Lucide match.
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

        pts=[(24,10),(34,14),(38,24),(34,34),(24,38),(14,34),(10,24),(14,14)]
        path('fruit',pts[0],[('A',p,14,14,True) for p in pts[1:]+pts[:1]],True)
        ends=[(24,6),(39,9),(42,24),(39,39),(24,42),(9,39),(6,24),(9,9)]
        for j,(p,q) in enumerate(zip(pts,ends)):line('hair-'+str(j),p,q);join('hair-'+str(j),'fruit')
        path('mark-left',(20,21),[('C',(20,27),(19,22),(19,26))])
        path('mark-right',(28,21),[('C',(28,27),(29,22),(29,26))])
