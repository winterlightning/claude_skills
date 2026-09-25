"""bike parking 2. Plan: HRECT_L extremes (4,8)-(44,40); shared radius-eight wheels, open V-frame, saddle and angled handlebar. Frame attaches at top cardinal wheel points. Lower duplicate frame tube omitted to enlarge openings; Lucide bike informs shared radii."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7eea5c25-9b41-4dec-ba5e-91b557120a37'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bike parking 2_7eea5c25-9b41-4dec-ba5e-91b557120a37.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'angled-handlebar-road-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('bike', 'parking', '2')
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
        for x in (12,36):
            self.path(f'wheel-{x}',(x,24),[((x+8,32),8,8,True),((x,40),8,8,True),((x-8,32),8,8,True),((x,24),8,8,True)],True)
        self.add_polyline('frame',(12,24),(12,12),(24,20),(36,12),(36,24))
        self.add_polyline('seat',(8,12),(12,12),(16,12))
        self.add_polyline('handlebar',(36,12),(32,8),(40,8))
        for a,b in [('frame','wheel-12'),('frame','wheel-36'),('frame','seat'),('frame','handlebar')]:self.relate('connect',a,b)
