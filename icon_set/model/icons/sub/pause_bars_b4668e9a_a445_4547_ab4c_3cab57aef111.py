"""Pause Bars: Two separate equal vertical strokes stand parallel with a clear gap between them. Generate this component alone; exclude Phone Frame.

Construction: Two identical parallel vertical strokes retain the source pause spacing.
Keyshape: VRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH = 'pictographic-primitives/state/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'
AUTHOR = 'gpt-6'


class PauseBars(Sub32):
    icon_id = 'pause-bars'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('pause', 'bars', 'separate', 'equal', 'vertical', 'strokes', 'stand', 'parallel')

    def build(self):
        for x in (10,22):self.add_line(f'bar-{x}',(x,2),(x,30))
