"""Lowercase t with a broad crossbar and curled lower terminal. Reduce the thick outline to a coherent monoline stem and true crossbar junction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b338d5da-6ce4-482a-87f6-e354f8f9155d'
SOURCE_PATH = 'pictographic-primitives/logos/tumblr logo_b338d5da-6ce4-482a-87f6-e354f8f9155d.svg'
AUTHOR = 'gpt-6'

class TumblrLogo(Solo48):
    icon_id = 'tumblr-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('tumblr', 'blog', 'letter-t', 'social', 'logo', 'brand', 'microblog')

    def build(self):
        # Plan: Lowercase t with a broad crossbar and curled lower terminal. Reduce the thick outline to a coherent monoline stem and true crossbar junction.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_polyline('crossbar',(8,17),(24,17),(40,17))
        self.add_line('upper-stem',(24,4),(24,17));self.add_line('lower-stem',(24,17),(24,34))
        self.add_bezier('tail',(24,34),((24,40),(27,44),(32,44)),((35,44),(38,42),(40,40)))
        self.relate('connect','crossbar','upper-stem');self.relate('connect','crossbar','lower-stem');self.relate('connect','upper-stem','lower-stem');self.relate('connect','lower-stem','tail')

