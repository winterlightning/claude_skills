from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Audio Waveform: Five separate vertical bars form an uneven audio waveform around a common horizontal centre. The middle bar is tallest, with shorter bars on both sides and a very short far-right bar.\n\nConstruction: Four parallel bars in a regular eight-unit series; unequal heights preserve a sound waveform.\nKeyshape: VRECT_XL; extremes follow the SUB32 contract.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f991ef0f-2aa9-4924-9670-c07e3215f3a9'
SOURCE_PATH = 'pictographic-primitives/state/microphone sound_f991ef0f-2aa9-4924-9670-c07e3215f3a9.svg'
AUTHOR = 'gpt-6'

class AudioWaveformVariant2(SourceFaithfulSideSub):
    icon_id = 'audio-waveform-v2'
    variant_of = 'audio-waveform'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('audio', 'waveform', 'five', 'separate', 'vertical', 'bars', 'form', 'uneven')
    keyshape = Keyshape.SQUARE
    canvas_width = 44
    canvas_height = 48

    def build(self):
        """Five waveform bars with the original unequal heights, in their original order."""
        for i, (x, t, b) in enumerate([(2, 18, 30), (12, 10, 38), (22, 2, 46), (32, 14, 34), (42, 22, 26)]):
            self.add_line(f'bar-{i}', (x, t), (x, b))
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub

def box(s, n, l, t, r, b, k=3):
    points = [(l + k, t), (r - k, t), (r, t + k), (r, b - k), (r - k, b), (l + k, b), (l, b - k), (l, t + k)]
    members = []
    for i, p in enumerate(points):
        q = points[(i + 1) % 8]
        name = f'{n}-{i}'
        if i % 2:
            s.add_arc(name, p, q, radius_x=k)
        else:
            s.add_line(name, p, q)
        members.append(name)
    s.add_contour(n, *members, closed=True)

def circle(s, n, cx, cy, r):
    s.add_arc(n + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
    s.add_arc(n + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
    s.add_contour(n, n + '-top', n + '-bottom', closed=True)
