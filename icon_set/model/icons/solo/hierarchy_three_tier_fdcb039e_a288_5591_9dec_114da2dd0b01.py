"""A wide parent bar feeds two columns of two smaller bars. The separate branch bus is absorbed into the parent lower edge, leaving direct stems to the second tier. Lucide network informs shared attachment points and equal child bars; all five nodes retained.
SOLO48 VRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='fdcb039e-a288-5591-9dec-114da2dd0b01'
SOURCE_PATH='pictographic-primitives/programing/hierarchy_fdcb039e-a288-5591-9dec-114da2dd0b01.svg'
AUTHOR='gpt-6'

class HierarchyThreeTier(Solo48):
    icon_id='hierarchy-three-tier'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('hierarchy', 'tree', 'tiers', 'structure', 'organization', 'chart', 'levels', 'diagram')

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

        self.add_polyline('parent',(14,4),(34,4),(34,12),(14,12),closed=True)
        for name,x in (('left',14),('right',34)):
            node(name+'-middle',x-6,20,12,8)
            node(name+'-lower',x-6,36,12,8)
            self.add_line(name+'-upper-stem',(x,12),(x,20))
            self.add_line(name+'-lower-stem',(x,28),(x,36))
            join('parent',name+'-upper-stem')
            join(name+'-upper-stem',name+'-middle')
            join(name+'-middle',name+'-lower-stem')
            join(name+'-lower-stem',name+'-lower')
