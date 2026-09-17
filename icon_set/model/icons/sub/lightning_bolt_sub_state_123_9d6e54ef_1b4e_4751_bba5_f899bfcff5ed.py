"""Lightning Bolt: An angular lightning stroke forms a sharp zigzag beneath the wrench. Generate this component alone; exclude Wrench.

Construction: A single open zigzag is isolated from the wrench, preserving the source sloping arms.
Keyshape: VRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9d6e54ef-1b4e-4751-bba5-f899bfcff5ed'
SOURCE_PATH = 'pictographic-primitives/state/flash wrench_9d6e54ef-1b4e-4751-bba5-f899bfcff5ed.svg'
AUTHOR = 'gpt-6'


class LightningBoltSubState123(Sub32):
    icon_id = 'lightning-bolt-sub-state-123'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('lightning', 'bolt', 'angular', 'stroke', 'forms', 'sharp', 'zigzag', 'beneath')

    def build(self):
        self.add_polyline('bolt',(24,2),(6,18),(26,12),(10,30))
