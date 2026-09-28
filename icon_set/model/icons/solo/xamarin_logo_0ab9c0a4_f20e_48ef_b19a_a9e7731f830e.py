"""Flat-topped hexagonal badge encloses a centered X. Use a shared center and mirrored inner arms."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ab9c0a4-f20e-48ef-b19a-a9e7731f830e'
SOURCE_PATH = 'pictographic-primitives/logos/xamarin logo_0ab9c0a4-f20e-48ef-b19a-a9e7731f830e.svg'
AUTHOR = 'gpt-6'

class XamarinLogo(Solo48):
    icon_id = 'xamarin-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('xamarin', 'microsoft', 'mobile', 'hexagon', 'letter-x', 'logo', 'brand')

    def build(self):
        # Plan: Flat-topped hexagonal badge encloses a centered X. Use a shared center and mirrored inner arms.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_polyline('hexagon',(4,24),(14,8),(34,8),(44,24),(34,40),(14,40),closed=True)
        for j,p in enumerate([(18,18),(30,18),(30,30),(18,30)]):self.add_line('arm-'+str(j),(24,24),p)
        for j in range(4):
            for k in range(j+1,4):self.relate('connect','arm-'+str(j),'arm-'+str(k))

