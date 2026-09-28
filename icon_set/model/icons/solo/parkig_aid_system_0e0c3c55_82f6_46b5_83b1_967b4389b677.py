"""A parking P emitting a sensor wave toward a triangular obstacle.
Plan: SQUARE preserves the upper-left P and lower-right obstacle.
Reduction: Reduced two sensor waves to one and moved it slightly right.
Construction: Lucide-style parking letter loop and radio-wave construction, guided by the source.
Layout: Intentional upper-left to lower-right sensing arrangement remains clear."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0e0c3c55-82f6-46b5-83b1-967b4389b677'
SOURCE_PATH = 'pictographic-primitives/transportation/parkig aid system_0e0c3c55-82f6-46b5-83b1-967b4389b677.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'parkig-aid-system'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('parkig', 'aid', 'system')

    def build(self):
        self.parking_letter('p',6,6,24,12,12)
        self.add_bezier('wave-inner',(27,12),((27,18),(25,23),(21,26)))
        self.add_polyline('obstacle',(34,26),(42,42),(26,42),closed=True)
        self.add_line('ground',(24,42),(26,42))
        self.relate('connect','ground','obstacle')

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def box(self, name, x, y, right, bottom, r=4):
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if a==b: continue
            n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def parking_letter(self,name,x,top,bottom,width=10,bowl_height=14):
        # Vertical stem split at the bowl attachment; one smooth half-ellipse owns its loop.
        mid=top+bowl_height; shoulder=x+3
        self.add_line(name+'-stem-upper',(x,mid),(x,top))
        self.add_line(name+'-top',(x,top),(shoulder,top))
        self.add_arc(name+'-bowl',(shoulder,top),(shoulder,mid),radius_x=width-3,radius_y=bowl_height//2)
        self.add_line(name+'-return',(shoulder,mid),(x,mid))
        self.add_contour(name+'-loop',name+'-stem-upper',name+'-top',name+'-bowl',name+'-return',closed=True)
        self.add_line(name+'-stem-lower',(x,mid),(x,bottom))
        self.relate('connect',name+'-loop',name+'-stem-lower')

    def plus(self,x,y,r=2):
        names=[]
        for i,p in enumerate(((x-r,y),(x+r,y),(x,y-4),(x,y+4))):
            n=f'plus-{i}';self.add_line(n,p,(x,y))
            for prev in names:self.relate('connect',n,prev)
            names.append(n)

