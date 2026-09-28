"""Power Sign: A broad circular arc has a clear opening at the top and a separate vertical stroke centred in that opening. The stroke extends down toward the circle's centre.

Construction: A top-open round arc remains separate from its upright power stroke.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5783646c-bee0-4bc8-8bf2-60ad9a4b7d66'
SOURCE_PATH = 'pictographic-primitives/state/power_5783646c-bee0-4bc8-8bf2-60ad9a4b7d66.svg'
AUTHOR = 'gpt-6'


class PowerSignState215(Sub32):
    icon_id = 'power-sign-state-215'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('power', 'sign', 'broad', 'circular', 'arc', 'clear', 'opening', 'top')

    def build(self):
        self.add_arc("left-top",(5,7),(2,16),radius_x=15,sweep=False)
        self.add_arc("bottom",(2,16),(30,16),radius_x=14,sweep=False)
        self.add_arc("right-top",(30,16),(27,7),radius_x=15,sweep=False)
        self.add_contour("ring","left-top","bottom","right-top")
        self.add_line("stem",(16,2),(16,14))
