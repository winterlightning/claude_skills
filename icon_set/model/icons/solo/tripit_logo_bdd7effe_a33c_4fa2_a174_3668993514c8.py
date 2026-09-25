"""Seven radial spokes with small circular endpoints. Reduce the central oval hub to one shared junction, retaining the seven-node starburst."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdd7effe-a33c-4fa2-a174-3668993514c8'
SOURCE_PATH = 'pictographic-primitives/logos/tripit logo_bdd7effe-a33c-4fa2-a174-3668993514c8.svg'
AUTHOR = 'gpt-6'

class TripitLogo(Solo48):
    icon_id = 'tripit-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('tripit', 'travel', 'itinerary', 'network', 'logo', 'brand', 'nodes')

    def build(self):
        # Plan: Seven radial spokes with small circular endpoints. Reduce the central oval hub to one shared junction, retaining the seven-node starburst.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        ends=[(24,8),(39,12),(39,26),(34,39),(14,39),(8,27),(9,14)]
        for j,(x,y) in enumerate(ends):
            # Each circular node shares its exact inward apex with the spoke.
            r=2 if j in (0,4,5,6) else 3
            a=(x-r,y) if x>24 else (x+r,y) if x<24 else (x,y+r)
            b=(2*x-a[0],2*y-a[1])
            self.add_arc(f'node-{j}-a',a,b,radius_x=r);self.add_arc(f'node-{j}-b',b,a,radius_x=r)
            self.add_contour('node-'+str(j),f'node-{j}-a',f'node-{j}-b',closed=True)
            self.add_line('spoke-'+str(j),(24,25),a);self.relate('connect','node-'+str(j),'spoke-'+str(j))
        for j in range(7):
            for k in range(j+1,7):self.relate('connect','spoke-'+str(j),'spoke-'+str(k))

