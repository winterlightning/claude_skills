"""A square parent branches to two larger square children. Lucide network informs the shared bus and consistent node construction. All three nodes and original square identities remain; bilateral symmetry.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bd04715e-144d-4c6c-84e7-b3504ca80063'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hierarchy-two-square-nodes/20260927T032104Z-thuan-mac-1/reference/hierarchy_bd04715e-144d-4c6c-84e7-b3504ca80063.svg'
AUTHOR = "gpt-6"

class HierarchyTwoSquareNodes(Solo48):
    icon_id='hierarchy-two-square-nodes'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "state")
    aliases=()
    keywords=('hierarchy', 'tree', 'parent', 'child', 'nodes', 'structure', 'diagram', 'organization')

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

        node('parent',18,6,12,12)
        self.add_line('root-stem',(24,18),(24,26))
        join('parent','root-stem')
        for name,x in (('left',11),('right',37)):
            self.add_polyline(name+'-branch',(24,26),(x,26),(x,34))
            node(name+'-child',x-5,34,10,8)
            join(name+'-branch',name+'-child')
        join('root-stem','left-branch','right-branch')
