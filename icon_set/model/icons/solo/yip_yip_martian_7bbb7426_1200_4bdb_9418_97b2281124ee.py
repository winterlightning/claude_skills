"""A rounded dome-like creature has two large circular eyes sitting along its upper edge. Two curved antennae rise outward above the eyes and end near short detached tips; a straight baseline closes the body.

SQUARE visible bounds (4,4)-(44,44); two prominent round eyes, outward antennae and dome body with straight base. Detached antenna tips omitted. No useful Lucide character match; symmetric paired construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bbb7426-1200-4bdb-9418-97b2281124ee'
SOURCE_PATH = 'pictographic-primitives/science/sesame street yip yips_7bbb7426-1200-4bdb-9418-97b2281124ee.svg'
AUTHOR = 'gpt-6'

class YipYipMartian(Solo48):
    icon_id = 'yip-yip-martian'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('yip yip', 'martian', 'alien', 'antenna', 'eyes', 'puppet')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.circle('eye-left',16,20,5);self.circle('eye-right',32,20,5)
        self.add_arc('body-left',(11,20),(6,42),radius_x=5,radius_y=22,sweep=False)
        self.add_line('body-base',(6,42),(42,42))
        self.add_arc('body-right',(42,42),(37,20),radius_x=5,radius_y=22,sweep=False)
        self.add_contour('body','body-left','body-base','body-right')
        self.add_line('eye-bridge',(21,20),(27,20))
        self.relate('connect','body','eye-left');self.relate('connect','body','eye-right')
        self.relate('connect','eye-bridge','eye-left');self.relate('connect','eye-bridge','eye-right')
        self.add_arc('antenna-left',(16,15),(10,6),radius_x=6,radius_y=9,sweep=False)
        self.add_arc('antenna-right',(32,15),(38,6),radius_x=6,radius_y=9)
        self.relate('connect','antenna-left','eye-left');self.relate('connect','antenna-right','eye-right')
