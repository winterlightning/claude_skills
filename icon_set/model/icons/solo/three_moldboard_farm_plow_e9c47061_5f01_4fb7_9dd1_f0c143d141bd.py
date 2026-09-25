"""Agricultural Farm Plow.
Plan: Three equal curved moldboards below a shared beam; triangular brace above. Extrema (4,8)-(44,40).
Reference: Original source silhouette; Lucide geometric construction with shared joints and coherent curves.
Reduction: Moldboard double outlines reduced to three coherent curved blades; narrow beam thickness removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9c47061-5f01-4fb7-9dd1-f0c143d141bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/plowing_e9c47061-5f01-4fb7-9dd1-f0c143d141bd.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'three-moldboard-farm-plow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('agricultural', 'farm', 'plow')

    def build(self):

        self.add_polyline('beam',(4,24),(10,24),(24,24),(38,24),(44,24))
        self.add_polyline('mount',(10,24),(10,16),(38,8),(38,24));self.relate('connect','beam','mount')
        for i,x in enumerate((10,24,38)):
            self.add_bezier(f'blade-{i}',(x,24),((x-6,30),(x-6,38),(x+4,40)))
            self.relate('connect','beam',f'blade-{i}')
