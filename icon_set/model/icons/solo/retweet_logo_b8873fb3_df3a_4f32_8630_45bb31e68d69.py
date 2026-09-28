"""Two opposed right-angle arrows with identical corner radii; Lucide repeat-2 informs the continuous corner construction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8873fb3-df3a-4f32-8630-45bb31e68d69'
SOURCE_PATH = 'pictographic-primitives/logos/retweet logo_b8873fb3-df3a-4f32-8630-45bb31e68d69.svg'
AUTHOR = 'gpt-6'

class RetweetLogo(Solo48):
    icon_id = 'retweet-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('retweet', 'repost', 'share', 'arrows', 'logo', 'brand', 'twitter')

    def build(self):
        # Plan: Two opposed right-angle arrows with identical corner radii; Lucide repeat-2 informs the continuous corner construction.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_line('left',(14,6),(14,34))
        self.add_arc('left-corner',(14,34),(22,42),radius_x=8,sweep=False)
        self.add_contour('up-shaft','left','left-corner')
        self.add_polyline('up-head',(6,14),(14,6),(22,14))
        self.relate('connect','up-shaft','up-head')
        self.add_arc('right-corner',(26,6),(34,14),radius_x=8)
        self.add_line('right',(34,14),(34,42))
        self.add_contour('down-shaft','right-corner','right')
        self.add_polyline('down-head',(26,34),(34,42),(42,34))
        self.relate('connect','down-shaft','down-head')

