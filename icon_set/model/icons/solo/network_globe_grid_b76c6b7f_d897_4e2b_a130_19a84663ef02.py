"""Network Globe. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b76c6b7f-d897-4e2b-a130-19a84663ef02'
SOURCE_PATH = 'pictographic-primitives/websites/network globe_b76c6b7f-d897-4e2b-a130-19a84663ef02.svg'
AUTHOR = 'gpt-6'

class NetworkGlobeGrid(Solo48):
    icon_id = 'network-globe-grid'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    aliases = ()
    keywords = ('globe', 'network', 'world', 'internet', 'sphere', 'grid', 'web')

    def build(self):
        # Radius 20 has integer 12/16 offsets, so all band joins lie on the sphere.
        points=[(24,6),(40,12),(42,24),(40,36),(24,42),(8,36),(6,24),(8,12)]
        for n,p in enumerate(points): self.add_arc(f'outline-{n}',p,points[(n+1)%8],radius_x=20)
        self.add_contour('globe',*(f'outline-{n}' for n in range(8)),closed=True)
        self.add_polyline('meridian',(24,6),(24,12),(24,24),(24,36),(24,42))
        self.relate('connect','meridian','globe')
        for y,left,right in [(12,8,40),(24,4,44),(36,8,40)]:
            name=f'band-{y}'
            self.add_polyline(name,(left,y),(24,y),(right,y))
            self.relate('connect',name,'globe')
            self.relate('connect',name,'meridian')
