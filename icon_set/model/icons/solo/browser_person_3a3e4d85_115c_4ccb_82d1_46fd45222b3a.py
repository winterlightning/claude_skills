"""A browser containing a circular user head above open shoulders.
Symbol plan: panels-top-left: rounded window and header; human_ref/user.svg: circular head and smooth open shoulder bust.
Reduction: Tiny title-bar marks omitted to preserve the clear header band.
Keyshape: VRECT_L; exact bounds are obtained from the model.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='3a3e4d85-115c-4ccb-82d1-46fd45222b3a'
SOURCE_PATH='icon_set/work/todo-references/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='browser-person'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('browser', 'person')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.browser()
        self.circle('head',24,23,3)
        self.add_arc('shoulder-left',(17,35),(24,34),radius_x=7,radius_y=1)
        self.add_arc('shoulder-right',(24,34),(31,35),radius_x=7,radius_y=1)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        # Circular head bottom26; shoulder apex34 => exact8 centerline /4 ink gap.

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
