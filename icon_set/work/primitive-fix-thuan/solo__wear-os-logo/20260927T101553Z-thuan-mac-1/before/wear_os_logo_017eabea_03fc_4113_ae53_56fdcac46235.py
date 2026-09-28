"""Two parallel slanted bars followed by two unequal rings. Share the bar vector and omit capsule outlines to preserve four distinct components."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '017eabea-03fc-4113-ae53-56fdcac46235'
SOURCE_PATH = 'pictographic-primitives/logos/wear os logo_017eabea-03fc-4113-ae53-56fdcac46235.svg'
AUTHOR = 'gpt-6'

class WearOsLogo(Solo48):
    icon_id = 'wear-os-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('wear-os', 'google', 'smartwatch', 'wearable', 'logo', 'brand', 'android')

    def build(self):
        # Plan: Two parallel slanted bars followed by two unequal rings. Share the bar vector and omit capsule outlines to preserve four distinct components.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        for j,x in enumerate((4,18)):self.add_line('bar-'+str(j),(x,8),(x+12,40))
        circle('large',39,14,5);circle('small',39,31,3)

