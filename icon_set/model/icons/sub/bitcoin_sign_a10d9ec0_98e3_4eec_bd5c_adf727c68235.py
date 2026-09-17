"""Bitcoin Sign: An uppercase B-shaped bitcoin glyph has two rounded bowls and paired short vertical strokes projecting above and below it. Generate this component alone; exclude Circle Frame.

Construction: A B-shaped outline has paired short stems above and below, retaining the source currency details.
Keyshape: VRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a10d9ec0-98e3-4eec-bd5c-adf727c68235'
SOURCE_PATH = 'pictographic-primitives/state/crypto_a10d9ec0-98e3-4eec-bd5c-adf727c68235.svg'
AUTHOR = 'gpt-6'


class BitcoinSign(Sub32):
    icon_id = 'bitcoin-sign'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('bitcoin', 'sign', 'uppercase', 'b', 'shaped', 'glyph', 'rounded', 'bowls')

    def build(self):
        self.add_line('stem',(6,6),(6,26))
        self.add_line('upper-top',(4,6),(18,6))
        self.add_arc('upper-bowl',(18,6),(18,16),radius_x=10,radius_y=5)
        self.add_line('middle',(18,16),(6,16))
        self.add_contour('upper','upper-top','upper-bowl','middle')
        self.add_line('lower-top',(6,16),(18,16))
        self.add_arc('lower-bowl',(18,16),(18,26),radius_x=10,radius_y=5)
        self.add_line('lower-bottom',(18,26),(4,26))
        self.add_contour('lower','lower-top','lower-bowl','lower-bottom')
        self.relate('connect','stem','upper')
        self.relate('connect','stem','lower')
        self.relate('connect','upper','lower')
        for x in (10,18):
            self.add_line(f'top-{x}',(x,2),(x,6))
            self.add_line(f'bottom-{x}',(x,26),(x,30))
            self.relate('connect','upper',f'top-{x}')
            self.relate('connect','lower',f'bottom-{x}')
