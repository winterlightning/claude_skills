"""A round central sun is surrounded by two concentric orbital rings. Three smaller circular planets interrupt the rings at the left, upper right, and lower right, creating an asymmetric arrangement around the center.

CIRCLE radial visible extremes (2,2)-(46,46); two interrupted orbits with three visible planets. Orbit arcs break around planets, following Lucide orbit. Sun and the smallest planet simplified to dots; upper/lower planets repositioned to give the rings room.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19de80f5-6c4d-5313-9076-8b30370de428'
SOURCE_PATH = 'pictographic-primitives/science/astronomy solar system_19de80f5-6c4d-5313-9076-8b30370de428.svg'
AUTHOR = 'gpt-6'

class SolarSystemOrbits(Solo48):
    icon_id = 'solar-system-orbits'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('solar system', 'orbit', 'planet', 'sun', 'astronomy', 'space')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('outer-left',(12,8),(12,40),radius_x=20,sweep=False)
        self.add_arc('outer-right',(36,40),(36,8),radius_x=20,sweep=False)
        self.circle('planet-upper',24,7,3)
        self.circle('planet-lower',24,41,3)
        self.add_arc('inner-orbit',(29,17),(29,31),radius_x=9)
        self.add_dot('planet-left',(14,24))
        self.add_dot('sun',(24,24))
