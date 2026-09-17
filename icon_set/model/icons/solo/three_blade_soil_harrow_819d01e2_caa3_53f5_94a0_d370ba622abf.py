"""Agriculture Soil Harrow Tool.
Plan: Three repeating curved blades under beam with raised mounting plate. Extrema (4,8)-(44,40).
Reference: Original source silhouette; Lucide geometric construction with shared joints and coherent curves.
Reduction: Thin beam thickness and mounting mark omitted; three blades and rounded mounting plate retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '819d01e2-caa3-53f5-94a0-d370ba622abf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/plow_819d01e2-caa3-53f5-94a0-d370ba622abf.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'three-blade-soil-harrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('agriculture', 'soil', 'harrow', 'tool')

    def build(self):

        self.add_polyline('beam',(4,24),(8,24),(16,24),(24,24),(32,24),(40,24),(44,24))
        self.add_polyline('mount',(16,24),(16,16))
        self.add_arc('mount-top',(16,16),(32,16),radius_x=8)
        self.add_line('mount-right',(32,16),(32,24))
        self.relate('connect','mount','mount-top');self.relate('connect','mount-top','mount-right')
        self.relate('connect','beam','mount');self.relate('connect','beam','mount-right')
        for i,x in enumerate((8,24,40)):
            self.add_bezier(f'blade-{i}',(x,24),((x,32),(x-2,37),(x+4,40)))
            self.relate('connect','beam',f'blade-{i}')
