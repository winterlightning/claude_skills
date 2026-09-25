"""TM Text: The uppercase letters TM sit side by side, with a broad crossbar on the T and two softly rounded peaks on the M. Generate this component alone; exclude Circle Frame.

Construction: A short T is followed by the source sloping-stem M; the horizontal profile keeps both letters readable with open spacing.
Keyshape: HRECT_S; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0f425c8c-5acb-4425-9800-ca04332f5010'
SOURCE_PATH = 'pictographic-primitives/state/circle tm_0f425c8c-5acb-4425-9800-ca04332f5010.svg'
AUTHOR = 'gpt-6'


class TmText(Sub32):
    icon_id = 'tm-text'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('tm', 'text', 'uppercase', 'letters', 'sit', 'side', 'broad', 'crossbar')

    def build(self):
        self.add_line('t-top',(2,10),(10,10))
        self.add_line('t-stem',(6,10),(6,22))
        self.relate('connect','t-top','t-stem')
        self.add_polyline('m',(16,22),(18,10),(23,20),(28,10),(30,22))
