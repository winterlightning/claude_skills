"""A single upright test tube has straight parallel sides that join in a deep rounded bottom. Its open mouth is indicated by a broad projecting rim across the top.

VRECT_XL visible bounds (6,2)-(42,46); parallel tube walls and round bottom, topped by a projecting rim. Lucide test-tube informed the continuous U contour. Empty interior retained; symmetric about x=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4c97de9-a22d-519d-af05-c06bdb6f8b8c'
SOURCE_PATH = 'pictographic-primitives/science/lab tube_f4c97de9-a22d-519d-af05-c06bdb6f8b8c.svg'
AUTHOR = 'gpt-6'

class PlainTestTube(Solo48):
    icon_id = 'plain-test-tube'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('test tube', 'laboratory', 'glass', 'chemistry', 'tube', 'vessel')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_line('left',(14,4),(14,34))
        self.add_arc('bottom',(14,34),(34,34),radius_x=10,sweep=False)
        self.add_line('right',(34,34),(34,4))
        self.add_contour('tube','left','bottom','right')
        self.add_polyline('rim',(8,4),(14,4),(34,4),(40,4))
        self.relate('connect','tube','rim')
