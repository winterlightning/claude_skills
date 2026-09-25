"""The five-letter VALVE wordmark.
Symbol plan: No useful local logo original; hand-authored geometric letter strokes preserve the given word.
Keyshape: HRECT_M; fixed profile envelope is recorded in ink_extremes.
Reduction: None; all five letters retained.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='cbc8a808-542b-49df-b4bd-c313efd61052'
SOURCE_PATH='icon_set/work/todo-references/valve logo_cbc8a808-542b-49df-b4bd-c313efd61052.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='valve-logo'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('valve', 'logo')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_polyline('v-first',(4,10),(7,38),(10,10))
        self.add_polyline('a-sides',(13,38),(16,10),(19,38))
        self.add_line('a-bar',(14,29),(18,29))
        self.add_polyline('l',(23,10),(23,38),(28,38))
        self.add_polyline('v-second',(31,10),(34,38),(37,10))
        self.add_polyline('e',(44,10),(40,10),(40,24),(40,38),(44,38))
        self.add_line('e-middle',(40,24),(44,24));self.relate('connect','e','e-middle')

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
