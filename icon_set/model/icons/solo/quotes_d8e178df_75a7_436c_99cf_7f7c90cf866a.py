"""A pair of broad closing quotation marks.
Symbol plan: Two equal block-and-tail contours occupy a shorter horizontal keyshape. Ink extremes (2,8)-(46,40).
Construction: quote: rounded block and coherent closing tail, re-authored as a broad shorter form.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd8e178df-75a7-436c-99cf-7f7c90cf866a'
SOURCE_PATH = 'icon_set/work/todo-references/quotes_d8e178df-75a7-436c-99cf-7f7c90cf866a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'quotes'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('quotes',)

    def build(self):
        for i,x in enumerate((4,29)):
            n=f'quote-{i}'
            self.add_line(n+'-top',(x+4,10),(x+11,10))
            self.add_arc(n+'-tr',(x+11,10),(x+15,14),radius_x=4)
            self.add_line(n+'-right',(x+15,14),(x+15,24))
            self.add_bezier(n+'-outer-tail',(x+15,24),((x+15,31),(x+9,38),(x+4,38)))
            self.add_line(n+'-tail-end',(x+4,38),(x+4,30))
            self.add_bezier(n+'-inner-tail',(x+4,30),((x+8,30),(x+9,27),(x+9,24)))
            self.add_line(n+'-shelf',(x+9,24),(x+4,24))
            self.add_arc(n+'-bl',(x+4,24),(x,20),radius_x=4)
            self.add_line(n+'-left',(x,20),(x,14))
            self.add_arc(n+'-tl',(x,14),(x+4,10),radius_x=4)
            self.add_contour(n,*[n+s for s in ('-top','-tr','-right','-outer-tail','-tail-end','-inner-tail','-shelf','-bl','-left','-tl')],closed=True)

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

