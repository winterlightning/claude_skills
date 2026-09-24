"""A veterinarian with a stethoscope and cat badge.
Symbol plan: human_ref/user.svg: circular head and shoulders; stethoscope: tubing and bell; source supplies cat badge.
Keyshape: SQUARE; fixed profile envelope is recorded in ink_extremes.
Reduction: Fine facial detail omitted; collar, stethoscope and cat retained.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='16ebf22c-f2dd-4834-bf5b-3033fd6dbd8a'
SOURCE_PATH='icon_set/work/todo-references/veterinarian_16ebf22c-f2dd-4834-bf5b-3033fd6dbd8a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='veterinarian'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('veterinarian',)
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.circle('head',20,12,6)
        self.add_bezier('shoulders',(6,42),((6,28),(10,26),(20,26)),((28,26),(32,29),(32,34)))
        self.add_line('body-bottom',(6,42),(28,42));self.relate('connect','body-bottom','shoulders')
        self.add_polyline('collar',(16,26),(20,30),(24,26))
        self.add_line('stethoscope-tube',(14,27),(14,33))
        self.circle('stethoscope-bell',14,36,3);self.relate('connect','stethoscope-tube','stethoscope-bell')
        self.circle('badge',33,33,9)
        self.add_polyline('cat-ears',(28,32),(28,27),(32,29),(34,29),(38,27),(38,32))
        self.add_arc('cat-jaw',(38,32),(28,32),radius_x=5,sweep=True)
        self.relate('connect','cat-ears','cat-jaw')

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
