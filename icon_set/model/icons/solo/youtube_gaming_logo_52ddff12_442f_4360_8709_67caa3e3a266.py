"""Angular heart-shaped controller with a left directional cross and two staggered buttons. Share the cross center and reduce button rings to dots."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '52ddff12-442f-4360-8709-67caa3e3a266'
SOURCE_PATH = 'pictographic-primitives/logos/youtube gaming logo_52ddff12-442f-4360-8709-67caa3e3a266.svg'
AUTHOR = 'gpt-6'

class YoutubeGamingLogo(Solo48):
    icon_id = 'youtube-gaming-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('youtube-gaming', 'youtube', 'gaming', 'controller', 'heart', 'logo', 'brand')

    def build(self):
        # Plan: Angular heart-shaped controller with a left directional cross and two staggered buttons. Share the cross center and reduce button rings to dots.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('heart',(6,16),(16,6),(24,12),(32,6),(42,16),(42,28),(24,42),(6,28),closed=True)
        for j,p in enumerate([(15,23),(21,23),(18,20),(18,26)]):self.add_line('pad-'+str(j),(18,23),p)
        for j in range(4):
            for k in range(j+1,4):self.relate('connect','pad-'+str(j),'pad-'+str(k))
        self.add_dot('button-top',(32,18));self.add_dot('button-bottom',(28,27))

