"""Mountain Peaks: Two pointed mountain peaks form one continuous zigzag above a shared baseline, with the right peak slightly taller. Generate this component alone; exclude Rectangle Frame.

Construction: Two unequal mountain peaks and the baseline reproduce the source closed ridge.
Keyshape: HRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '00bf1033-7ed9-48a1-92ef-7122ca973175'
SOURCE_PATH = 'pictographic-primitives/state/two image_00bf1033-7ed9-48a1-92ef-7122ca973175.svg'
AUTHOR = 'gpt-6'


class MountainPeaks(Sub32):
    icon_id = 'mountain-peaks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('mountain', 'peaks', 'pointed', 'form', 'continuous', 'zigzag', 'shared', 'baseline')

    def build(self):
        self.add_polyline('mountains',(2,26),(9,10),(16,22),(23,6),(30,26),closed=True)
