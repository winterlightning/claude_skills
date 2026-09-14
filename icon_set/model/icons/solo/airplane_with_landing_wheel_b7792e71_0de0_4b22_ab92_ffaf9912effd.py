"""A level airplane has swept wings and a nose wheel on a short strut.

Construction: plane: single wing/fuselage outline; luggage: small circular wheel and real attachment.
Reduction: Upper wing reduced to one attached stroke; landing wheel retained. Deliberate level side-view asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7792e71-0de0-4b22-ab92-ffaf9912effd'
SOURCE_PATH = 'pictographic-primitives/travel/plane with wheel_b7792e71-0de0-4b22-ab92-ffaf9912effd.svg'
AUTHOR = 'gpt-6'


class AirplaneWithLandingWheel(Solo48):
    icon_id = 'airplane-with-landing-wheel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airplane', 'landing-gear', 'wheel', 'flight', 'aircraft', 'plane', 'aviation', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); round nose rx5, wheel r3.
        run('body',(37,26),(34,26),(29,26),(22,42),(12,42),(19,26),(12,26),(6,14),(14,14),(19,18),(26,18),(37,18))
        self.add_arc('nose',(37,18),(37,26),radius_x=5,radius_y=4)
        self.add_contour('airplane',*runs['body'],'nose',closed=True)
        self.add_line('upper-wing',(26,18),(14,6))
        self.relate('connect','airplane','upper-wing')
        self.add_line('strut',(34,26),(34,35))
        self.relate('connect','airplane','strut')
        self.add_arc('wheel-right',(34,35),(34,41),radius_x=3)
        self.add_arc('wheel-left',(34,41),(34,35),radius_x=3)
        self.add_contour('wheel','wheel-right','wheel-left',closed=True)
        self.relate('connect','wheel','strut')
