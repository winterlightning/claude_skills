"""Four diamonds in the source two-one-one arrangement. Share a six-unit diamond radius; preserve the touching lower pair and enlarge the bottom diamond so its counter remains open."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e697ec7-0492-4216-9590-fa65c0e1adad'
SOURCE_PATH = 'pictographic-primitives/logos/tidal music logo_4e697ec7-0492-4216-9590-fa65c0e1adad.svg'
AUTHOR = 'gpt-6'

class TidalLogo(Solo48):
    icon_id = 'tidal-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('tidal', 'music', 'streaming', 'diamonds', 'logo', 'brand', 'audio')

    def build(self):
        # Plan: Four diamonds in the source two-one-one arrangement. Share a six-unit diamond radius; preserve the touching lower pair and enlarge the bottom diamond so its counter remains open.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        for j,(x,y) in enumerate([(14,10),(34,10),(24,26),(24,38)]):self.add_polyline('diamond-'+str(j),(x,y-6),(x+6,y),(x,y+6),(x-6,y),closed=True)
        self.relate('connect','diamond-2','diamond-3')

