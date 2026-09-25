"""Flowing standalone S monogram; retain the oversized script initial and omit the cramped ass suffix. Intentional asymmetric sweep follows the supplied script, using coherent tangent-continuous cubics."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '393d0fe7-3e20-45f3-afa0-6a6ea66ebba3'
SOURCE_PATH = 'pictographic-primitives/logos/sass logo_393d0fe7-3e20-45f3-afa0-6a6ea66ebba3.svg'
AUTHOR = 'gpt-6'

class SassLogo(Solo48):
    icon_id = 'sass-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('sass', 'css', 'script', 'wordmark', 'logo', 'brand', 'developer')

    def build(self):
        # Plan: Flowing standalone S monogram; retain the oversized script initial and omit the cramped ass suffix. Intentional asymmetric sweep follows the supplied script, using coherent tangent-continuous cubics.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_bezier('script-s',(42,10),((42,6),(34,6),(28,6)),((16,6),(8,14),(8,20)),((8,26),(34,26),(34,34)),((34,40),(24,42),(18,42)),((12,42),(8,40),(6,36)))

