"""Rounded square frame and central forward slash. Reduce the outlined parallelogram to one slanted stroke, retaining open space around it."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba09f2a8-8b62-435c-9541-abb3adc7212a'
SOURCE_PATH = 'pictographic-primitives/logos/wip logo_ba09f2a8-8b62-435c-9541-abb3adc7212a.svg'
AUTHOR = 'gpt-6'

class WipLogo(Solo48):
    icon_id = 'wip-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('wip', 'work-in-progress', 'slash', 'logo', 'brand', 'makers', 'community')

    def build(self):
        # Plan: Rounded square frame and central forward slash. Reduce the outlined parallelogram to one slanted stroke, retaining open space around it.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for j,(a,b,c) in enumerate([((10,6),(38,6),(42,10)),((42,10),(42,38),(38,42)),((38,42),(10,42),(6,38)),((6,38),(6,10),(10,6))]):
            self.add_line('side-'+str(j),a,b);self.add_arc('corner-'+str(j),b,c,radius_x=4)
        self.add_contour('frame',*[x for j in range(4) for x in ('side-'+str(j),'corner-'+str(j))],closed=True)
        self.add_line('slash',(18,32),(30,16))

