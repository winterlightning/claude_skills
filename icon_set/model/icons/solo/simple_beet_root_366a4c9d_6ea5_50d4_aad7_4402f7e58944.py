"""Simple Beet Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '366a4c9d-6ea5-50d4-aad7-4402f7e58944'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/beet_366a4c9d-6ea5-50d4-aad7-4402f7e58944.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-beet-root'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('simple', 'beet', 'root')

    def build(self):
        # Plan: Broad diagonal beet with a pointed root and two cut stalks. Asymmetric body preserves the natural reference. Stalks reduced to paired strokes; no useful exact Lucide match.
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

        path('root',(6,42),[('C',(6,28),(9,36),(6,34)),('C',(24,14),(6,20),(14,14)),('C',(34,18),(28,14),(32,15)),('C',(38,28),(36,21),(38,24)),('C',(22,42),(38,37),(30,42)),('C',(6,42),(15,42),(12,38))],True)
        line('stalk-a',(34,18),(34,6));join('stalk-a','root')
        line('stalk-b',(34,18),(42,10));join('stalk-b','root');join('stalk-a','stalk-b')
