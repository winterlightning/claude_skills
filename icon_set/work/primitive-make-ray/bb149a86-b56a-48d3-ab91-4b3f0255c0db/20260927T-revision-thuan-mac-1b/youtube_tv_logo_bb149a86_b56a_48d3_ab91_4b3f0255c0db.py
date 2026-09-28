"""Rounded screen enclosing a play triangle above a separate stand line. Use a taller keyshape to preserve a legal play counter and stand spacing."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bb149a86-b56a-48d3-ab91-4b3f0255c0db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__youtube-tv-logo/20260927T145855Z-thuan-mac-1/reference/youtube tv logo_bb149a86-b56a-48d3-ab91-4b3f0255c0db.svg'
AUTHOR = "gpt-6"

class YoutubeTvLogo(Solo48):
    icon_id = 'youtube-tv-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('youtube-tv', 'youtube', 'television', 'play', 'streaming', 'logo', 'brand')

    def build(self):
        # Plan: Rounded screen enclosing a play triangle above a separate stand line. Use a taller keyshape to preserve a legal play counter and stand spacing.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        for j,(a,b,c) in enumerate([((10,6),(38,6),(42,10)),((42,10),(42,30),(38,34)),((38,34),(10,34),(6,30)),((6,30),(6,10),(10,6))]):
            self.add_line('edge-'+str(j),a,b);self.add_arc('corner-'+str(j),b,c,radius_x=4)
        self.add_contour('screen',*[x for j in range(4) for x in ('edge-'+str(j),'corner-'+str(j))],closed=True)
        self.add_polyline('play',(18,16),(30,20),(18,26),closed=True)
        self.add_line('stand',(14,42),(34,42))

