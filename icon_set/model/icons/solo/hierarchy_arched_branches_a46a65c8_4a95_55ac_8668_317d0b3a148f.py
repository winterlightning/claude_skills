"""A square root connects to three square leaves through two broad arches and a central stem. The short common neck is removed; branch arches join directly at the parent. The middle leaf taper is normalized. Lucide network informs mirrored branching; broad elliptical arcs preserve the reference arches.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='a46a65c8-4a95-55ac-8668-317d0b3a148f'
SOURCE_PATH='pictographic-primitives/programing/hierarchy_a46a65c8-4a95-55ac-8668-317d0b3a148f.svg'
AUTHOR='gpt-6'

class HierarchyArchedBranches(Solo48):
    icon_id='hierarchy-arched-branches'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('hierarchy', 'tree', 'branches', 'structure', 'nodes', 'diagram', 'organization', 'network')

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

        node('parent',20,8,8,8)
        self.add_arc('left-arch',(24,16),(8,32),radius_x=16,sweep=False)
        self.add_arc('right-arch',(24,16),(40,32),radius_x=16)
        self.add_line('middle-stem',(24,16),(24,32))
        join('parent','left-arch','right-arch','middle-stem')
        for name,x,branch in (('left',8,'left-arch'),('middle',24,'middle-stem'),('right',40,'right-arch')):
            node(name+'-child',x-4,32,8,8)
            join(name+'-child',branch)
