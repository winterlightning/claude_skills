"""caviar. Plan: SQUARE extremes (6,6)-(42,42); six identical radius-three circles in centered one-two-three rows. Shared circle construction follows local Lucide circle. Eggs separated by at least nine centerline units; circular openings use the existing diameter-six circle rule. None omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e625a592-a7be-4a88-9cc8-1a1640f52612'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/caviar_e625a592-a7be-4a88-9cc8-1a1640f52612.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'pyramid-of-round-caviar-eggs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('caviar',)
    def path(self,n,start,steps,closed=False):
        here=start;members=[]
        for k,step in enumerate(steps):
            ident=f'{n}-{k}';members.append(ident)
            if len(step)==2:
                self.add_line(ident,here,step);here=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep);here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,q=0):
        if q==0:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        else:self.path(n,(l+q,t),[(r-q,t),((r,t+q),q,q,True),(r,b-q),((r-q,b),q,q,True),(l+q,b),((l,b-q),q,q,True),(l,t+q),((l+q,t),q,q,True)],True)
    def build(self):
        # Shared circular egg definition and three centered rows preserve the 1-2-3 count.
        rows=((9,(24,)),(24,(16,32)),(39,(9,24,39)))
        for row,(y,xs) in enumerate(rows):
            for col,x in enumerate(xs):self.circle(f'egg-{row}-{col}',x,y,3)
