"""Tapered traffic cone on a wide baseline with two curved stripe divisions. Use shared stripe attachment levels and omit one stripe and the doubled base rim."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed875ea9-e0f3-4ba1-b40a-ead95c60d0b3'
SOURCE_PATH = 'pictographic-primitives/logos/vlc logo_ed875ea9-e0f3-4ba1-b40a-ead95c60d0b3.svg'
AUTHOR = 'gpt-6'

class VlcLogo(Solo48):
    icon_id = 'vlc-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('vlc', 'media-player', 'traffic-cone', 'videolan', 'logo', 'brand', 'video')

    def build(self):
        # Plan: Tapered traffic cone on a wide baseline with two curved stripe divisions. Use shared stripe attachment levels and omit one stripe and the doubled base rim.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_polyline('left',(10,44),(14,28),(18,16),(22,4))
        self.add_line('top',(22,4),(26,4))
        self.add_polyline('right',(26,4),(30,16),(34,28),(38,44))
        self.add_polyline('base',(8,44),(10,44),(38,44),(40,44))
        for a,b in [('left','top'),('top','right'),('right','base'),('base','left')]:self.relate('connect',a,b)
        for j,(a,b,rx) in enumerate([((18,16),(30,16),6),((14,28),(34,28),10)]):
            self.add_arc('stripe-'+str(j),a,b,radius_x=rx,radius_y=2,sweep=False)
            self.relate('connect','stripe-'+str(j),'left');self.relate('connect','stripe-'+str(j),'right')

