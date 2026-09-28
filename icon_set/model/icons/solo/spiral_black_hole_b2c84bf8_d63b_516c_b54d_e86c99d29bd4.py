"""Several long curved arms sweep inward around a small open center, forming a rotating pinwheel-like silhouette. Their outer ends spread in different directions while the inner curves overlap closely around the central opening.

CIRCLE visible extremes (2,2)-(46,46), radial fit; overlapping arms reduced to one coherent inward spiral. No useful Lucide spiral match. Directional rotational asymmetry is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2c84bf8-d63b-516c-b54d-e86c99d29bd4'
SOURCE_PATH = 'pictographic-primitives/science/astronomy blackhole_b2c84bf8-d63b-516c-b54d-e86c99d29bd4.svg'
AUTHOR = 'gpt-6'

class SpiralBlackHole(Solo48):
    icon_id = 'spiral-black-hole'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('black hole', 'spiral', 'vortex', 'astronomy', 'space', 'swirl')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('outer',(24,4),(24,44),radius_x=20,large_arc=False)
        self.add_arc('lower-turn',(24,44),(24,14),radius_x=15,sweep=True)
        self.add_arc('inner-turn',(24,14),(24,34),radius_x=10,sweep=True)
        self.add_arc('core-turn',(24,34),(24,24),radius_x=5,sweep=True)
        self.add_contour('vortex','outer','lower-turn','inner-turn','core-turn')
