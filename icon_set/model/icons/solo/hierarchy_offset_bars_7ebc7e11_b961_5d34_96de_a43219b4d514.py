"""Three rectangular bars step diagonally, linked by elbows on their left edges. Lucide list-tree informs the elbow construction. Source roundings are simplified to round joins; all three bars retained. Deliberate diagonal offset expresses succession.
SOLO48 VRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='7ebc7e11-b961-5d34-96de-a43219b4d514'
SOURCE_PATH='pictographic-primitives/programing/hierarchy_7ebc7e11-b961-5d34-96de-a43219b4d514.svg'
AUTHOR='gpt-6'

class HierarchyOffsetBars(Solo48):
    icon_id='hierarchy-offset-bars'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    aliases=()
    keywords=('hierarchy', 'flow', 'steps', 'tree', 'connector', 'bars', 'structure', 'diagram')

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

        for i in range(3):
            x=8+i*8; y=4+i*16
            self.add_polyline(f'bar-{i}',(x,y),(x+16,y),(x+16,y+8),(x,y+8),(x,y+4),closed=True)
            if i:
                self.add_polyline(f'link-{i}',(x-8,y-8),(x-8,y+4),(x,y+4))
                join(f'link-{i}',f'bar-{i-1}')
                join(f'link-{i}',f'bar-{i}')
