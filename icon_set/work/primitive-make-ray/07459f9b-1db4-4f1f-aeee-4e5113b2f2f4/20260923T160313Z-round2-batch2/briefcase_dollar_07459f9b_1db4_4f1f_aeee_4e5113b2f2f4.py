"""A briefcase with an attached handle and dollar sign.
Symbol plan: briefcase: rounded case and genuine handle joins; dollar-sign: smooth currency lobes.
Reduction: None.
Keyshape: SQUARE; exact bounds are obtained from the model.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='07459f9b-1db4-4f1f-aeee-4e5113b2f2f4'
SOURCE_PATH='icon_set/work/todo-references/briefcase dollar_07459f9b-1db4-4f1f-aeee-4e5113b2f2f4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='briefcase-dollar'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('briefcase', 'dollar')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('case-top',(10,14),(16,14),(32,14),(38,14))
        self.add_arc('tr',(38,14),(42,18),radius_x=4)
        self.add_line('right',(42,18),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left',(6,38),(6,18))
        self.add_arc('tl',(6,18),(10,14),radius_x=4)
        parts=['case-top','tr','right','br','bottom','bl','left','tl']
        for i,n in enumerate(parts):self.relate('connect',n,parts[(i+1)%8])
        self.add_polyline('handle',(16,14),(16,6),(32,6),(32,14));self.relate('connect','handle','case-top')
        self.dollar(24,28)
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
        self.add_bezier('dollar',(x+4,y-4),((x+2,y-5),(x+1,y-5),(x,y-5)),((x-7,y-5),(x-7,y),(x,y)),((x+7,y),(x+7,y+5),(x,y+5)),((x-1,y+5),(x-2,y+5),(x-4,y+4)))
        self.add_line('stem-top',(x,y-6),(x,y-5));self.relate('connect','dollar','stem-top')
        self.add_line('stem-bottom',(x,y+5),(x,y+6));self.relate('connect','dollar','stem-bottom')

    def euro(self,x):
        self.add_bezier('euro',(x+3,22),((x-2,19),(x-8,21),(x-8,28)),((x-8,35),(x-2,37),(x+3,34)))
        self.add_polyline('crossbar',(x-11,28),(x-8,28),(x,28));self.relate('connect','euro','crossbar')
