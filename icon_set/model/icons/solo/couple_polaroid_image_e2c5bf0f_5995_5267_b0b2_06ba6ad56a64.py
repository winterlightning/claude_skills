"""A Polaroid photograph of a couple beneath a heart.
Symbol plan: image: coherent photo frame; human_ref/user.svg: paired circular heads and smooth shoulders.
Reduction: None; both people and the heart retained.
Keyshape: VRECT_L; model supplies exact ink extremes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='e2c5bf0f-5995-5267-b0b2-06ba6ad56a64'
SOURCE_PATH='icon_set/work/todo-references/couple polaroid image_e2c5bf0f-5995-5267-b0b2-06ba6ad56a64.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='couple-polaroid-image'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'romance'
    categories = ('primitives', 'romance')
    aliases=()
    keywords=('couple', 'polaroid', 'image')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('frame',(8,4),(40,4),(40,36),(40,44),(8,44),(8,36),closed=True)
        self.add_polyline('photo-bottom',(8,36),(11,36),(23,36),(25,36),(37,36),(40,36));self.relate('connect','frame','photo-bottom')
        for i,cx in enumerate((17,31)):
            self.circle(f'head-{i}',cx,22,3)
            self.add_arc(f'shoulders-{i}',(cx-6,36),(cx+6,36),radius_x=6,radius_y=3)
            self.relate('connect',f'shoulders-{i}','photo-bottom')
        # Head bottom25, shoulder apex33: exact8 centerline /4 ink gap.
        self.add_bezier('heart',(24,11),((19,6),(16,12),(24,17)),((32,12),(29,6),(24,11)))

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

