"""A row of library books with rounded feet and spine bands.
Symbol plan: library: repeat spacing; source supplies open tops and rounded spine feet.
Reduction: Four books reduced to three equal books to keep the required spacing; two bands per spine retained.
Keyshape: HRECT_L; exact bounds are obtained from the model.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='2841f97c-3470-4026-a287-d82828da5d59'
SOURCE_PATH='icon_set/work/todo-references/book library shelf_2841f97c-3470-4026-a287-d82828da5d59.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='book-library-shelf'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('book', 'library', 'shelf')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        for i,x in enumerate((4,20,36)):
            nodes=[(x,8),(x,16),(x,28),(x,36)]
            members=[]
            for j,(a,b) in enumerate(zip(nodes,nodes[1:])):
                name=f'book-{i}-left-{j}';self.add_line(name,a,b);members.append(name)
            name=f'book-{i}-foot';self.add_arc(name,(x,36),(x+8,36),radius_x=4,sweep=False);members.append(name)
            for j,(ya,yb) in enumerate(((36,28),(28,16),(16,8))):
                name=f'book-{i}-right-{j}';self.add_line(name,(x+8,ya),(x+8,yb));members.append(name)
            self.add_contour(f'book-{i}',*members)
            for y in (16,28):
                name=f'book-{i}-band-{y}';self.add_line(name,(x,y),(x+8,y));self.relate('connect',name,f'book-{i}')

    def circle(self,name,cx,cy,r):
        pts=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            m=f'{name}-{i}';self.add_arc(m,a,b,radius_x=r);members.append(m)
        self.add_contour(name,*members,closed=True)

    def rounded(self,name,l,t,r,b,rad,breaks=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad),(l+rad,t)]
        members=[];breaks=breaks or {}
        for i,(a,z) in enumerate(zip(pts,pts[1:])):
            if i%2:
                m=f'{name}-{i}';self.add_arc(m,a,z,radius_x=rad);members.append(m)
            else:
                nodes=[a]+breaks.get(i,[])+[z]
                for j,(start,end) in enumerate(zip(nodes,nodes[1:])):
                    if start==end:continue
                    m=f'{name}-{i}-{j}';self.add_line(m,start,end);members.append(m)
        self.add_contour(name,*members,closed=True)


    def browser(self):
        self.rounded('window',8,4,40,44,4,breaks={2:[(40,12)],6:[(8,12)]})
        self.add_line('header',(8,12),(40,12));self.relate('connect','header','window')

    def dollar(self,x,y):
        self.add_bezier('dollar',(x+4,y-6),((x+2,y-7),(x+1,y-7),(x,y-7)),((x-7,y-7),(x-7,y),(x,y)),((x+7,y),(x+7,y+7),(x,y+7)),((x-1,y+7),(x-2,y+7),(x-4,y+6)))
        self.add_line('stem-top',(x,y-8),(x,y-7));self.relate('connect','dollar','stem-top')
        self.add_line('stem-bottom',(x,y+7),(x,y+8));self.relate('connect','dollar','stem-bottom')

    def euro(self,x):
        self.add_bezier('euro',(x+3,22),((x-2,19),(x-8,21),(x-8,28)),((x-8,35),(x-2,37),(x+3,34)))
        self.add_polyline('crossbar',(x-11,28),(x-8,28),(x,28));self.relate('connect','euro','crossbar')
