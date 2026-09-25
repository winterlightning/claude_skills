"""A browser with a navigation column and two stacked content cards.
Symbol plan: panels-top-left: shared header/sidebar nodes and rounded frame.
Reduction: Header controls omitted; five navigation marks reduced to two dots and two repeated content cards reduced to one for the spacing budget.
Keyshape: HRECT_L; exact bounds are obtained from the model.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='b317a6a6-fb5f-4063-b4ca-9345a6cec436'
SOURCE_PATH='icon_set/work/todo-references/browser page text 2_b317a6a6-fb5f-4063-b4ca-9345a6cec436.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='browser-page-text-2'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('browser', 'page', 'text', '2')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        # Explicit frame walls preserve tangent joins and let the checker prove straight-wall clearances.
        self.add_line('top',(8,8),(40,8))
        self.add_arc('tr',(40,8),(44,12),radius_x=4)
        self.add_polyline('right',(44,12),(44,16),(44,36))
        self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_polyline('bottom',(40,40),(20,40),(8,40))
        self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_polyline('left',(4,36),(4,16),(4,12))
        self.add_arc('tl',(4,12),(8,8),radius_x=4)
        parts=['top','tr','right','br','bottom','bl','left','tl']
        for i,p in enumerate(parts):self.relate('connect',p,parts[(i+1)%len(parts)])
        self.add_polyline('header',(4,16),(20,16),(44,16))
        self.relate('connect','header','left');self.relate('connect','header','right')
        self.add_line('sidebar',(20,16),(20,40));self.relate('connect','sidebar','header');self.relate('connect','sidebar','bottom')
        for i,y in enumerate((24,32)):self.add_dot(f'nav-{i}',(12,y))
        self.add_polyline('card',(28,24),(36,24),(36,32),(28,32),closed=True)
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
