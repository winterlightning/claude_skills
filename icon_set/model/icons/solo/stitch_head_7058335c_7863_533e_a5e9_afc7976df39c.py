"""A small rounded alien head has two extremely long upright ears curving outward, a short tuft on top, and tiny facial marks. A broad rounded lower muzzle projects beneath the face.

SQUARE visible bounds (4,4)-(44,44). Rounded alien face with elongated upright ears and broad lower muzzle. Tiny eyes and tuft omitted to keep the ears and nose clear. No useful exact Lucide character match; paired ears and head arcs mirror about x=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7058335c-7863-533e-a5e9-afc7976df39c'
SOURCE_PATH = 'pictographic-primitives/science/stitch_7058335c-7863-533e-a5e9-afc7976df39c.svg'
AUTHOR = 'gpt-6'

class StitchHead(Solo48):
    icon_id = 'stitch-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('stitch', 'alien', 'head', 'ears', 'cartoon', 'face')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('crown-left',(12,28),(24,14),radius_x=12,radius_y=14)
        self.add_arc('crown-right',(24,14),(36,28),radius_x=12,radius_y=14)
        self.add_line('cheek-right',(36,28),(36,32))
        self.add_arc('muzzle',(36,32),(12,32),radius_x=12,radius_y=10)
        self.add_line('cheek-left',(12,32),(12,28))
        self.add_contour('head','crown-left','crown-right','cheek-right','muzzle','cheek-left',closed=True)
        self.add_line('muzzle-top',(12,32),(36,32));self.relate('connect','muzzle-top','head')
        self.add_arc('ear-left-outer',(12,28),(6,10),radius_x=6,radius_y=18)
        self.add_arc('ear-left-tip',(6,10),(14,10),radius_x=4)
        self.add_line('ear-left-inner',(14,10),(14,20))
        self.add_contour('ear-left','ear-left-outer','ear-left-tip','ear-left-inner')
        self.add_arc('ear-right-outer',(42,10),(36,28),radius_x=6,radius_y=18)
        self.add_arc('ear-right-tip',(34,10),(42,10),radius_x=4)
        self.add_line('ear-right-inner',(34,20),(34,10))
        self.add_contour('ear-right','ear-right-inner','ear-right-tip','ear-right-outer')
        self.relate('connect','ear-left','head');self.relate('connect','ear-right','head')
        self.add_dot('nose',(24,23))
