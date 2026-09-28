"""Central sun surrounded by an orbit interrupted by three small outlined planets. Circular radii and shared attachment points preserve the source orbital composition at SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '19de80f5-6c4d-5313-9076-8b30370de428'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__solar-system-orbits/20260927T172707Z-thuan-mac-1/reference/astronomy solar system_19de80f5-6c4d-5313-9076-8b30370de428.svg'
AUTHOR = "gpt-6"

class SolarSystemOrbits(Solo48):
    icon_id = 'solar-system-orbits'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('solar system', 'orbit', 'planet', 'sun', 'astronomy', 'space')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        # One orbit interrupted by three outlined planets, with the sun at center.
        self.add_arc('orbit-ne',(27,7),(41,21),radius_x=17,sweep=True)
        self.add_arc('orbit-se',(41,27),(27,41),radius_x=17,sweep=True)
        self.add_arc('orbit-left',(21,41),(21,7),radius_x=17,sweep=True)
        self.circle('sun',24,24,5)
        for name,x,y in (('upper',24,7),('right',41,24),('lower',24,41)):
            points=((x,y-3),(x+3,y),(x,y+3),(x-3,y),(x,y-3))
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_arc(f'{name}-{j}',a,b,radius_x=3,sweep=True)
            self.add_contour(name,*(f'{name}-{j}' for j in range(1,5)),closed=True)
        self.relate('connect','orbit-ne','upper')
        self.relate('connect','orbit-ne','right')
        self.relate('connect','orbit-se','right')
        self.relate('connect','orbit-se','lower')
        self.relate('connect','orbit-left','lower')
        self.relate('connect','orbit-left','upper')
