"""A centered parent node branches to three equal child nodes. Rebuilt to fill the square profile symmetrically with a clear orthogonal hierarchy."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "80d19f77-aa43-4744-a812-6dcdc52b243a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__organization-chart-three-nodes/20260926T171117Z-thuan-mac-1/reference/organizations_80d19f77-aa43-4744-a812-6dcdc52b243a.svg"
AUTHOR = "gpt-6"
class OrganizationChartThreeNodes(Solo48):
    icon_id="organization-chart-three-nodes"
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="programing"
    aliases=()
    keywords=("organization", "hierarchy", "chart", "tree", "nodes")
    def build(self):
        self.add_polyline("parent",(20,8),(28,8),(28,16),(20,16),closed=True)
        self.add_line("root-stem",(24,16),(24,24))
        self.add_line("bus",(4,24),(44,24))
        for i,x in enumerate((8,24,40)):
            self.add_line(f"child-stem-{i}",(x,24),(x,32))
            self.add_polyline(f"child-{i}",(x-4,32),(x+4,32),(x+4,40),(x-4,40),closed=True)
        for i in range(3):
            self.relate("connect","bus",f"child-stem-{i}")
            self.relate("connect",f"child-stem-{i}",f"child-{i}")
        self.relate("connect","root-stem","parent")
        self.relate("connect","root-stem","bus")
