"""The four swept bands of the Crowdin logo.
Symbol plan: No useful exact logo match; coherent cubic boundaries preserve the nested broken C arrangement.
Reduction: None; all four bands retained.
Keyshape: HRECT_L; model supplies exact ink extremes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='e89d9bcb-0e93-4a07-abd4-7740608fbbd7'
SOURCE_PATH='icon_set/work/todo-references/crowdin logo_e89d9bcb-0e93-4a07-abd4-7740608fbbd7.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='crowdin-logo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('crowdin', 'logo')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_bezier('outer-upper',(44,10),((38,8),(34,8),(28,8)),((16,8),(6,12),(4,20)))
        self.add_line('upper-end',(4,20),(12,22))
        self.add_bezier('upper-inner',(12,22),((18,10),(32,12),(44,12)))
        self.add_contour('upper-band','outer-upper','upper-end','upper-inner')
        self.add_bezier('inner-upper',(42,21),((32,19),(25,22),(23,29)))
        self.add_line('inner-end',(23,29),(29,30))
        self.add_bezier('inner-return',(29,30),((31,24),(36,24),(40,24)))
        self.add_line('inner-tip',(40,24),(42,21))
        self.add_contour('inner-upper-band','inner-upper','inner-end','inner-return','inner-tip',closed=True)
        self.add_line('lower-end',(4,31),(12,32))
        self.add_bezier('lower-inner',(12,32),((14,37),(18,39),(24,40)))
        self.add_bezier('lower-outer',(24,40),((12,40),(4,38),(4,31)))
        self.add_contour('lower-band','lower-end','lower-inner','lower-outer',closed=True)
        self.add_line('small-end',(23,38),(29,38))
        self.add_bezier('small-inner',(29,38),((31,39),(34,40),(37,40)))
        self.add_bezier('small-outer',(37,40),((31,40),(26,40),(23,38)))
        self.add_contour('small-band','small-end','small-inner','small-outer',closed=True)

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

