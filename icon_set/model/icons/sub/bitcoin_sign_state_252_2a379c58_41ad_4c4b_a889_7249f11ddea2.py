"""Bitcoin Sign: An uppercase B has two rounded bowls and two short parallel stems projecting above and below. Generate this component alone; exclude Shield Frame.

Construction: The source B currency glyph retains both upper and lower pairs of projecting stems.
Keyshape: VRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2a379c58-41ad-4c4b-a889-7249f11ddea2'
SOURCE_PATH = 'pictographic-primitives/state/shield bitcoin_2a379c58-41ad-4c4b-a889-7249f11ddea2.svg'
AUTHOR = 'gpt-6'


class BitcoinSignState252(Sub32):
    icon_id = 'bitcoin-sign-state-252'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('bitcoin', 'sign', 'uppercase', 'b', 'rounded', 'bowls', 'short', 'parallel')

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
