"""Audio Waveform: Five separate vertical bars form an uneven audio waveform around a common horizontal centre. The middle bar is tallest, with shorter bars on both sides and a very short far-right bar.

Construction: Four parallel bars in a regular eight-unit series; unequal heights preserve a sound waveform.
Keyshape: VRECT_XL; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f991ef0f-2aa9-4924-9670-c07e3215f3a9'
SOURCE_PATH = 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'
AUTHOR = 'gpt-6'


class AudioWaveform(Sub32):
    icon_id = 'audio-waveform'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    aliases = ()
    keywords = ('audio', 'waveform', 'five', 'separate', 'vertical', 'bars', 'form', 'uneven')

    def build(self):
        for i,(top,bottom) in enumerate(((11,21),(5,27),(2,30),(9,23))):
            x=4+8*i
            self.add_line(f"bar-{i}",(x,top),(x,bottom))
