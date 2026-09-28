"""Detached diamond above an open hexagonal cup with a short inward right rim. Reduce the doubled cup walls to a single contour."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b864100d-66af-420b-950a-fabea9dbb5e9'
SOURCE_PATH = 'pictographic-primitives/logos/uikit logo_b864100d-66af-420b-950a-fabea9dbb5e9.svg'
AUTHOR = 'gpt-6'

class UikitLogo(Solo48):
    icon_id = 'uikit-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('uikit', 'css', 'framework', 'hexagon', 'logo', 'brand', 'frontend')

    def build(self):
        # Plan: Detached diamond above an open hexagonal cup with a short inward right rim. Reduce the doubled cup walls to a single contour.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_polyline('diamond',(24,4),(32,10),(24,16),(16,10),closed=True)
        self.add_polyline('cup',(8,22),(8,34),(24,44),(40,34),(40,22),(36,20))

