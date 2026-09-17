"""Sound Waves: Two detached curved sound waves expand toward the right. Generate this component alone; exclude Earbud.

Construction: Two rightward bowed half ellipses, wider for the outer wave.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'cd4e700a-5d5e-4752-8cea-1bc976043740'
SOURCE_PATH = 'pictographic-primitives/state/airpod wave forward_cd4e700a-5d5e-4752-8cea-1bc976043740.svg'
AUTHOR = 'gpt-6'


class SoundWaves(Sub32):
    icon_id = 'sound-waves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('sound', 'waves', 'detached', 'curved', 'expand', 'toward', 'right')

    def build(self):
        self.add_arc('outer',(14,2),(14,30),radius_x=12,radius_y=14)
        self.add_arc('inner',(6,10),(6,22),radius_x=4,radius_y=6)
