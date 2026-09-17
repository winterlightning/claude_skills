"""Target Ticks: Three short crosshair ticks point inward from the top, left and right. Generate this component alone; exclude User Bust.

Construction: Three inward-facing target ticks retain the upper and two side positions.
Keyshape: HRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9517d6fa-de42-443e-9aa6-8980c740b291'
SOURCE_PATH = 'pictographic-primitives/state/user target_9517d6fa-de42-443e-9aa6-8980c740b291.svg'
AUTHOR = 'gpt-6'


class TargetTicks(Sub32):
    icon_id = 'target-ticks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('target', 'ticks', 'short', 'crosshair', 'point', 'inward', 'top', 'left')

    def build(self):
        self.add_line('top',(16,6),(16,14))
        self.add_line('left',(2,26),(10,26))
        self.add_line('right',(22,26),(30,26))
