"""Complete VIRB monogram reflowed into VI above RB. Omit the small plus to keep the I distinct and use open monoline letters to retain all four initials."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93582401-2800-4550-9f29-2758366643de'
SOURCE_PATH = 'pictographic-primitives/logos/virb logo_93582401-2800-4550-9f29-2758366643de.svg'
AUTHOR = 'gpt-6'

class VirbLogo(Solo48):
    icon_id = 'virb-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('virb', 'web', 'wordmark', 'letters', 'logo', 'brand', 'sites')

    def build(self):
        # Plan: Complete VIRB monogram reflowed into VI above RB. Omit the small plus to keep the I distinct and use open monoline letters to retain all four initials.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('v',(6,6),(13,18),(20,6))
        self.add_line('i',(36,6),(36,18))
        for n,x in [('r',6),('b',30)]:
            self.add_polyline(n+'-stem',(x,42),(x,34),(x,26))
            self.add_arc(n+'-top',(x,26),(x,34),radius_x=12,radius_y=4)
            self.relate('connect',n+'-stem',n+'-top')
        self.add_line('r-leg',(6,34),(18,42));self.relate('connect','r-leg','r-stem');self.relate('connect','r-leg','r-top')
        self.add_arc('b-bottom',(30,34),(30,42),radius_x=12,radius_y=4);self.relate('connect','b-bottom','b-stem');self.relate('connect','b-bottom','b-top')

