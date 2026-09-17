"""Signal Waves: Two detached nested quarter-circle arcs expand upward and right. Generate this component alone; exclude Telephone Handset.

Construction: Two nested quarter-circle signal arcs preserve the original upward-right orientation.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '75f76bb5-f6c5-4feb-80ea-54e38ec9dbe4'
SOURCE_PATH = 'pictographic-primitives/state/phone with electric waves_75f76bb5-f6c5-4feb-80ea-54e38ec9dbe4.svg'
AUTHOR = 'gpt-6'


class SignalWaves(Sub32):
    icon_id = 'signal-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('signal', 'waves', 'detached', 'nested', 'quarter', 'circle', 'arcs', 'expand')

    def build(self):
        self.add_arc('outer',(2,2),(30,30),radius_x=28)
        self.add_arc('inner',(2,16),(16,30),radius_x=14)
