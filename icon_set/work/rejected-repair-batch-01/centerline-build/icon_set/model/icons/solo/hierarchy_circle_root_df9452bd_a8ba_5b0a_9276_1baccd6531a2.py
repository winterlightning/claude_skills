"""A circular root feeds three square children through a rounded branch bus. Lucide network informs tangent quarter-circle elbows and repeated children. Tiny corner details are omitted; all four nodes remain and the arrangement mirrors on x=24.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='df9452bd-a8ba-5b0a-9276-1baccd6531a2'
SOURCE_PATH='pictographic-primitives/programing/hierarchy_df9452bd-a8ba-5b0a-9276-1baccd6531a2.svg'
AUTHOR='gpt-6'

class HierarchyCircleRoot(Solo48):
    icon_id='hierarchy-circle-root'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('hierarchy', 'tree', 'root', 'nodes', 'structure', 'diagram', 'organization', 'network')

    def build(self) -> None:
        def ring(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)

        def node(name,x,y,w,h):
            self.add_polyline(name,(x,y),(x+w//2,y),(x+w,y),(x+w,y+h),(x+w//2,y+h),(x,y+h),closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        ring('root',24,11,3)
        self.add_line('root-stem',(24,14),(24,23))
        join('root','root-stem')
        for side,sign in (('left',-1),('right',1)):
            x=24+sign*16
            self.add_line(side+'-bus',(24,23),(x-sign*3,23))
            self.add_arc(side+'-elbow',(x-sign*3,23),(x,26),radius_x=3,sweep=sign==1)
            self.add_line(side+'-drop',(x,26),(x,32))
            self.add_contour(side+'-branch',side+'-bus',side+'-elbow',side+'-drop')
            node(side+'-child',x-4,32,8,8)
            join(side+'-branch',side+'-child')
        self.add_line('middle-drop',(24,23),(24,32))
        node('middle-child',20,32,8,8)
        join('middle-child','middle-drop')
        join('root-stem','left-branch','right-branch','middle-drop')
