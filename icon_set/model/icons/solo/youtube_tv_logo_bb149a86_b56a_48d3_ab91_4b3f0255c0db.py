"""Rounded screen enclosing a play triangle above a separate stand line. Use a taller keyshape to preserve a legal play counter and stand spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb149a86-b56a-48d3-ab91-4b3f0255c0db'
SOURCE_PATH = 'pictographic-primitives/logos/youtube tv logo_bb149a86-b56a-48d3-ab91-4b3f0255c0db.svg'
AUTHOR = 'gpt-6'

class YoutubeTvLogo(Solo48):
    icon_id = 'youtube-tv-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('youtube-tv', 'youtube', 'television', 'play', 'streaming', 'logo', 'brand')

    def build(self):
        # Plan: Rounded screen enclosing a play triangle above a separate stand line. Use a taller keyshape to preserve a legal play counter and stand spacing.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        for j,(a,b,c) in enumerate([((12,4),(36,4),(40,8)),((40,8),(40,28),(36,32)),((36,32),(12,32),(8,28)),((8,28),(8,8),(12,4))]):
            self.add_line('edge-'+str(j),a,b);self.add_arc('corner-'+str(j),b,c,radius_x=4)
        self.add_contour('screen',*[x for j in range(4) for x in ('edge-'+str(j),'corner-'+str(j))],closed=True)
        self.add_polyline('play',(20,13),(30,18),(20,23),closed=True)
        self.add_line('stand',(16,44),(32,44))

