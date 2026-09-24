"""A 360-degree VR band with a small game symbol.
Symbol plan: cylinder: curved band silhouette; source supplies 360 text and open-mouth game mark.
Keyshape: HRECT_L; fixed profile envelope is recorded in ink_extremes.
Reduction: None; digits and game symbol retained.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='c710459a-2d6e-4c8e-89da-f6b82e663367'
SOURCE_PATH='icon_set/work/todo-references/video game 360 vr_c710459a-2d6e-4c8e-89da-f6b82e663367.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='video-game-360-vr'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('video', 'game', '360', 'vr')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_arc('band-top',(4,24),(44,24),radius_x=20,radius_y=6,sweep=False)
        self.add_line('band-right',(44,24),(44,34))
        self.add_arc('band-bottom',(44,34),(4,34),radius_x=20,radius_y=6)
        self.add_line('band-left',(4,34),(4,24))
        self.add_contour('band','band-top','band-right','band-bottom','band-left',closed=True)
        self.add_bezier('three',(13,9),((21,6),(21,13),(15,13)),((21,13),(21,21),(13,17)))
        self.add_bezier('six',(28,9),((20,6),(20,19),(26,19)),((32,19),(30,11),(23,14)))
        self.add_arc('zero-top',(32,13),(40,13),radius_x=4,radius_y=5)
        self.add_arc('zero-bottom',(40,13),(32,13),radius_x=4,radius_y=5)
        self.add_contour('zero','zero-top','zero-bottom',closed=True)
        self.add_arc('game-mouth',(27,31),(27,37),radius_x=4,large_arc=True,sweep=False)
        self.add_polyline('game-wedge',(27,37),(24,34),(27,31));self.relate('connect','game-mouth','game-wedge')

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
