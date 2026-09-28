"""An envelope in a targeting reticle.
Repair plan: Open envelope top; mirrored U outline and shallow flap preserve the mail shape without the tiny upper triangle.
Omissions: Top horizontal envelope edge.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ea274b51-b095-451d-addb-e6a29ef9d9da'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/read email target_ea274b51-b095-451d-addb-e6a29ef9d9da.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'read-email-target'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('read', 'email', 'target')

    def build(self):
        # Cardinal arcs use mirrored cubic control hulls, with exact extrema at6 and42.
        c=17/3
        self.add_bezier('ring-top',(18,7),((22,c),(26,c),(30,7)))
        self.add_bezier('ring-bottom',(30,41),((26,48-c),(22,48-c),(18,41)))
        self.add_bezier('ring-left',(7,30),((c,26),(c,22),(7,18)))
        self.add_bezier('ring-right',(41,18),((48-c,22),(48-c,26),(41,30)))
        for i,(a,b) in enumerate((((6,6),(10,10)),((42,6),(38,10)),((6,42),(10,38)),((42,42),(38,38)))):self.add_line(f'target-tick-{i}',a,b)
        self.add_polyline('envelope',(16,17),(16,31),(32,31),(32,17))
        self.add_polyline('flap',(16,17),(24,22),(32,17))
        self.relate('connect','flap','envelope')

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

