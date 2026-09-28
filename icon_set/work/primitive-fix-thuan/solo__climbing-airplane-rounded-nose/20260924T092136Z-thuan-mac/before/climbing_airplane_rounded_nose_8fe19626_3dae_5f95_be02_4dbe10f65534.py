"""A gently climbing airplane has a rounded nose and swept near wing.

Construction: plane-takeoff: a continuous fuselage with rounded nose and tapered tail.
Reduction: Omitted windows; kept the upper wing and distinct lower wing. Side-view asymmetry follows the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fe19626-3dae-5f95-be02-4dbe10f65534'
SOURCE_PATH = 'pictographic-primitives/travel/plane 1_8fe19626-3dae-5f95-be02-4dbe10f65534.svg'
AUTHOR = 'gpt-6'


class ClimbingAirplaneRoundedNose(Solo48):
    icon_id = 'climbing-airplane-rounded-nose'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'climbing', 'aircraft', 'departure', 'aviation', 'travel')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # HRECT_L centerline extremes (4,8)-(44,40); coherent curved belly and round nose.
        run('upper-body',(4, 21),(10,19),(14,25),(23,20),(12,10),(22,8),(33,18),(35,16))
        self.add_arc('nose',(35,16),(44, 22),radius_x=9,radius_y=6)
        self.add_arc('chin',(44, 22),(40,26),radius_x=4)
        run('lower-body',(40,26),(30,29),(25,40),(15,40),(19,30),(13,34))
        self.add_arc('belly',(13,34),(7,30),radius_x=8)
        self.add_line('tail-close',(7,30),(4, 21))
        self.add_contour('outline',*runs['upper-body'],'nose','chin',*runs['lower-body'],'belly','tail-close',closed=True)
        # The far wing is part of the silhouette; its redundant crossing seam
        # is omitted so the tail/wing junction does not create tiny counters.
