"""A browser with a navigation column and two stacked content cards.
Plan: panels-top-left: shared header/sidebar nodes and rounded frame.
Reduction: Three tiny header controls omitted; five navigation ticks reduced to two.
Author geometry backwards from the exact VRECT_L envelope.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='b317a6a6-fb5f-4063-b4ca-9345a6cec436'
SOURCE_PATH='icon_set/work/todo-references/browser page text 2_b317a6a6-fb5f-4063-b4ca-9345a6cec436.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='browser-page-text-2'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('browser', 'page', 'text', '2')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.rounded('window',4,8,44,40,4,breaks={2:[(44,16)],4:[(20,40)],6:[(4,16)]})
        self.add_polyline('header',(4,16),(20,16),(44,16));self.relate('connect','header','window')
        self.add_line('sidebar',(20,16),(20,40));self.relate('connect','sidebar','header');self.relate('connect','sidebar','window')
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
