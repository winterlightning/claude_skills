"""Paired cupped hands surround a two-leaf sprout. Mirror hands and broad curved leaves about x=24. Human full_body_ref.png informs round-ended limb vocabulary; no head is present."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf61d88d-d269-4a85-955c-a411e11583cd'
SOURCE_PATH = 'pictographic-primitives/logos/treehouse logo_bf61d88d-d269-4a85-955c-a411e11583cd.svg'
AUTHOR = 'gpt-6'

class TreehouseLogo(Solo48):
    icon_id = 'treehouse-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('treehouse', 'learning', 'hands', 'sprout', 'logo', 'brand', 'education')

    def build(self):
        # Plan: Paired cupped hands surround a two-leaf sprout. Mirror hands and broad curved leaves about x=24. Human full_body_ref.png informs round-ended limb vocabulary; no head is present.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for j in range(2):
            def p(x,y):return (x,y) if j==0 else (48-x,y)
            self.add_polyline('fingers-'+str(j),p(6,24),p(6,30),p(6,34))
            self.add_bezier('palm-'+str(j),p(6,34),(p(6,38),p(8,39),p(8,42)))
            self.add_polyline('thumb-'+str(j),p(6,30),p(18,36),p(18,42))
            self.relate('connect','fingers-'+str(j),'palm-'+str(j));self.relate('connect','fingers-'+str(j),'thumb-'+str(j))
            self.add_arc('leaf-a-'+str(j),p(10,6),p(24,20),radius_x=14,sweep=j==0)
            self.add_arc('leaf-b-'+str(j),p(24,20),p(10,6),radius_x=14,sweep=j==0)
            self.add_contour('leaf-'+str(j),'leaf-a-'+str(j),'leaf-b-'+str(j),closed=True)
        self.add_line('plant-stem',(24,20),(24,30))
        self.relate('connect','leaf-0','leaf-1')
        for j in range(2):self.relate('connect','leaf-'+str(j),'plant-stem')

