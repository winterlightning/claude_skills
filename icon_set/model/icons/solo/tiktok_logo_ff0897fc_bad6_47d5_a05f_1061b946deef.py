"""Round note head, upright stem and a sweeping flag. Reduce the thick outlined ribbon to one stroke; keep this source independently identified."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff0897fc-bad6-47d5-a05f-1061b946deef'
SOURCE_PATH = 'pictographic-primitives/logos/tiktok logo_ff0897fc-bad6-47d5-a05f-1061b946deef.svg'
AUTHOR = 'gpt-6'

class TiktokLogo(Solo48):
    icon_id = 'tiktok-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('tiktok', 'video', 'music-note', 'social', 'logo', 'brand', 'short-video')

    def build(self):
        # Plan: Round note head, upright stem and a sweeping flag. Reduce the thick outlined ribbon to one stroke; keep this source independently identified.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_arc('head-top',(8,34),(28,34),radius_x=10)
        self.add_arc('head-bottom',(28,34),(8,34),radius_x=10)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('stem',(28,34),(28,4))
        self.add_bezier('flag',(28,4),((28,12),(34,18),(40,18)))
        self.add_contour('staff','stem','flag');self.relate('connect','head','staff')

