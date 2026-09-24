"""An Indian rupee sign inside a circular badge.
Symbol plan: indian-rupee: two horizontal bars, curved bowl and descending leg.
Reduction: None.
Keyshape: CIRCLE; model supplies exact ink extremes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='54a12c47-2b42-4009-a41b-1b8ab3a9ef93'
SOURCE_PATH='icon_set/work/todo-references/circle rupee_54a12c47-2b42-4009-a41b-1b8ab3a9ef93.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circle-rupee'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('circle', 'rupee')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('ring',24,24,20)
        self.add_polyline('top',(17,15),(24,15),(31,15))
        self.add_polyline('middle',(17,23),(29,23),(31,23))
        self.add_arc('bowl-upper',(24,15),(29,23),radius_x=5,radius_y=8)
        self.add_arc('bowl-lower',(29,23),(24,31),radius_x=5,radius_y=8)
        self.add_polyline('leg',(24,31),(17,31),(27,35))
        self.add_contour('bowl','bowl-upper','bowl-lower')
        self.relate('connect','bowl','top');self.relate('connect','bowl','middle');self.relate('connect','bowl','leg')

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

