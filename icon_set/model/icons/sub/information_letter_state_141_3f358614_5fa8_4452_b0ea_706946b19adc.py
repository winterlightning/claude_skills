"""Information Letter: A lowercase i has a tiny detached dot above a vertical stem with a leftward upper serif and a broad lower foot. Generate this component alone; exclude Circle Frame.

Construction: The dot, leftward upper serif, upright and bottom foot retain the source lowercase i.
Keyshape: VRECT_S; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '3f358614-5fa8-4452-b0ea-706946b19adc'
SOURCE_PATH = 'pictographic-primitives/state/information_3f358614-5fa8-4452-b0ea-706946b19adc.svg'
AUTHOR = 'gpt-6'


class InformationLetterState141(Sub32):
    icon_id = 'information-letter-state-141'
    keyshape = Keyshape.VRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('information', 'letter', 'lowercase', 'i', 'tiny', 'detached', 'dot', 'vertical')

    def build(self):
        self.add_dot('dot',(16,2))
        self.add_polyline('stem',(10,12),(16,12),(16,30))
        self.add_line('foot',(10,30),(22,30))
        self.relate('connect','stem','foot')
