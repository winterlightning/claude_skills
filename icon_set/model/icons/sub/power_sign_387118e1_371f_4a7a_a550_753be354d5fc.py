"""Power Sign: An almost complete circular arc opens at the top around a detached upright stroke. The central stroke descends from above the arc into its upper interior.

Construction: Circular lower power arc with exact side and bottom extrema; detached vertical stem.
Keyshape: SQUARE; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '387118e1-371f-4a7a-a550-753be354d5fc'
SOURCE_PATH = 'pictographic-primitives/state/power_387118e1-371f-4a7a-a550-753be354d5fc.svg'
AUTHOR = 'gpt-6'


class PowerSign(Sub32):
    icon_id = 'power-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    categories = ("state",)
    aliases = ()
    keywords = ('power', 'sign', 'almost', 'complete', 'circular', 'arc', 'opens', 'top')

    def build(self):
        self.add_arc("left-top",(5,7),(2,16),radius_x=15,sweep=False)
        self.add_arc("bottom",(2,16),(30,16),radius_x=14,sweep=False)
        self.add_arc("right-top",(30,16),(27,7),radius_x=15,sweep=False)
        self.add_contour("ring","left-top","bottom","right-top")
        self.add_line("stem",(16,2),(16,14))
