"""A real-estate handshake beneath a roof.
Plan: SQUARE separates the roof from a broad handshake and paired cuffs.
Reduction: Minor finger creases omitted; thumb and hand contours widened without removing the handshake.
Construction: Lucide handshake: joined wrists, thumb fold and broad finger mass; shared human reference guidance inspected.
Layout: Handshake anatomy is intentionally asymmetric beneath a symmetric roof; no detached head-body spacing applies."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '490f19a8-c170-4914-bea1-18cbfb479033'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate deal shake_490f19a8-c170-4914-bea1-18cbfb479033.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'real-estate-deal-shake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('real', 'estate', 'deal', 'shake')

    def build(self):
        self.add_polyline('roof',(6,20),(24,6),(42,20))
        self.add_polyline('cuff-left',(6,28),(14,28),(14,30),(14,38),(14,40),(6,40),closed=True)
        self.add_polyline('cuff-right',(34,28),(42,28),(42,40),(34,40),(34,38),(34,30),closed=True)
        self.add_line('left-hand-top-1',(14, 30),(17, 24))
        self.add_line('left-hand-top-2',(17, 24),(28, 24))
        self.add_bezier('right-hand-top',(34,28),((32,25),(30,24),(28,24)))
        self.add_line('thumb-1',(28, 24),(22, 32))
        self.add_bezier('thumb-return',(22,32),((24,35),(27,33),(28,32)))
        self.add_line('fingers-upper-1',(28, 32),(34, 38))
        self.add_bezier('fingers-bottom',(34,38),((34,40),(30,41),(28,40)),((28,42),(25,42),(24,42)),((21,42),(18,39),(14,38)))
        self.add_contour('handshake-outline','left-hand-top-1','left-hand-top-2','thumb-1','thumb-return','fingers-upper-1','fingers-bottom')
        self.relate('connect','handshake-outline','cuff-left')
        self.relate('connect','handshake-outline','cuff-right')
        self.relate('connect','right-hand-top','handshake-outline')
        self.relate('connect','right-hand-top','cuff-right')

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

