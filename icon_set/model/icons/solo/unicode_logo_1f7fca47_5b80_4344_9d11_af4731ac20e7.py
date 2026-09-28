"""Joined UN monogram using one shared upright. Omit the enclosing square to preserve both letters with open counters."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f7fca47-5b80-4344-9d11-af4731ac20e7'
SOURCE_PATH = 'pictographic-primitives/logos/unicode logo_1f7fca47-5b80-4344-9d11-af4731ac20e7.svg'
AUTHOR = 'gpt-6'

class UnicodeLogo(Solo48):
    icon_id = 'unicode-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('unicode', 'characters', 'text', 'un', 'logo', 'brand', 'standard')

    def build(self):
        # Plan: Joined UN monogram using one shared upright. Omit the enclosing square to preserve both letters with open counters.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_line('u-left',(6,6),(6,33));self.add_arc('u-bend',(6,33),(24,33),radius_x=9,sweep=False)
        self.add_polyline('shared',(24,33),(24,6),(42,42),(42,6))
        self.relate('connect','u-left','u-bend');self.relate('connect','u-bend','shared')

