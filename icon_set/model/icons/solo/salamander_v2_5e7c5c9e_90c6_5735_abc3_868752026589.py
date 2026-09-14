"""Square envelope; widened the head, centered the eye and opened the tail curl with exact elliptical bounds.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
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
        self.add_arc('head', (8, 16), (26, 16), radius_x=9, radius_y=10, sweep=True)
        self.add_line('back', (26, 16), (26, 27))
        self.add_arc('inner-tail', (26, 27), (34, 27), radius_x=4, radius_y=4, sweep=False)
        self.add_arc('tail-cap', (34, 27), (42, 27), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('tail-round', (42, 27), (31, 42), radius_x=11, radius_y=15, sweep=True)
        self.add_line('tail-base', (31, 42), (26, 42))
        self.add_arc('belly', (26, 42), (8, 25), radius_x=18, radius_y=17, sweep=True)
        self.add_line('neck', (8, 25), (8, 16))
        self.add_contour('body', 'head', 'back', 'inner-tail', 'tail-cap', 'tail-round', 'tail-base', 'belly', 'neck', closed=True)
        self.add_line('foreleg', (8, 16), (6, 19))
        self.relate('connect', 'foreleg', 'body')
        self.add_line('hindleg', (8, 25), (6, 29))
        self.relate('connect', 'hindleg', 'body')
        self.add_dot('eye', (17, 16))
