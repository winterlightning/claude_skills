"""An alien head has a broad curved crown, slanted leaf-shaped eyes, and a segmented lower mask with a long central panel. Long narrow appendages hang down from both sides of the head.

SQUARE visible bounds (4,4)-(44,44); crown, long side appendages, angled brows and central mask panel. Leaf eye interiors and minor jaw segmentation omitted. No useful Lucide Predator match; symmetric mask construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35e9f543-af8b-4fac-86a7-de6f396b8693'
SOURCE_PATH = 'pictographic-primitives/science/predator_35e9f543-af8b-4fac-86a7-de6f396b8693.svg'
AUTHOR = 'gpt-6'

class PredatorHead(Solo48):
    icon_id = 'predator-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('predator', 'alien', 'head', 'mask', 'creature', 'fiction')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('crown',(10,16),(38,16),radius_x=14,radius_y=10)
        self.segments('mask',(38,16),(34,30),(30,38),(28,38),(20,38),(18,38),(14,30),(10,16))
        self.add_contour('head','crown',*(f'mask-{i}' for i in range(1,8)),closed=True)
        self.add_polyline('left-tendril',(10,16),(6,24),(6,42))
        self.add_polyline('right-tendril',(38,16),(42,24),(42,42))
        self.relate('connect','head','left-tendril');self.relate('connect','head','right-tendril')
        self.add_polyline('central-mask',(20,38),(20,22),(20,20),(28,20),(28,22),(28,38))
        self.relate('connect','central-mask','head')
        self.add_line('brow-left',(14,18),(20,22));self.add_line('brow-right',(34,18),(28,22))
        self.relate('connect','brow-left','central-mask');self.relate('connect','brow-right','central-mask')
