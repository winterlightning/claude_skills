"""Gift box following user reference: broad bow on lid, empty box face.
SQUARE visible extremes (0,0)-(64,64), native 4-unit stroke.
User clipboard b296dcc9-5ef6-4656-8612-b557f0b5702d is the visual reference.
Lucide gift informs geometric construction. Bow bases share the lid edge
without duplicate strokes. The plain lid is eight units high on centerlines.
Paired symbols measured separately; native 32 does not fit. 24-unit prototypes are measured separately.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = 'c08ff3f4-e21c-4658-a232-539f6251d633'
SOURCE_PATH = 'pictographic-primitives/rewards/gift box_c08ff3f4-e21c-4658-a232-539f6251d633.svg'
AUTHOR = 'gpt-6'

class GiftBoxContainer(Container64):
    icon_id = 'gift-box-container'
    category = 'rewards'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('gift', 'box', 'container')

    def build(self):
        path(self, 'lid', (14, 20), [('L', (6, 20)), ('A', (2, 24), 4, 4, False), ('A', (6, 28), 4, 4, False), ('L', (58, 28)), ('A', (62, 24), 4, 4, False), ('A', (58, 20), 4, 4, False), ('L', (50, 20))])
        path(self, 'box', (6, 28), [('L', (6, 56)), ('A', (12, 62), 6, 6, False), ('L', (52, 62)), ('A', (58, 56), 6, 6, False), ('L', (58, 28))])
        self.relate('connect', 'box', 'lid')
        for side in (-1, 1):

            def p(x, y):
                return (32 + side * x, y)
            path(self, f'bow-{side}', p(0, 20), [('A', p(18, 2), 18, 18, side > 0), ('A', p(18, 20), 9, 9, side > 0), ('L', p(0, 20))], True)
            self.relate('connect', f'bow-{side}', 'lid')
        self.relate('connect', 'bow--1', 'bow-1')
