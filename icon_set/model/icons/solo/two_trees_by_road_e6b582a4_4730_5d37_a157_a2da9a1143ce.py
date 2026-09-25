"""Two unequal rounded trees stand beside a road. HRECT extremes (4,8)-(44,40); trunks share the ground baseline while canopy sizes remain intentionally different.
Reduction: Smoothed foliage lobes into round canopies and removed the small branch.
Lucide construction: tree-deciduous
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6b582a4-4730-5d37-a157-a2da9a1143ce'
SOURCE_PATH = 'pictographic-primitives/nature/outdoors tree road_e6b582a4-4730-5d37-a157-a2da9a1143ce.svg'
AUTHOR = 'gpt-6'


class TwoTreesByRoad(Solo48):
    icon_id = 'two-trees-by-road'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('trees', 'road', 'park', 'outdoors', 'landscape', 'ground', 'nature', 'street')

    def build(self) -> None:
        for i,(cx,cy,r) in enumerate(((12,18,6),(34,16,8))):
            self.add_arc(f"tree-{i}-top",(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(f"tree-{i}-right",(cx+r,cy),(cx,cy+r),radius_x=r)
            self.add_arc(f"tree-{i}-left",(cx,cy+r),(cx-r,cy),radius_x=r)
            self.add_contour(f"tree-{i}",f"tree-{i}-top",f"tree-{i}-right",f"tree-{i}-left",closed=True)
            self.add_line(f"trunk-{i}",(cx,cy+r),(cx,32))
            self.relate("connect",f"trunk-{i}",f"tree-{i}-right")
            self.relate("connect",f"trunk-{i}",f"tree-{i}-left")
        self.add_polyline("ground",(4,32),(12,32),(34,32),(44,32))
        for i in range(2):
            self.relate("connect",f"trunk-{i}",f"ground-{i+1}")
            self.relate("connect",f"trunk-{i}",f"ground-{i+2}")
        self.add_line("road",(4,40),(44,40))
