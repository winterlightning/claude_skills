"""Squared C silhouette enclosing one detached horizontal block, reduced to a stroke. Preserve the nested squared E construction with integer parallel offsets."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78a72000-1201-4a99-a591-9d9e0be2b7c8'
SOURCE_PATH = 'pictographic-primitives/logos/square enix logo_78a72000-1201-4a99-a591-9d9e0be2b7c8.svg'
AUTHOR = 'gpt-6'

class SquareEnixLogo(Solo48):
    icon_id = 'square-enix-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('square-enix', 'gaming', 'publisher', 'letter-e', 'logo', 'brand', 'japanese')

    def build(self):
        # Plan: Squared C silhouette enclosing one detached horizontal block, reduced to a stroke. Preserve the nested squared E construction with integer parallel offsets.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('c',(6,6),(42,6),(42,14),(16,14),(16,34),(42,34),(42,42),(6,42),closed=True)
        self.add_line('block',(26,24),(36,24))

