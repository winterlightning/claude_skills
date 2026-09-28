"""Standalone PlayStation monogram: upright P above a flattened S. Omit surrounding play-button wrapper to isolate the requested logo."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be7296d8-ee16-4dcb-add5-c91c2de21efe'
SOURCE_PATH = 'pictographic-primitives/logos/playstation logo_be7296d8-ee16-4dcb-add5-c91c2de21efe.svg'
AUTHOR = 'gpt-6'

class PlaystationLogo(Solo48):
    icon_id = 'playstation-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('playstation', 'sony', 'gaming', 'console', 'logo', 'brand', 'play')

    def build(self):
        # Plan: Standalone PlayStation monogram: upright P above a flattened S. Omit surrounding play-button wrapper to isolate the requested logo.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_line('p-stem',(20,8),(20,40))
        self.add_bezier('p-bowl',(20,8),((38,8),(39,22),(30,24)))
        self.relate('connect','p-stem','p-bowl')
        self.add_polyline('s-left',(12,28),(4,33),(12,36))
        self.add_bezier('s-right',(30,33),((39,28),(44,31),(44,33)),((44,35),(33,38),(28,40)))

