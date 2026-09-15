"""Lowercase y with a curved descender and three rightward signal strokes. Reduce doubled letter outlines to one coherent branch and keep all three rays."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af506dcb-44a3-4932-8104-f8bded8e82ba'
SOURCE_PATH = 'pictographic-primitives/logos/yammer logo_af506dcb-44a3-4932-8104-f8bded8e82ba.svg'
AUTHOR = 'gpt-6'

class YammerLogo(Solo48):
    icon_id = 'yammer-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('yammer', 'microsoft', 'social', 'letter-y', 'logo', 'brand', 'enterprise')

    def build(self):
        # Plan: Lowercase y with a curved descender and three rightward signal strokes. Reduce doubled letter outlines to one coherent branch and keep all three rays.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_polyline('y',(4,8),(14,28),(24,8))
        self.add_bezier('tail',(14,28),((14,36),(10,40),(4,40)));self.relate('connect','y','tail')
        for j,(a,b) in enumerate([((34,16),(42,8)),((34,24),(44,24)),((34,32),(42,40))]):self.add_line('ray-'+str(j),a,b)

