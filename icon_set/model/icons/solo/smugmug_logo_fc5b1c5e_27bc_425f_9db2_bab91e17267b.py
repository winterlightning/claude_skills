"""A broad semicircular grin under two matching small ring eyes; share eye radius and baseline and mirror about x=24."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc5b1c5e-27bc-425f-9db2-bab91e17267b'
SOURCE_PATH = 'pictographic-primitives/logos/smug mug logo_fc5b1c5e-27bc-425f-9db2-bab91e17267b.svg'
AUTHOR = 'gpt-6'

class SmugmugLogo(Solo48):
    icon_id = 'smugmug-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('smugmug', 'photos', 'smile', 'face', 'logo', 'brand', 'hosting')

    def build(self):
        # Plan: A broad semicircular grin under two matching small ring eyes; share eye radius and baseline and mirror about x=24.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_line('mouth-top',(4,24),(44,24))
        self.add_arc('grin',(44,24),(4,24),radius_x=20,radius_y=16)
        self.add_contour('mouth','mouth-top','grin',closed=True)
        for x in (14,34):circle('eye-'+str(x),x,11,3)

