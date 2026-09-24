"""A rating booklet with a prominent star.
Plan: VRECT_L leaves vertical room for the rear page and front cover.
Reduction: Omitted tiny writing lines; squared the rear-page edge in place of the crowded shallow diagonal.
Construction: Lucide file-text and star: simple page silhouette and a centered five-point symbol.
Layout: Star and cover are centered; rear-page offset intentionally indicates multiple pages."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd9776d01-07f9-402d-ac77-fc73a405a509'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/rating booklet_d9776d01-07f9-402d-ac77-fc73a405a509.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'rating-booklet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rating', 'booklet')

    def build(self):
        self.add_polyline('cover',(8,12),(36,12),(40,12),(40,44),(8,44),closed=True)
        self.add_polyline('rear-leaf',(16,4),(36,4),(36,12))
        self.relate('connect','rear-leaf','cover')
        self.add_polyline('rating-star',(24,20),(27,26),(32,26),(28,30),(29,36),(24,32),(19,36),(20,30),(16,26),(21,26),closed=True)

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

