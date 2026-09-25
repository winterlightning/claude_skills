"""A house with a large rating star and two smaller sparkles.
Plan: VRECT_L fits a full closed house below the rating group.
Reduction: Omitted doorway; replaced the tiny outlined side stars with two-stroke sparkles.
Construction: Lucide house and star: recognizable closed house silhouette and centered five-point main star.
Layout: Main star and house share x24; smaller sparkles form a mirrored pair. House enlarged after native-size review."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f53e79c7-b34f-44d2-9af3-49b5684cc631'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate favorite house rating_f53e79c7-b34f-44d2-9af3-49b5684cc631.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'real-estate-favorite-house-rating'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('real', 'estate', 'favorite', 'house', 'rating')

    def build(self):
        # VRECT_L (8,4)-(40,44); full house, one rating star and two sparkles.
        self.add_polyline('main-star',(24,4),(27,10),(32,10),(28,14),(29,20),(24,16),(19,20),(20,14),(16,10),(21,10),closed=True)
        for x in (10,38):
            self.add_polyline(f'star-h-{x}',(x-2,24),(x,24),(x+2,24))
            self.add_polyline(f'star-v-{x}',(x,22),(x,24),(x,26))
            self.relate('connect',f'star-h-{x}',f'star-v-{x}')
        self.add_polyline('house',(8,36),(24,28),(40,36),(40,44),(8,44),closed=True)

    def circle(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-upper',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-lower',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-upper',name+'-lower',closed=True)

    def box(self,name,x,y,right,bottom,r=4):
        pts=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r)]
        members=[]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if a==b:continue
            n=f'{name}-{i}'
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def opening_quote(self,name,x,closing=False):
        # A shared 15-unit body and 25-unit pitch own both repeated quotation marks.
        def p(v):
            a,b=v
            return (x+15-a,48-b) if closing else (x+a,b)
        def line(n,a,b):self.add_line(name+n,p(a),p(b))
        def arc(n,a,b):self.add_arc(name+n,p(a),p(b),radius_x=4)
        def bez(n,a,*segs):self.add_bezier(name+n,p(a),*[(p(a),p(b),p(c)) for a,b,c in segs])
        bez('-outer',(0,24),((0,16),(5,8),(11,8)))
        arc('-crown',(11,8),(15,12))
        arc('-return',(15,12),(11,16))
        bez('-inner',(11,16),((7,16),(7,20),(7,24)))
        line('-shelf',(7,24),(11,24))
        arc('-tr',(11,24),(15,28))
        line('-right',(15,28),(15,36))
        arc('-br',(15,36),(11,40))
        line('-bottom',(11,40),(4,40))
        arc('-bl',(4,40),(0,36))
        line('-left',(0,36),(0,24))
        self.add_contour(name,*[name+n for n in ('-outer','-crown','-return','-inner','-shelf','-tr','-right','-br','-bottom','-bl','-left')],closed=True)

