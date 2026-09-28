"""Complete VISA lettering reflowed as VI above SA. The single-row attempts crowded the A counter and neighboring S; use two rows to preserve all four letters. Omit italic lean and the V flick."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '54dac0e5-3283-4c94-88fa-9346f0d0f9ba'
SOURCE_PATH = 'pictographic-primitives/logos/visa logo_54dac0e5-3283-4c94-88fa-9346f0d0f9ba.svg'
AUTHOR = 'gpt-6'

class VisaLogo(Solo48):
    icon_id = 'visa-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('visa', 'payment', 'credit-card', 'wordmark', 'logo', 'brand', 'finance')

    def build(self):
        # Plan: Complete VISA lettering reflowed as VI above SA. The single-row attempts crowded the A counter and neighboring S; use two rows to preserve all four letters. Omit italic lean and the V flick.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('v',(6,6),(12,18),(18,6));self.add_line('i',(34,6),(34,18))
        self.add_bezier('s',(18,30),((18,26),(6,26),(6,30)),((6,34),(18,34),(18,38)),((18,42),(6,42),(6,38)))
        self.add_polyline('a',(26,42),(28,38),(34,26),(40,38),(42,42))
        self.add_line('a-bar',(28,38),(40,38));self.relate('connect','a','a-bar')

