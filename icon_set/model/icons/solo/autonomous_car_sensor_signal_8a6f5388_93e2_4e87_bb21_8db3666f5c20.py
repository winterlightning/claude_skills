"""auto pilot car radius. Plan: mirrored car with equal circular wheels and four surrounding sensor arcs. SQUARE extremes (6,6)-(42,42). Lucide car-front informs roof/body simplification; source side-view wheels retained. Omit repeated inner sensor layer to free clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a6f5388-93e2-4e87-bb21-8db3666f5c20'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/auto pilot car radius_8a6f5388-93e2-4e87-bb21-8db3666f5c20.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'autonomous-car-sensor-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('auto', 'pilot', 'car', 'radius')
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
        # Four sensor quadrants share one radius; the redundant inner band is omitted.
        for ix in (0,1):
            for iy in (0,1):
                def p(x,y):return (48-x if ix else x,48-y if iy else y)
                self.add_arc(f'sensor-{ix}-{iy}',p(6,18),p(18,6),radius_x=12,sweep=(ix==iy))
        points=[(14,29),(14,25),(18,22),(20,18),(28,18),(30,22),(34,25),(34,29)]
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'body-{j}',a,b)
        self.add_arc('wheel-right',(34,29),(28,29),radius_x=3)
        self.add_line('chassis',(28,29),(20,29))
        self.add_arc('wheel-left',(20,29),(14,29),radius_x=3)
        self.add_contour('car','body-1','body-2','body-3','body-4','body-5','body-6','body-7','wheel-right','chassis','wheel-left',closed=True)
