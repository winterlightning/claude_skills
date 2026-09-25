"""Three increasing building columns beneath an upward market arrow.
Symbol plan: Three equal-width bars share a baseline and rise at equal height steps; arrow points up-right. Ink extremes (2,6)-(46,42).
Construction: chart-no-axes-column-increasing: equal-pitch rising series; supplied reference adds outlined columns and trend arrow.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4cb4eabd-1bfb-46c2-ab15-0b351ab22677'
SOURCE_PATH = 'icon_set/work/todo-references/real estate market building increase_4cb4eabd-1bfb-46c2-ab15-0b351ab22677.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'real-estate-market-building-increase'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('real', 'estate', 'market', 'building', 'increase')

    def build(self):
        self.add_polyline('baseline',(4,40),(12,40),(20,40),(28,40),(36,40),(44,40))
        for i,(x,y) in enumerate(((4,28),(20,20),(36,12))):
            self.add_polyline(f'building-{i}',(x,40),(x,y),(x+8,y),(x+8,40))
            self.relate('connect',f'building-{i}','baseline')
        self.add_line('trend',(6,18),(24,8))
        self.add_polyline('arrow-head',(18,8),(24,8),(24,12))
        self.relate('connect','trend','arrow-head')

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

