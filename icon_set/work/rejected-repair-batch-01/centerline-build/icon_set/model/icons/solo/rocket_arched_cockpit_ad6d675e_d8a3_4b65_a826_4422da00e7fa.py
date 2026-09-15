"""An upright rocket has a pointed curved nose and a long body ending in a rounded base. Two broad triangular fins flank its lower half, with a small arched cockpit mark above and a short central tail line below.

VRECT_XL visible bounds (6,2)-(42,46); pointed curved nose, arched cockpit, fins integrated into the hull and central tail. Fin interior seams omitted. Lucide rocket informed hierarchy; symmetric construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad6d675e-d8a3-4b65-a826-4422da00e7fa'
SOURCE_PATH = 'pictographic-primitives/science/rocket base_ad6d675e-d8a3-4b65-a826-4422da00e7fa.svg'
AUTHOR = 'gpt-6'

class RocketArchedCockpit(Solo48):
    icon_id = 'rocket-arched-cockpit'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('rocket', 'cockpit', 'fin', 'space', 'launch', 'spacecraft')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('nose-right',(24,4),(36,18),radius_x=18)
        self.segments('right-side',(36,18),(36,24),(40,36),(28,36))
        self.add_arc('base-right',(28,36),(24,38),radius_x=4,radius_y=2)
        self.add_arc('base-left',(24,38),(20,36),radius_x=4,radius_y=2)
        self.segments('left-side',(20,36),(8,36),(12,24),(12,18))
        self.add_arc('nose-left',(12,18),(24,4),radius_x=18)
        self.add_contour('hull','nose-right',*(f'right-side-{i}' for i in range(1,4)),'base-right','base-left',*(f'left-side-{i}' for i in range(1,4)),'nose-left',closed=True)
        self.add_arc('cockpit',(21,24),(27,24),radius_x=3,radius_y=4)
        self.add_line('tail',(24,38),(24,44));self.relate('connect','tail','hull')
