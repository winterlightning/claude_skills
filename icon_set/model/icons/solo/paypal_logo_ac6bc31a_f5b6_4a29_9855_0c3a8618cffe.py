"""Bold inclined P outline with rounded bowl and independent counter; retain italic asymmetry and wide stem."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac6bc31a-f5b6-4a29-9855-0c3a8618cffe'
SOURCE_PATH = 'pictographic-primitives/logos/paypal logo_ac6bc31a-f5b6-4a29-9855-0c3a8618cffe.svg'
AUTHOR = 'gpt-6'

class PaypalLogo(Solo48):
    icon_id = 'paypal-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('paypal', 'payment', 'letter-p', 'logo', 'brand', 'finance', 'money')

    def build(self):
        # Plan: Bold inclined P outline with rounded bowl and independent counter; retain italic asymmetry and wide stem.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_line('top',(16,4),(27,4))
        self.add_arc('bowl',(27,4),(27,30),radius_x=13,radius_y=13)
        for n,a,b in [('foot-1',(27,30),(20,30)),('foot-2',(20,30),(17,44)),('foot-3',(17,44),(8,44)),('foot-4',(8,44),(16,4))]:
            self.add_line(n,a,b)
        self.add_contour('outline','top','bowl','foot-1','foot-2','foot-3','foot-4',closed=True)
        self.add_bezier('counter',(23,13),((34,12),(32,21),(21,21)))
        self.add_line('counter-close',(21,21),(23,13))
        self.add_contour('counter-shape','counter','counter-close',closed=True)

