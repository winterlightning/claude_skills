"""A square parent connects to two ring leaves. Lucide network informs the parent and bus; full circles retain the distinct leaf identity. No semantic features removed. Equal leaf radius and bilateral symmetry.
SOLO48 VRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='f540eba4-5f02-4b15-ab87-852a4076e2c9'
SOURCE_PATH='pictographic-primitives/programing/hierarchy_f540eba4-5f02-4b15-ab87-852a4076e2c9.svg'
AUTHOR='gpt-6'

class HierarchyCircleLeaves(Solo48):
    icon_id='hierarchy-circle-leaves'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    aliases=()
    keywords=('hierarchy', 'tree', 'parent', 'nodes', 'circles', 'structure', 'diagram', 'organization')

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

        node('parent',20,4,8,8)
        self.add_line('root-stem',(24,12),(24,25))
        join('parent','root-stem')
        for name,x in (('left',13),('right',35)):
            self.add_polyline(name+'-branch',(24,25),(x,25),(x,34))
            ring(name+'-leaf',x,39,5)
            join(name+'-branch',name+'-leaf')
        join('root-stem','left-branch','right-branch')
