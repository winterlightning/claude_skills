"""Simple Carrot Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '193a2827-9fbf-5df7-b701-3488c645fb91'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/carrot_193a2827-9fbf-5df7-b701-3488c645fb91.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-carrot-root'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('simple', 'carrot', 'root')

    def build(self):
        # Plan: Diagonal carrot with a long tapered root, two leaves and one side cut. Lucide carrot informs the coherent taper and attached notch. Rotated from the upright reference to preserve carrot proportions on SOLO48; small repeated cuts omitted.
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

        path('root',(6,42),[('C',(16,20),(8,34),(12,24)),('C',(30,16),(21,15),(26,12)),('C',(34,29),(35,20),(38,24)),('C',(6,42),(25,36),(12,41))],True)
        line('leaf-a',(30,16),(30,6));line('leaf-b',(30,16),(42,10))
        join('leaf-a','root');join('leaf-b','root');join('leaf-a','leaf-b')
        line('cut',(16,20),(22,26));join('cut','root')
