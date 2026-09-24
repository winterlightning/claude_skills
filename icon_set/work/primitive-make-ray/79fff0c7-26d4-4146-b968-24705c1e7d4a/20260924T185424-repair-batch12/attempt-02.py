"""A balance scale weighing a person against a dollar sign.
Symbol plan: scale: mirrored pans and central pedestal; human_ref/user.svg: round head and smooth shoulders.
Keyshape: HRECT_L; fixed profile envelope is recorded in ink_extremes.
Reduction: Small arm/leg outline steps simplified; human, dollar, both pans and pedestal retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='79fff0c7-26d4-4146-b968-24705c1e7d4a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/user cash scale 1_79fff0c7-26d4-4146-b968-24705c1e7d4a.svg'
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
        # Human circle and broad shoulders, exact head-bottom 14 to shoulder-top 22.
        self.circle('head',12,11,3)
        self.add_arc('shoulders',(4,30),(20,30),radius_x=8)
        for n,cx in [('left',12),('right',36)]:
            self.add_polyline(n+'-rim',(cx-8,30),(cx,30),(cx+8,30))
            self.add_arc(n+'-pan',(cx+8,30),(cx-8,30),radius_x=8)
            self.relate('connect',n+'-rim',n+'-pan')
        self.relate('connect','shoulders','left-rim')
        self.add_polyline('base',(20,40),(24,40),(28,40))
        self.add_line('stem',(24,40),(24,30))
        self.add_polyline('beam',(20,30),(24,30),(28,30))
        self.relate('connect','stem','base','beam')
        self.relate('connect','beam','left-rim','right-rim')
        self.add_polyline('dollar-top',(40,10),(36,10),(36,8))
        self.add_arc('dollar-upper',(36,10),(36,18),radius_x=4,sweep=False)
        self.add_arc('dollar-lower',(36,18),(36,26),radius_x=4)
        self.add_polyline('dollar-bottom',(32,26),(36,26),(36,28))
        self.relate('connect','dollar-upper','dollar-top','dollar-lower')
        self.relate('connect','dollar-lower','dollar-bottom')

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
