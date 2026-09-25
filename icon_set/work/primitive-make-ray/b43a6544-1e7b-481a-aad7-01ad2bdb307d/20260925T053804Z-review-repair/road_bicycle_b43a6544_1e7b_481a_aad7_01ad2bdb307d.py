"""Fresh reference repair. Construction reference: Lucide bike (wheel construction only).
Keyshape HRECT_L; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b43a6544-1e7b-481a-aad7-01ad2bdb307d'
SOURCE_PATH = 'pictographic-primitives/transportation/bicycle_b43a6544-1e7b-481a-aad7-01ad2bdb307d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'road-bicycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('bicycle',)

    def path(self,n,start,*steps,closed=False):
        here=start; ids=[]
        for i,step in enumerate(steps):
            kind,end,*v=step; name=f'{n}-{i}';ids.append(name)
            if kind=='L':self.add_line(name,here,end)
            elif kind=='A':self.add_arc(name,here,end,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C':self.add_bezier(name,here,(v[0],v[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)

    def build(self):
        # Diamond frame with sufficient open triangles; two matched wheels and a hooked racing bar.
        for n,x in [('rear',10),('front',38)]:self.circle(n,x,34,6)
        self.add_polyline('rear-stay',(10,28),(18,16),(24,28),(10,28))
        self.add_polyline('front-frame',(18,16),(32,16),(24,28))
        self.add_polyline('fork',(38,28),(32,16),(30,8),(38,8))
        self.path('bar',(38,8),('A',(42,12),4,4,True),('L',(42,14)))
        self.add_line('seatpost',(18,16),(16,8))
        self.add_polyline('seat',(12,8),(16,8),(20,8))
        for a,b in [('rear','rear-stay'),('front','fork'),('rear-stay','front-frame'),('rear-stay','seatpost'),('front-frame','fork'),('seatpost','seat'),('fork','bar')]:self.relate('connect',a,b)
