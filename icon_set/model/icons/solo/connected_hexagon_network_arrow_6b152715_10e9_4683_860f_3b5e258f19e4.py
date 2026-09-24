"""elemental mediaconnect 1. Plan: SQUARE extremes (6,6)-(42,42); three hexagon nodes arranged symmetrically, upper branches, downward arrow and lower V-link. All source groups retained; lower boundary truly joins side nodes. Lucide network informs shared endpoint branches and repeated node shapes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6b152715-10e9-4683-860f-3b5e258f19e4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/elemental mediaconnect 1_6b152715-10e9-4683-860f-3b5e258f19e4.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'connected-hexagon-network-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('elemental', 'mediaconnect', '1')
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
        self.add_polyline('top-node',(24,6),(30,9),(30,12),(30,15),(24,18),(18,15),(18,12),(18,9),closed=True)
        for name,x in [('left-node',10),('right-node',38)]:
            self.add_polyline(name,(x,22),(x+4,25),(x+4,29),(x,32),(x-4,29),(x-4,25),closed=True)
        self.add_line('link-left',(18,12),(6,12))
        self.add_line('link-right',(30,12),(42,12))
        self.relate('connect','top-node','link-left')
        self.relate('connect','top-node','link-right')
        self.add_polyline('lower-link',(10,32),(24,42),(38,32))
        for n in ('left-node','right-node'):self.relate('connect',n,'lower-link')
        self.add_line('arrow',(24,26),(24,32))
        self.add_polyline('arrow-head',(22,30),(24,32),(26,30))
        self.relate('connect','arrow','arrow-head')
