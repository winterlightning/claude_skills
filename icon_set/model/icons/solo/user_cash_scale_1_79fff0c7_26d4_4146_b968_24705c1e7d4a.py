"""A balance scale weighing a person against a dollar sign.
Symbol plan: scale: mirrored pans and central pedestal; human_ref/user.svg: round head and smooth shoulders.
Keyshape: HRECT_L; fixed profile envelope is recorded in ink_extremes.
Reduction: Small arm/leg outline steps simplified; human, dollar, both pans and pedestal retained.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='79fff0c7-26d4-4146-b968-24705c1e7d4a'
SOURCE_PATH='icon_set/work/todo-references/user cash scale 1_79fff0c7-26d4-4146-b968-24705c1e7d4a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='user-cash-scale-1'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('user', 'cash', 'scale', '1')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.person('person',12,12,4,30)
        for name,cx in [('left',12),('right',36)]:
            self.add_polyline(name+'-rim',(cx-8,30),(cx,30),(cx+8,30))
            self.add_arc(name+'-bowl-right',(cx+8,30),(cx,35),radius_x=8,radius_y=5)
            self.add_arc(name+'-bowl-left',(cx,35),(cx-8,30),radius_x=8,radius_y=5)
            self.add_contour(name+'-bowl',name+'-bowl-right',name+'-bowl-left')
            self.relate('connect',name+'-rim',name+'-bowl')
        self.relate('connect','person-body','left-rim')
        self.add_polyline('pedestal',(18,40),(20,36),(22,32),(26,32),(28,36),(30,40),closed=True)
        self.add_bezier('left-link',(12,35),((12,38),(17,36),(20,36)))
        self.add_bezier('right-link',(28,36),((31,36),(36,38),(36,35)))
        self.relate('connect','left-link','left-bowl');self.relate('connect','left-link','pedestal')
        self.relate('connect','right-link','right-bowl');self.relate('connect','right-link','pedestal')
        self.add_bezier('dollar',(39,11),((33,8),(31,14),(36,15)),((41,16),(40,22),(33,20)))
        self.add_polyline('dollar-stem',(36,8),(36,15),(36,22));self.relate('connect','dollar','dollar-stem')

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


    def person(self,name,cx,cy,r,bottom):
        # Shared human reference: exact detached head gap at the shoulder apex.
        self.circle(name+'-head',cx,cy,r)
        top=cy+r+8;w=6
        self.add_arc(name+'-shoulder-left',(cx-w,top+6),(cx,top),radius_x=w)
        self.add_arc(name+'-shoulder-right',(cx,top),(cx+w,top+6),radius_x=w)
        self.add_line(name+'-right',(cx+w,top+6),(cx+w,bottom))
        self.add_line(name+'-bottom-right',(cx+w,bottom),(cx,bottom))
        self.add_line(name+'-bottom-left',(cx,bottom),(cx-w,bottom))
        self.add_line(name+'-left',(cx-w,bottom),(cx-w,top+6))
        self.add_contour(name+'-body',name+'-shoulder-left',name+'-shoulder-right',name+'-right',name+'-bottom-right',name+'-bottom-left',name+'-left',closed=True)

    def dollar(self,cx,cy):
        self.add_bezier('dollar',(cx+3,cy-6),((cx-3,cy-9),(cx-6,cy-3),(cx,cy)),((cx+6,cy+3),(cx+3,cy+9),(cx-3,cy+6)))
        self.add_polyline('dollar-stem',(cx,cy-9),(cx,cy),(cx,cy+9))
        self.relate('connect','dollar','dollar-stem')
