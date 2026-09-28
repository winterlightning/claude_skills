"""Rounded square with a square lower-right corner encloses the winking punctuation face. Reduce the dot ring to a dot and preserve the short comma and curved parenthesis."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '590274ee-e371-4017-a4ff-3b25e6e3ad50'
SOURCE_PATH = 'pictographic-primitives/logos/tuenti logo_590274ee-e371-4017-a4ff-3b25e6e3ad50.svg'
AUTHOR = 'gpt-6'

class TuentiLogo(Solo48):
    icon_id = 'tuenti-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('tuenti', 'social', 'winking-face', 'logo', 'brand', 'spanish', 'smiley')

    def build(self):
        # Plan: Rounded square with a square lower-right corner encloses the winking punctuation face. Reduce the dot ring to a dot and preserve the short comma and curved parenthesis.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_line('top',(16,6),(32,6));self.add_arc('tr',(32,6),(42,16),radius_x=10)
        self.add_polyline('right',(42,16),(42,42),(16,42))
        self.add_arc('bl',(16,42),(6,32),radius_x=10);self.add_line('left',(6,32),(6,16));self.add_arc('tl',(6,16),(16,6),radius_x=10)
        self.relate('connect','top','tr');self.relate('connect','tr','right');self.relate('connect','right','bl');self.relate('connect','bl','left');self.relate('connect','left','tl');self.relate('connect','tl','top')
        self.add_dot('dot',(17,17));self.add_line('comma',(18,28),(16,32))
        self.add_bezier('smile',(29,16),((34,22),(34,26),(29,32)))

