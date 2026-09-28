"""Two opening quotation marks.
Plan: HRECT_L fits two equal 15-unit symbols on a 25-unit pitch.
Reduction: No component removed; enlarged return caps and opened the tail bands.
Construction: Lucide quote: rounded blocks, curved return tails and repeated definitions.
Layout: Two identical symbols; curve radius5 at the tail cap, radius4 at body corners."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bbf400c0-4ed9-481e-8643-979aa728bc9d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/quote left_bbf400c0-4ed9-481e-8643-979aa728bc9d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'quote-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('quote', 'left')

    def build(self):
        for i,x in enumerate((4,29)):self.opening_quote(f'quote-{i}',x,closing=False)

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
        bez('-outer',(0,24),((0,16),(4,8),(10,8)))
        self.add_arc(name+'-crown',p((10,8)),p((15,13)),radius_x=5)
        self.add_arc(name+'-return',p((15,13)),p((10,18)),radius_x=5)
        bez('-inner',(10,18),((9,18),(9,21),(9,24)))
        line('-shelf',(9,24),(11,24))
        arc('-tr',(11,24),(15,28))
        line('-right',(15,28),(15,36))
        arc('-br',(15,36),(11,40))
        line('-bottom',(11,40),(4,40))
        arc('-bl',(4,40),(0,36))
        line('-left',(0,36),(0,24))
        self.add_contour(name,*[name+n for n in ('-outer','-crown','-return','-inner','-shelf','-tr','-right','-br','-bottom','-bl','-left')],closed=True)

