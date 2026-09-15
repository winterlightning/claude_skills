"""Balanced hexagonal brand badge with a single centered play triangle. Reduce source rounding to clean joined polygon corners."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '367a0228-f7a0-43a7-9f81-ed2546ce3170'
SOURCE_PATH = 'pictographic-primitives/logos/runkit logo_367a0228-f7a0-43a7-9f81-ed2546ce3170.svg'
AUTHOR = 'gpt-6'

class RunkitLogo(Solo48):
    icon_id = 'runkit-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('runkit', 'javascript', 'notebook', 'play', 'logo', 'brand', 'developer')

    def build(self):
        # Plan: Balanced hexagonal brand badge with a single centered play triangle. Reduce source rounding to clean joined polygon corners.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('hexagon',(24,6),(42,16),(42,32),(24,42),(6,32),(6,16),closed=True)
        self.add_polyline('play',(20,18),(30,24),(20,30),closed=True)

