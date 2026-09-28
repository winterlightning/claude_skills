"""Three rising signal arcs over a small dome, all sharing x=24. Use a taller envelope with ten-unit spacing between wave crests, preserving the broad base dome while reducing its double outline to one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53941f4a-fd75-44ae-8054-37c839d1aa98'
SOURCE_PATH = 'pictographic-primitives/logos/spotify logo_53941f4a-fd75-44ae-8054-37c839d1aa98.svg'
AUTHOR = 'gpt-6'

class SpotifyWavesLogo(Solo48):
    icon_id = 'spotify-waves-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('spotify', 'music', 'waves', 'signal', 'logo', 'brand', 'audio')

    def build(self):
        # Plan: Three rising signal arcs over a small dome, all sharing x=24. Use a taller envelope with ten-unit spacing between wave crests, preserving the broad base dome while reducing its double outline to one stroke.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        for j,(rx,ry,y) in enumerate([(16,4,8),(12,4,18),(8,4,28),(12,9,44)]):
            self.add_arc('wave-'+str(j),(24-rx,y),(24+rx,y),radius_x=rx,radius_y=ry)

