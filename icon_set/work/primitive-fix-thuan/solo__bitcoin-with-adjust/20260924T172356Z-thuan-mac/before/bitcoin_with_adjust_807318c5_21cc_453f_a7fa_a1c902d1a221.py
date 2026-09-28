"""Two vertical adjustment sliders beside a Bitcoin B.
Symbol plan: sliders-vertical: shared vertical axes; bitcoin: joined double lobes.
Reduction: One Bitcoin stem per end rather than the pair of fine ticks; both sliders and both B lobes retained.
Keyshape: SQUARE; exact bounds are obtained from the model.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='807318c5-21cc-453f-a7fa-a1c902d1a221'
SOURCE_PATH='icon_set/work/todo-references/bitcoin with adjust_807318c5-21cc-453f-a7fa-a1c902d1a221.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='bitcoin-with-adjust'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('bitcoin', 'with', 'adjust')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        for name,x,y in [('low',10,32),('high',22,14)]:
            self.add_polyline(name+'-box',(x-4,y-4),(x,y-4),(x+4,y-4),(x+4,y+4),(x,y+4),(x-4,y+4),closed=True)
            self.add_line(name+'-top',(x,8),(x,y-4));self.add_line(name+'-bottom',(x,y+4),(x,40))
            self.relate('connect',name+'-box',name+'-top');self.relate('connect',name+'-box',name+'-bottom')
        self.add_polyline('b-stem',(35,6),(35,10),(35,24),(35,38),(35,42))
        self.add_arc('b-upper',(35,10),(35,24),radius_x=7,radius_y=7)
        self.add_arc('b-lower',(35,24),(35,38),radius_x=7,radius_y=7)
        self.relate('connect','b-stem','b-upper');self.relate('connect','b-stem','b-lower')

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
