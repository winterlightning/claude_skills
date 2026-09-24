"""Two video panels separated by a dashed cut line and a top marker.
Symbol plan: split: paired panels and central division; source supplies the downward triangle.
Keyshape: SQUARE; fixed profile envelope is recorded in ink_extremes.
Reduction: None; paired footers and three cut marks retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2dcda804-d52b-4984-9a4e-b6abdfa0030f'
SOURCE_PATH = 'pictographic-primitives/video/video edit split_2dcda804-d52b-4984-9a4e-b6abdfa0030f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id='video-edit-split'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('video', 'edit', 'split')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        for name,l,r in [('left',6,16),('right',32,42)]:
            self.rounded(name,l,24,r,42,3,breaks={2:[(r,34)],6:[(l,34)]})
            self.add_line(name+'-footer',(l,34),(r,34));self.relate('connect',name+'-footer',name)
        self.add_polyline('marker',(18,6),(30,6),(24,16),closed=True)
        for i,y in enumerate((24,36)):self.add_line(f'cut-{i}',(24,y),(24,y+4))

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

# Final repair review: Two video strips flank a dashed cut line beneath a triangular marker.
# SQUARE fits paired strips and the upper marker.
# Changes: Marker made taller; strips moved downward; no defining components omitted.
# validate_icon: valid; build gate: pass with zero errors and zero warnings.
