"""A spherical satellite sits toward the upper right, with long slender antenna rods extending leftward and downward. The rods attach at different points around the sphere, producing a strongly asymmetric silhouette.

SQUARE visible bounds (4,4)-(44,44). Sphere with three long aerials as visible in the source. Directional asymmetry retained. Lucide satellite informed clear separation of body and antennae, without importing its solar-panel design.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78fe3b70-a677-407c-a689-55a0827b0ff4'
SOURCE_PATH = 'pictographic-primitives/science/sputnik_78fe3b70-a677-407c-a689-55a0827b0ff4.svg'
AUTHOR = 'gpt-6'

class SputnikSatellite(Solo48):
    icon_id = 'sputnik-satellite'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('sputnik', 'satellite', 'sphere', 'antenna', 'orbit', 'space')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        points=[(29,6),(42,19),(34,31),(29,32),(17,24),(16,19)]
        for i,a in enumerate(points):
            self.add_arc(f'sphere-{i}',a,points[(i+1)%6],radius_x=13)
        self.add_contour('sphere',*(f'sphere-{i}' for i in range(6)),closed=True)
        for n,a,b in [('upper',(29,6),(6,14)),('lower-left',(17,24),(6,42)),('lower-right',(34,31),(30,42))]:
            self.add_line(n,a,b);self.relate('connect',n,'sphere')
