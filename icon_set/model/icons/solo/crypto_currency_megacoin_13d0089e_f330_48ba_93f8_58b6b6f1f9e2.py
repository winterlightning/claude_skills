"""A Megacoin badge containing three equal domed arches.
Symbol plan: No useful exact currency logo match; parameterized identical arches within a circle.
Reduction: None; all three arches retained.
Keyshape: CIRCLE; model supplies exact ink extremes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='13d0089e-f330-48ba-93f8-58b6b6f1f9e2'
SOURCE_PATH='icon_set/work/todo-references/crypto currency megacoin_13d0089e-f330-48ba-93f8-58b6b6f1f9e2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='crypto-currency-megacoin'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'money'
    categories = ('primitives', 'money')
    aliases=()
    keywords=('crypto', 'currency', 'megacoin')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.circle('coin',24,24,20)
        for i,x in enumerate((8,20,32)):
            self.add_line(f'arch-{i}-left',(x,28),(x,23))
            self.add_arc(f'arch-{i}-top',(x,23),(x+8,23),radius_x=4)
            self.add_polyline(f'arch-{i}-rest',(x+8,23),(x+8,28),(x,28))
            self.relate('connect',f'arch-{i}-top',f'arch-{i}-left');self.relate('connect',f'arch-{i}-top',f'arch-{i}-rest');self.relate('connect',f'arch-{i}-left',f'arch-{i}-rest')

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

