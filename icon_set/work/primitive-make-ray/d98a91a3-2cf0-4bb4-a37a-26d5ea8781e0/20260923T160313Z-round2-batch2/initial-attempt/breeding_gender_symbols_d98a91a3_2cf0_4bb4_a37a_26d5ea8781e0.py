"""An open male symbol with two floating circles and a triangle.
Plan: mars: open round body and attached diagonal arrow.
Reduction: None; unequal circles, triangle, ring and arrow retained.
Author geometry backwards from the exact SQUARE envelope.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='d98a91a3-2cf0-4bb4-a37a-26d5ea8781e0'
SOURCE_PATH='icon_set/work/todo-references/breeding gender symbols_d98a91a3-2cf0-4bb4-a37a-26d5ea8781e0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='breeding-gender-symbols'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('breeding', 'gender', 'symbols')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_arc('ring-top',(14,16),(24,6),radius_x=10)
        self.add_arc('ring-right',(24,6),(34,16),radius_x=10)
        self.add_arc('ring-bottom',(34,16),(24,26),radius_x=10)
        self.add_contour('open-ring','ring-top','ring-right','ring-bottom')
        self.add_line('shaft',(34,16),(42,8))
        self.add_polyline('arrowhead',(34,8),(42,8),(42,16));self.relate('connect','shaft','open-ring');self.relate('connect','shaft','arrowhead')
        self.circle('small-circle',9,28,3)
        self.circle('large-circle',22,22,4)
        self.add_polyline('triangle',(16,34),(24,42),(8,42),closed=True)

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
