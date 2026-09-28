"""A calculator in front of a house.
Plan: SQUARE preserves foreground calculator and upper-right house overlap.
Reduction: Replaced plus/minus/multiply/equals labels and quadrant dividers with a display and two keys.
Construction: Lucide house and calculator: roof outline, display bar and sparse key row.
Layout: Calculator intentionally occludes the lower-left part of the house; true attachment endpoints are shared."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '110df7d0-d83c-4e1f-a771-57b0adb39e09'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate market calculator house_110df7d0-d83c-4e1f-a771-57b0adb39e09.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'real-estate-market-calculator-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('real', 'estate', 'market', 'calculator', 'house')

    def build(self):
        # SQUARE (6,6)-(42,42); calculator occludes the house lower-left.
        # Keep a display and two keys; omit crowded operator labels and dividers.
        self.add_polyline('roof',(18,18),(30,6),(42,18))
        self.add_polyline('house-wall',(42,18),(42,30),(30,30))
        self.add_polyline('calculator',(6,18),(18,18),(30,18),(30,30),(30,42),(6,42),closed=True)
        self.relate('connect','roof','house-wall')
        self.relate('connect','roof','calculator');self.relate('connect','house-wall','calculator')
        self.add_line('display',(14,26),(22,26))
        for x in (14,22):self.add_dot(f'key-{x}',(x,34))

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

