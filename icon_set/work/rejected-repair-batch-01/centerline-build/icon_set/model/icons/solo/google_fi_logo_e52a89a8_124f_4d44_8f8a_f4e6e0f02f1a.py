"""A long rounded bar spans the top above a stubby F at the lower left and a tall rounded i bar at the lower right.

Plan: Horizontal capsule above F and i; same 8-unit bar width and integer radii.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: No useful exact logo match; geometric capsule and joined letter strokes.
Simplification: F and i outlined bars become single strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e52a89a8-124f-4d44-8f8a-f4e6e0f02f1a'
SOURCE_PATH = 'pictographic-primitives/logos/google fi logo_e52a89a8-124f-4d44-8f8a-f4e6e0f02f1a.svg'
AUTHOR = 'gpt-6'


class GoogleFiLogo(Solo48):
    icon_id = 'google-fi-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-fi', 'google', 'mobile', 'carrier', 'logo', 'brand', 'wireless')

    def build(self):
        self.add_line('bar-top',(10,6),(38,6))
        self.add_arc('bar-right',(38,6),(38,14),radius_x=4)
        self.add_line('bar-bottom',(38,14),(10,14))
        self.add_arc('bar-left',(10,14),(10,6),radius_x=4)
        self.add_contour('top-bar','bar-top','bar-right','bar-bottom','bar-left',closed=True)
        self.add_polyline('f',(6,42),(6,33),(6,24),(22,24))
        self.add_line('f-middle',(6,33),(18,33))
        self.relate('connect','f','f-middle')
        self.add_line('i',(38,24),(38,42))
