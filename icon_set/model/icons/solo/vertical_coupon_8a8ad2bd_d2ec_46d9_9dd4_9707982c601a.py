"""A vertical coupon with centered top and bottom semicircular notches.
Symbol plan: ticket: inward notches and equal rounded corners.
Keyshape: VRECT_M; fixed profile envelope is recorded in ink_extremes.
Reduction: None.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='8a8ad2bd-d2ec-46d9-9dd4-9707982c601a'
SOURCE_PATH='icon_set/work/todo-references/vertical coupon_8a8ad2bd-d2ec-46d9-9dd4-9707982c601a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='vertical-coupon'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'container'
    aliases=()
    keywords=('vertical', 'coupon')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_line('top-left',(14,4),(20,4))
        self.add_arc('top-notch',(20,4),(28,4),radius_x=4,sweep=False)
        self.add_line('top-right',(28,4),(34,4))
        self.add_arc('tr',(34,4),(38,8),radius_x=4)
        self.add_line('right',(38,8),(38,40))
        self.add_arc('br',(38,40),(34,44),radius_x=4)
        self.add_line('bottom-right',(34,44),(28,44))
        self.add_arc('bottom-notch',(28,44),(20,44),radius_x=4,sweep=False)
        self.add_line('bottom-left',(20,44),(14,44))
        self.add_arc('bl',(14,44),(10,40),radius_x=4)
        self.add_line('left',(10,40),(10,8))
        self.add_arc('tl',(10,8),(14,4),radius_x=4)
        self.add_contour('coupon','top-left','top-notch','top-right','tr','right','br','bottom-right','bottom-notch','bottom-left','bl','left','tl',closed=True)

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
