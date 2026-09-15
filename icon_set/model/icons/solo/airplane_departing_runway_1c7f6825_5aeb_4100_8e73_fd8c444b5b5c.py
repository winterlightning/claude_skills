"""A climbing airplane rises above a perspective runway.

Construction: plane-takeoff: rising silhouette above a detached ground element.
Reduction: Runway reduced to a plain perspective trapezoid; dashed centerline omitted for clearance; airplane upper wing reduced to one attached stroke. Deliberate flight-direction asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c7f6825-5aeb-4100-8e73-fd8c444b5b5c'
SOURCE_PATH = 'pictographic-primitives/travel/optimization plane_1c7f6825-5aeb-4100-8e73-fd8c444b5b5c.svg'
AUTHOR = 'gpt-6'


class AirplaneDepartingRunway(Solo48):
    icon_id = 'airplane-departing-runway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airplane', 'departure', 'runway', 'takeoff', 'airport', 'flight', 'plane', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); airplane and runway are distinct scene parts.
        run('plane-body',(40,15),(17,25),(10,23),(6,14),(14,12),(18,14),(30,10),(34,7))
        self.add_arc('nose',(34,7),(40,15),radius_x=5)
        self.add_contour('plane',*runs['plane-body'],'nose',closed=True)
        self.add_line('far-wing',(30,10),(22,6))
        self.relate('connect','plane','far-wing')
        self.add_polyline('runway',(10,34),(38,34),(42,42),(6,42),closed=True)
