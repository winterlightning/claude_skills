"""Three list bars connect to a right-hand bracket spine extending above the first row. Lucide list-tree informs the three-level rhythm. Bar frames reduce to three bullet-and-stroke rows while the raised spine remains.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID='f31a007d-3a5d-501c-a760-c2b7f61bfea3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hierarchy-bracket-list/20260926T172218Z-thuan-mac-1/reference/hierarchy_f31a007d-3a5d-501c-a760-c2b7f61bfea3.svg'
AUTHOR = 'gpt-6'

class HierarchyBracketList(Solo48):
    icon_id='hierarchy-bracket-list'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('hierarchy', 'list', 'tree', 'structure', 'spine', 'bars', 'outline', 'diagram')

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

        ys=(16,28,40)
        self.add_line('spine-top',(44,8),(44,16))
        self.add_line('spine-middle',(44,16),(44,28))
        self.add_line('spine-bottom',(44,28),(44,40))
        self.add_contour('spine','spine-top','spine-middle','spine-bottom')
        for i,y in enumerate(ys):
            self.add_dot(f'item-{i}',(4,y))
            self.add_line(f'level-{i}',(14,y),(44,y))
            join(f'level-{i}','spine')
