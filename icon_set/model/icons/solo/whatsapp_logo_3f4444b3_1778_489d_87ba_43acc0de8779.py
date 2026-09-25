"""Round speech bubble with a diagonal telephone receiver. Reduce the handset ribbon to a hooked monoline stroke and keep the lower-left bubble tail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f4444b3-1778-489d-87ba-43acc0de8779'
SOURCE_PATH = 'pictographic-primitives/logos/whatsapp logo_3f4444b3-1778-489d-87ba-43acc0de8779.svg'
AUTHOR = 'gpt-6'

class WhatsappLogo(Solo48):
    icon_id = 'whatsapp-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('whatsapp', 'chat', 'phone', 'messenger', 'logo', 'brand', 'call')

    def build(self):
        # Plan: Round speech bubble with a diagonal telephone receiver. Reduce the handset ribbon to a hooked monoline stroke and keep the lower-left bubble tail.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_arc('top',(6,24),(24,6),radius_x=18);self.add_arc('right',(24,6),(42,24),radius_x=18)
        self.add_arc('bottom',(42,24),(24,42),radius_x=18)
        self.add_bezier('lower-left',(24,42),((21,42),(18,41),(16,40)))
        self.add_polyline('tail',(16,40),(6,42),(10,32))
        self.add_bezier('upper-left',(10,32),((7,29),(6,27),(6,24)))
        for a,b in [('top','right'),('right','bottom'),('bottom','lower-left'),('lower-left','tail'),('tail','upper-left'),('upper-left','top')]:self.relate('connect',a,b)
        self.add_line('earpiece',(20,16),(16,20))
        self.add_bezier('receiver',(16,20),((16,24),(24,32),(28,32)))
        self.add_line('mouthpiece',(28,32),(32,28));self.add_contour('phone','earpiece','receiver','mouthpiece')

