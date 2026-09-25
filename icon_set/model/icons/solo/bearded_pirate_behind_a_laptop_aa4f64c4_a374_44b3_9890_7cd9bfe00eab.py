"""avatar piracy laptop. Plan: SQUARE extremes (6,6)-(42,42), bicorn hat above circular jaw with beard exposed beside laptop. Human reference user.svg informs circular jaw; Lucide laptop informs simple closed screen. No detached torso is drawn. Tiny hat cross omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aa4f64c4-a374-44b3-9890-7cd9bfe00eab'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/avatar piracy laptop_aa4f64c4-a374-44b3-9890-7cd9bfe00eab.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'bearded-pirate-behind-a-laptop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('avatar', 'piracy', 'laptop')
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
        # Broad bicorn hat, circular jaw and a beard partly hidden by the laptop.
        self.add_bezier('hat-crown',(14,18),((14,12),(18,12),(20,12)),((22,8),(25,6),(28,6)),((31,6),(34,8),(36,12)),((40,12),(42,14),(42,18)))
        self.add_polyline('hat-brim',(42,18),(38,18),(18,18),(14,18))
        self.relate('connect','hat-crown','hat-brim')
        self.path('jaw',(18,18),[((22,26),10,10,False),((34,26),10,10,False),((38,18),10,10,False)])
        self.relate('connect','jaw','hat-brim')
        self.add_polyline('laptop',(6,26),(22,26),(28,42),(12,42),closed=True)
        self.relate('connect','jaw','laptop')
        self.add_bezier('beard',(34,26),((40,30),(40,36),(34,42)),((32,42),(30,42),(28,42)))
        self.relate('connect','jaw','beard')
        self.relate('connect','laptop','beard')
