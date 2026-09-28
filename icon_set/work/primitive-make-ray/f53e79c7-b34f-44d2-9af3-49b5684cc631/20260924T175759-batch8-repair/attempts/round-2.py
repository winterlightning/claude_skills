"""A house beneath a large central rating star and two smaller stars.
Symbol plan: Three five-point stars sit above a symmetric pitched-roof house. Ink extremes (4,4)-(44,44).
Construction: star: five-point outline; house: mirrored roof and doorway.
Human construction: Not applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f53e79c7-b34f-44d2-9af3-49b5684cc631'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate favorite house rating_f53e79c7-b34f-44d2-9af3-49b5684cc631.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'real-estate-favorite-house-rating'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('real', 'estate', 'favorite', 'house', 'rating')

    def build(self):
        # HRECT_L (4,8)-(44,40); one outlined rating star, two small sparkles,
        # and an open-bottom house. Door and minor closed star outlines omitted.
        self.add_polyline('main-star',(24,8),(27,14),(32,14),(28,18),(29,24),(24,20),(19,24),(20,18),(16,14),(21,14),closed=True)
        for x in (6,42):
            self.add_polyline(f'star-h-{x}',(x-2,14),(x,14),(x+2,14))
            self.add_polyline(f'star-v-{x}',(x,12),(x,14),(x,16))
            self.relate('connect',f'star-h-{x}',f'star-v-{x}')
        self.add_polyline('house',(14,40),(14,37),(24,32),(34,37),(34,40))

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

