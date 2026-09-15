'Cobra profile: retain flared hood and raised head, broadening the head vertically for a distinct eye without stretching the whole snake.'
# Variant of cobra-head; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '722cb33f-03cc-5935-ab1a-86a1ade0a234'
SOURCE_PATH = 'pictographic-primitives/animals/cobra head side_722cb33f-03cc-5935-ab1a-86a1ade0a234.svg'
AUTHOR = 'gpt-6'

class CobraHead(Solo48):
    icon_id = 'cobra-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('cobra', 'snake', 'hood', 'reptile', 'serpent', 'venom', 'head', 'profile')

    def build(self) -> None:
        self.add_line('neck-back',(16,42),(16,37))
        self.add_bezier('hood',(16,37),((9,34),(6,29),(6,23)),((6,12),(14,6),(24,6)))
        self.add_bezier('crown',(24,6),((31,6),(38,7),(42,11)))
        self.add_bezier('snout',(42,11),((42,18),(39,24),(33,24)))
        self.add_line('jaw',(33,24),(29,24))
        self.add_bezier('throat',(29,24),((22,24),(23,31),(29,42)))
        self.add_line('base',(29,42),(16,42))
        self.add_contour('outline','neck-back','hood','crown','snout','jaw','throat','base',closed=True)
        self.add_dot('eye',(28,15))
