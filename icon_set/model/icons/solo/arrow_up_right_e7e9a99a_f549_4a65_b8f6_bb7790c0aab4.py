"""A standalone arrow points diagonally up and right, as the saved solo brief requests.
SQUARE gives equal horizontal/vertical travel. Head arms share one length and
meet the shaft at the same endpoint. Source contributes the long shaft and
short head arms; Lucide arrow-up-right supplies the continuous head contour.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7e9a99a-f549-4a65-b8f6-bb7790c0aab4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/keyboard arrow top right_e7e9a99a-f549-4a65-b8f6-bb7790c0aab4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-top-right-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Arrow Up Right', 'Diagonal Top Right Arrow')
    keywords = ('arrow','diagonal','up','right','direction','keyboard','navigation')

    def build(self):
        tip = (42,6)
        arm = 16
        self.add_polyline('head',(tip[0]-arm,tip[1]),tip,(tip[0],tip[1]+arm))
        self.add_line('shaft',(6,42),tip)
        self.relate('connect','head','shaft')
