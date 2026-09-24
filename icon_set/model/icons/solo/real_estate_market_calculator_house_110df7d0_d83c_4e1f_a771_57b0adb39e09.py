"""A four-operation calculator in front of a house.
Symbol plan: A two-by-two calculator grid contains plus, minus, multiply and equals; roof and wall sit behind it. Ink extremes (4,4)-(44,44).
Construction: calculator: grouped controls within one enclosure; house: roof and rear wall.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '110df7d0-d83c-4e1f-a771-57b0adb39e09'
SOURCE_PATH = 'icon_set/work/todo-references/real estate market calculator house_110df7d0-d83c-4e1f-a771-57b0adb39e09.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'real-estate-market-calculator-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('real', 'estate', 'market', 'calculator', 'house')

    def build(self):
        self.add_polyline('roof',(18,16),(30,6),(42,16))
        self.add_polyline('house-wall',(40,20),(40,28),(34,28))
        self.box('calculator',6,18,32,42,4)
        self.add_polyline('vertical-divider',(19,18),(19,30),(19,42))
        self.add_polyline('horizontal-divider',(6,30),(19,30),(32,30))
        for n in ('vertical-divider','horizontal-divider'):self.relate('connect',n,'calculator')
        self.relate('connect','vertical-divider','horizontal-divider')
        for n,a,b in [('plus-left',(10,24),(12,24)),('plus-right',(12,24),(14,24)),('plus-top',(12,22),(12,24)),('plus-bottom',(12,24),(12,26))]:self.add_line(n,a,b)
        parts=['plus-left','plus-right','plus-top','plus-bottom']
        for i,a in enumerate(parts):
            for b in parts[:i]:self.relate('connect',a,b)
        self.add_line('minus',(23,24),(27,24))
        self.add_polyline('multiply-a',(10,34),(12,36),(14,38))
        self.add_polyline('multiply-b',(10,38),(12,36),(14,34))
        self.relate('connect','multiply-a','multiply-b')
        for i,y in enumerate((34,38)):self.add_line(f'equals-{i}',(23,y),(27,y))

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

