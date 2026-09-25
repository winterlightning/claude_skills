"""Monoline P followed by four horizontal streaming bars. Share stripe levels and retain the open lower stem; omit the doubled P outline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0daf6a58-52c3-46c1-9116-5fbf676eeb0e'
SOURCE_PATH = 'pictographic-primitives/logos/streaming logo_0daf6a58-52c3-46c1-9116-5fbf676eeb0e.svg'
AUTHOR = 'gpt-6'

class StreamingLogo(Solo48):
    icon_id = 'streaming-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('streaming', 'letter-p', 'lines', 'logo', 'brand', 'media', 'broadcast')

    def build(self):
        # Plan: Monoline P followed by four horizontal streaming bars. Share stripe levels and retain the open lower stem; omit the doubled P outline.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_line('stem',(4,8),(4,40))
        self.add_line('top',(4,8),(10,8))
        self.add_arc('bowl',(10,8),(10,24),radius_x=8)
        self.add_line('return',(10,24),(4,24))
        self.add_contour('p-bowl','top','bowl','return')
        self.relate('connect','stem','p-bowl')
        for j,(x,y) in enumerate([(32,8),(32,18),(30,28),(26,40)]):self.add_line('stripe-'+str(j),(x,y),(44,y))

