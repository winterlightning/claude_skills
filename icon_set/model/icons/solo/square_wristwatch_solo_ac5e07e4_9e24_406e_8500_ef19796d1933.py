"""Square wristwatch.

Construction reference: watch.
Blank square face; no euro glyph.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = 'ac5e07e4-9e24-406e-8500-ef19796d1933'
SOURCE_PATH = 'pictographic-primitives/other/smart watch square euro sign_ac5e07e4-9e24-406e-8500-ef19796d1933.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'square-wristwatch-solo-ac5e07e4'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('square-wristwatch',)
    keywords = ('square', 'wristwatch')

    def build(self):
        # Face owns equal top/bottom straps with an 8-unit longitudinal band.
        box(self,'face',8,12,40,36,4,nodes=((16,12),(32,12),(16,36),(32,36)))
        self.add_polyline('upper-strap',(16,12),(18,4),(30,4),(32,12))
        self.add_polyline('lower-strap',(16,36),(18,44),(30,44),(32,36))
        self.relate('connect','face','upper-strap')
        self.relate('connect','face','lower-strap')
