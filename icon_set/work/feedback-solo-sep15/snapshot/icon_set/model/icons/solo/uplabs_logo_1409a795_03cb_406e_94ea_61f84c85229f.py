"""Lowercase up in monoline lettering with an open p counter and long descender. Omit the heavy outline and the tiny u terminal."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1409a795-03cb-406e-94ea-61f84c85229f'
SOURCE_PATH = 'pictographic-primitives/logos/uplabs logo_1409a795-03cb-406e-94ea-61f84c85229f.svg'
AUTHOR = 'gpt-6'

class UplabsLogo(Solo48):
    icon_id = 'uplabs-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('uplabs', 'design', 'resources', 'wordmark', 'logo', 'brand', 'up')

    def build(self):
        # Plan: Lowercase up in monoline lettering with an open p counter and long descender. Omit the heavy outline and the tiny u terminal.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_line('u-left',(4,8),(4,26));self.add_arc('u-bend',(4,26),(18,26),radius_x=7,sweep=False);self.add_line('u-right',(18,26),(18,8));self.add_contour('u','u-left','u-bend','u-right')
        self.add_polyline('p-stem',(28,8),(28,18),(28,40))
        circle('p-counter',36,18,8);self.relate('connect','p-stem','p-counter')

