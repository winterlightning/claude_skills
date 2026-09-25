"""The OpenID logo with loop, upright stem and right arrow.
Plan: SQUARE fits the loop left, tall stem and right-pointing arrow.
Reduction: Replaced the narrow outlined arrow with a clear shaft and chevron; widened the D-like loop band.
Construction: No useful exact Lucide logo match used; supplied reference governs the arrangement.
Layout: Intentional right-facing asymmetry; shared attachment nodes retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '962c33a0-eaf5-4a99-9127-a5fd1da5870b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/protocol open id logo_962c33a0-eaf5-4a99-9127-a5fd1da5870b.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'protocol-open-id-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('protocol', 'open', 'id', 'logo')

    def build(self):
        # SQUARE (6,6)-(42,42); widened outlined D and compact right arrow.
        self.add_polyline('stem',(23,16),(23,10),(31,6),(31,20),(31,38),(23,42),(23,33),(23,25),(23,16))
        self.add_bezier('outer-loop',(23,16),((12,16),(6,22),(6,29)),((6,37),(13,42),(23,42)))
        self.add_bezier('inner-loop',(23,25),((18,25),(15,26),(15,29)),((15,32),(18,33),(23,33)))
        self.relate('connect','stem','outer-loop');self.relate('connect','inner-loop','stem')
        self.add_line('arrow-shaft',(31,20),(42,20))
        self.add_polyline('arrow-head',(36,14),(42,20),(36,26))
        self.relate('connect','arrow-shaft','stem');self.relate('connect','arrow-shaft','arrow-head')

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

