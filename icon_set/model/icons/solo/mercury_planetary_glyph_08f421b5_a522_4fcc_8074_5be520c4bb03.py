"""A circular body carries an upward-opening crescent across its top and a short stem below. A horizontal crossbar intersects the lower stem, forming the familiar vertically aligned Mercury symbol.

VRECT_XL visible bounds (6,2)-(42,46); standalone Mercury symbol retains upper crescent, circular body and lower cross. Local Mercury module informed shared cardinal attachments; symmetric about x=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '08f421b5-a522-4fcc-8074-5be520c4bb03'
SOURCE_PATH = 'pictographic-primitives/science/mercury_08f421b5-a522-4fcc-8074-5be520c4bb03.svg'
AUTHOR = 'gpt-6'

class MercuryPlanetaryGlyph(Solo48):
    icon_id = 'mercury-planetary-glyph'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('mercury', 'symbol', 'planet', 'astronomy', 'astrology', 'circle')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('horn-left',(8,4),(24,14),radius_x=16,radius_y=10,sweep=False)
        self.add_arc('horn-right',(24,14),(40,4),radius_x=16,radius_y=10,sweep=False)
        self.add_contour('horns','horn-left','horn-right')
        self.circle('body',24,24,10)
        self.add_polyline('stem',(24,34),(24,40),(24,44))
        self.add_polyline('cross',(16,40),(24,40),(32,40))
        self.relate('connect','horns','body');self.relate('connect','body','stem');self.relate('connect','stem','cross')
