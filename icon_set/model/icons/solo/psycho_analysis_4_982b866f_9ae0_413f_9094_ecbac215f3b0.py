"""A head profile with a large round thought region above its rear half.
Symbol plan: Open profile silhouette and separate circular mind region retain the upper-right arrangement. Ink extremes (4,4)-(44,44).
Construction: No useful exact Lucide match found; supplied profile owns the construction.
Human construction: human-reference.md and human_ref/user.svg inspected. This is a continuous head/neck profile with a thought circle, not a detached stick-figure head; detached-head flags do not apply.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '982b866f-9ae0-413f-9094-ecbac215f3b0'
SOURCE_PATH = 'icon_set/work/todo-references/psycho analysis 4_982b866f-9ae0-413f-9094-ecbac215f3b0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'psycho-analysis-4'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('psycho', 'analysis', '4')

    def build(self):
        self.circle('mind-circle',32,16,10)
        self.add_bezier('forehead',(14,15),((10,16),(10,19),(10,23)))
        self.add_line('nose-1',(10, 23),(6, 30))
        self.add_line('nose-2',(6, 30),(10, 31))
        self.add_line('nose-3',(10, 31),(10, 34))
        self.add_bezier('chin',(10,34),((10,37),(13,37),(16,37)))
        self.add_line('neck-front',(16,37),(16,42))
        self.add_contour('profile-front','forehead','nose-1','nose-2','nose-3','chin','neck-front')
        self.add_bezier('profile-back',(34,34),((34,36),(30,37),(30,39)))
        self.add_line('neck-back',(30,39),(30,42))
        self.add_contour('rear','profile-back','neck-back')

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

