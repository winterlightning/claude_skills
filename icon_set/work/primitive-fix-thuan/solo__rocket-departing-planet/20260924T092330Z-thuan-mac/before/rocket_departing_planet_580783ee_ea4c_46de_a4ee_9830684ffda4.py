"""A small rocket points upper-right beside a gap in a large circular planet outline. A curved orbital trail loops around the lower-left edge, and a separate tapered exhaust mark lies between the rocket and planet.

SQUARE visible bounds (4,4)-(44,44); rocket departing upper-right from an open planet outline. Dense orbit loop reduced to curved flight trail; separate exhaust omitted. Lucide rocket informed the small pointed craft. Directional scene retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '580783ee-ea4c-46de-a4ee-9830684ffda4'
SOURCE_PATH = 'pictographic-primitives/science/rocket earth_580783ee-ea4c-46de-a4ee-9830684ffda4.svg'
AUTHOR = 'gpt-6'

class RocketDepartingPlanet(Solo48):
    icon_id = 'rocket-departing-planet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('rocket', 'planet', 'orbit', 'departure', 'space', 'flight')

    def segments(self, name, *points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):
            self.add_line(f'{name}-{i}',a,b)

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('planet-upper-left',(18,20),(8,30),radius_x=10,sweep=False)
        self.add_arc('planet-left-bottom',(8,30),(12,38),radius_x=10,sweep=False)
        self.add_arc('planet-bottom',(12,38),(18,40),radius_x=10,sweep=False)
        self.add_arc('planet-right',(18,40),(28,30),radius_x=10,sweep=False)
        self.add_contour('planet','planet-upper-left','planet-left-bottom','planet-bottom','planet-right')
        self.add_polyline('rocket',(42,6),(40,16),(35,21),(27,13),(32,8),closed=True)
        self.add_arc('trail-curl',(6,42),(12,38),radius_x=10)
        self.add_line('trail',(12,38),(26,24))
        self.add_contour('departure-trail','trail-curl','trail')
        self.relate('connect','departure-trail','planet')
