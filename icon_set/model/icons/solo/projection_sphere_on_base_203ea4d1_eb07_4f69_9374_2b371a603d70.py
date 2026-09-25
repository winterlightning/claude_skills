"""A large plain sphere sits above a low rounded rectangular base. Two angled supports join its lower sides to the base, leaving a trapezoidal opening directly beneath the sphere.

VRECT_XL visible bounds (6,2)-(42,46); plain sphere, angled supports and low rounded base. No useful exact Lucide match; bilateral symmetry and empty sphere retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '203ea4d1-eb07-4f69-9374-2b371a603d70'
SOURCE_PATH = 'pictographic-primitives/science/projection_203ea4d1-eb07-4f69-9374-2b371a603d70.svg'
AUTHOR = 'gpt-6'

class ProjectionSphereOnBase(Solo48):
    icon_id = 'projection-sphere-on-base'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('projection', 'sphere', 'base', 'display', 'device', 'science')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        points=[(14,14),(24,4),(34,14),(30,22),(24,24),(18,22)]
        for i,a in enumerate(points):
            self.add_arc(f'sphere-{i}',a,points[(i+1)%6],radius_x=10)
        self.add_contour('sphere',*(f'sphere-{i}' for i in range(6)),closed=True)
        self.add_line('support-left',(18,22),(12,36))
        self.add_line('support-right',(30,22),(36,36))
        self.relate('connect','support-left','sphere');self.relate('connect','support-right','sphere')
        self.segments('base-top',(12,36),(36,36))
        self.add_arc('base-right',(36,36),(36,44),radius_x=4)
        self.add_line('base-bottom',(36,44),(12,44))
        self.add_arc('base-left',(12,44),(12,36),radius_x=4)
        self.add_contour('base','base-top-1','base-right','base-bottom','base-left',closed=True)
        self.relate('connect','base','support-left');self.relate('connect','base','support-right')
