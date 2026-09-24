"""A house beneath a large central rating star and two smaller stars.
Symbol plan: Three five-point stars sit above a symmetric pitched-roof house. Ink extremes (4,4)-(44,44).
Construction: star: five-point outline; house: mirrored roof and doorway.
Human construction: Not applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f53e79c7-b34f-44d2-9af3-49b5684cc631'
SOURCE_PATH = 'icon_set/work/todo-references/real estate favorite house rating_f53e79c7-b34f-44d2-9af3-49b5684cc631.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'real-estate-favorite-house-rating'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('real', 'estate', 'favorite', 'house', 'rating')

    def build(self):
        self.add_polyline('main-star',(24,6),(27,12),(33,12),(29,16),(30,22),(24,19),(18,22),(19,16),(15,12),(21,12),closed=True)
        for i,cx in enumerate((10,38)):
            self.add_polyline(f'star-{i}',(cx,16),(cx+1,19),(cx+4,19),(cx+2,22),(cx+3,25),(cx,23),(cx-3,25),(cx-2,22),(cx-4,19),(cx-1,19),closed=True)
        self.add_polyline('roof',(12,32),(24,24),(36,32))
        self.add_line('walls-1',(14, 34),(14, 42))
        self.add_line('walls-2',(14, 42),(21, 42))
        self.add_line('walls-3',(21, 42),(21, 38))
        self.add_arc('door',(21,38),(27,38),radius_x=3)
        self.add_line('walls-right-1',(27, 38),(27, 42))
        self.add_line('walls-right-2',(27, 42),(34, 42))
        self.add_line('walls-right-3',(34, 42),(34, 34))
        self.add_contour('house','walls-1','walls-2','walls-3','door','walls-right-1','walls-right-2','walls-right-3')

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

