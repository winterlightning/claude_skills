"""A broad outlined lowercase lambda has two diagonal legs meeting near the upper left. The longer descending stroke ends in a squared foot at lower right, while the upper stroke has a short horizontal cap.

SQUARE visible bounds (4,4)-(44,44); standalone outlined lowercase Greek letter with upper cap, diagonal legs and squared right foot. No useful local Lucide match. Directional letter structure is intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4cd0c002-8b03-5e29-8d64-2721a4a018cb'
SOURCE_PATH = 'pictographic-primitives/science/lambda_4cd0c002-8b03-5e29-8d64-2721a4a018cb.svg'
AUTHOR = 'gpt-6'

class OutlinedLambda(Solo48):
    icon_id = 'outlined-lambda'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('lambda', 'greek', 'letter', 'physics', 'mathematics', 'symbol')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_polyline('lambda',(12,6),(22,6),(38,34),(42,34),(42,42),(32,42),(24,28),(16,42),(6,42),(20,20),(16,14),(12,14),closed=True)
