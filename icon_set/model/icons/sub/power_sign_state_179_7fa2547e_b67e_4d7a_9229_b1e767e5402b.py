"""Power Sign: A circular arc remains open at the top, where a detached vertical stroke descends into its centre. Generate this component alone; exclude Phone Frame.

Construction: The top-open power ring and detached upright preserve the source control glyph.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '7fa2547e-b67e-4d7a-9229-b1e767e5402b'
SOURCE_PATH = 'pictographic-primitives/state/mobile phone control power_7fa2547e-b67e-4d7a-9229-b1e767e5402b.svg'
AUTHOR = 'gpt-6'


class PowerSignState179(Sub32):
    icon_id = 'power-sign-state-179'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('power', 'sign', 'circular', 'arc', 'remains', 'open', 'top', 'where')

    def build(self):
        self.add_arc("left-top",(5,7),(2,16),radius_x=15,sweep=False)
        self.add_arc("bottom",(2,16),(30,16),radius_x=14,sweep=False)
        self.add_arc("right-top",(30,16),(27,7),radius_x=15,sweep=False)
        self.add_contour("ring","left-top","bottom","right-top")
        self.add_line("stem",(16,2),(16,14))
