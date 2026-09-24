"""A suitcase below a floating weighing dial.
Symbol plan: gauge: circular dial and diagonal needle; luggage: joined top handle.
Reduction: Both decorative suitcase stripes omitted to preserve the case opening.
Keyshape: VRECT_L; exact bounds are obtained from the model.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='ee2a071e-6904-4d7d-a879-a7315aec3bd6'
SOURCE_PATH='icon_set/work/todo-references/baggage weight_ee2a071e-6904-4d7d-a879-a7315aec3bd6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='baggage-weight'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('baggage', 'weight')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('dial',24,12,8)
        self.add_line('needle',(24,12),(26,10))
        self.rounded('case',8,36,40,44,3,breaks={0:[(20,36),(28,36)]})
        self.add_polyline('handle',(20,36),(20,28),(28,28),(28,36));self.relate('connect','handle','case')
        self.add_polyline('ground',(8,44),(11,44),(37,44),(40,44));self.relate('connect','ground','case')

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
