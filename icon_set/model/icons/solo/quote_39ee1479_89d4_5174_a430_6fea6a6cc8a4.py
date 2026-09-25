"""A pair of thin opening quotation marks with circular bowls.
Symbol plan: Two radius7 bowls and long quarter-ellipse tails share a 26-unit pitch. Ink extremes (2,8)-(46,40).
Construction: quote: repeated marks and curved tails; the input owns the circular bowl variant.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '39ee1479-89d4-5174-a430-6fea6a6cc8a4'
SOURCE_PATH = 'icon_set/work/todo-references/quote_39ee1479-89d4-5174-a430-6fea6a6cc8a4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'quote'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('quote',)

    def build(self):
        for i,x in enumerate((4,30)):
            self.circle(f'bowl-{i}',x+7,31,7)
            self.add_arc(f'tail-{i}',(x,31),(x+14,10),radius_x=14,radius_y=21)
            self.relate('connect',f'bowl-{i}',f'tail-{i}')

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

