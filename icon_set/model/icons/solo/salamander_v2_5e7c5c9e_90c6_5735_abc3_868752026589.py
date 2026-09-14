from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5e7c5c9e-90c6-5735-abc3-868752026589'
SOURCE_PATH = 'pictographic-primitives/animals/amphibian chameleon_5e7c5c9e-90c6-5735-abc3-868752026589.svg'
AUTHOR = 'gpt-6'

class SalamanderVariant2(Solo48):
    icon_id = 'salamander-v2'
    variant_of = 'salamander'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('salamander', 'amphibian', 'newt', 'lizard', 'tail', 'animal', 'wildlife', 'reptile')

    def build(self) -> None:
        self.add_arc('head', (8, 16), (24, 16), radius_x=8, radius_y=10, sweep=True)
        self.add_line('back', (24, 16), (24, 33))
        self.add_arc('inner-tail', (24, 33), (34, 33), radius_x=5, radius_y=5, sweep=False)
        self.add_line('tail-rise', (34, 33), (34, 28))
        self.add_arc('tail-cap', (34, 28), (42, 28), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('tail-round', (42, 28), (31, 42), radius_x=11, radius_y=14, sweep=True)
        self.add_line('tail-base', (31, 42), (26, 42))
        self.add_arc('belly', (26, 42), (8, 25), radius_x=18, radius_y=17, sweep=True)
        self.add_line('neck', (8, 25), (8, 16))
        self.add_contour('body', 'head', 'back', 'inner-tail', 'tail-rise', 'tail-cap', 'tail-round', 'tail-base', 'belly', 'neck', closed=True)
        self.add_line('foreleg', (8, 16), (6, 19))
        self.relate('connect', 'foreleg', 'body')
        self.add_line('hindleg', (8, 25), (6, 29))
        self.relate('connect', 'hindleg', 'body')
        self.add_dot('eye', (16, 16))
