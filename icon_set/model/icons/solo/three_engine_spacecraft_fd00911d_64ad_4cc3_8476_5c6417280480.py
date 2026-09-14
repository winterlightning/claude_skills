"""A front-facing spacecraft has a rounded upper cabin above a boxy body and two side pods. A circular upper window and square central panel sit above three evenly spaced flared engine nozzles.

HRECT_XL visible bounds (2,6)-(46,42); rounded cabin, side pods and three equally spaced engines. Central square panel omitted to preserve the window and engines. Lucide rocket informed engine hierarchy; bilateral symmetry and shared nozzle dimensions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd00911d-64ad-4cc3-8476-5c6417280480'
SOURCE_PATH = 'pictographic-primitives/science/fiction ship_fd00911d-64ad-4cc3-8476-5c6417280480.svg'
AUTHOR = 'gpt-6'

class ThreeEngineSpacecraft(Solo48):
    icon_id = 'three-engine-spacecraft'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('spacecraft', 'engine', 'cabin', 'rocket', 'nozzle', 'space')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('cabin',(12,20),(36,20),radius_x=12,radius_y=12)
        self.segments('body',(36,20),(44,24),(44,32),(43,32),(37,32),(27,32),(21,32),(11,32),(5,32),(4,32),(4,24),(12,20))
        self.add_contour('hull','cabin',*(f'body-{i}' for i in range(1,12)),closed=True)
        self.circle('window',24,20,3)
        for i,x in enumerate((8,24,40)):
            self.add_polyline(f'nozzle-{i}',(x-3,32),(x-4,40),(x+4,40),(x+3,32))
            self.relate('connect','hull',f'nozzle-{i}')
