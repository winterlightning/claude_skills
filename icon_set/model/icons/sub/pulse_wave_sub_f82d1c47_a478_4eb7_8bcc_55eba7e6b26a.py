"""Pulse Wave: A continuous line begins horizontally, rises into a pointed peak, plunges into a deep trough, and returns to a short horizontal ending. Generate this component alone; exclude Magnifying Glass Frame.

Construction: A single pulse waveform joins level terminals, a peak and a trough; magnifier excluded.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f82d1c47-a478-4eb7-8bcc-55eba7e6b26a'
SOURCE_PATH = 'pictographic-primitives/state/magnifying glass with a wave_f82d1c47-a478-4eb7-8bcc-55eba7e6b26a.svg'
AUTHOR = 'gpt-6'


class PulseWaveSub(Sub32):
    icon_id = 'pulse-wave-sub'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('pulse', 'wave', 'continuous', 'line', 'begins', 'horizontally', 'rises', 'pointed')

    def build(self):
        self.add_polyline("pulse",(2,16),(8,16),(13,4),(21,28),(26,16),(30,16))
