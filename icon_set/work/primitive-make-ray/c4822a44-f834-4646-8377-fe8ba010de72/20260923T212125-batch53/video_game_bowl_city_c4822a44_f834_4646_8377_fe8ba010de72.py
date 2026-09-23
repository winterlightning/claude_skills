"""A round game flask containing a small stepped city and a floating ball.
Symbol plan: cylinder: round vessel vocabulary; source supplies narrow neck, city blocks and ball.
Keyshape: VRECT_L; fixed profile envelope is recorded in ink_extremes.
Reduction: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c4822a44-f834-4646-8377-fe8ba010de72'
SOURCE_PATH='icon_set/work/todo-references/video game bowl city_c4822a44-f834-4646-8377-fe8ba010de72.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='video-game-bowl-city'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('video', 'game', 'bowl', 'city')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_bezier('bowl-left',(18,14),((12,16),(8,21),(8,28)),((8,37),(15,44),(24,44)))
        self.add_bezier('bowl-right',(24,44),((33,44),(40,37),(40,28)),((40,21),(36,16),(30,14)))
        self.add_polyline('neck',(18,14),(18,8),(30,8),(30,14))
        self.relate('connect','neck','bowl-left');self.relate('connect','neck','bowl-right');self.relate('connect','bowl-left','bowl-right')
        self.add_line('lip',(14,8),(34,8))
        self.circle('ball',34,6,2)
        self.add_polyline('city',(16,35),(16,31),(20,31),(20,27),(24,27),(24,23),(28,23),(28,27),(32,27),(32,35),closed=True)

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
