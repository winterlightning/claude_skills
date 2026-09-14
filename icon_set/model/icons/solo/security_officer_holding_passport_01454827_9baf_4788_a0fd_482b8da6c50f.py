"""A uniformed officer raises a passport booklet in one hand.

Construction: user-round: simple face/shoulder arcs; hat-glasses: cap silhouette; briefcase-business: restrained document outline.
Reduction: Reduced the open booklet to a single tilted cover and omitted the cap brim extension. Kept the physically connected raised arm.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01454827-9baf-4788-a0fd-482b8da6c50f'
SOURCE_PATH = 'pictographic-primitives/travel/security officer passport_01454827-9baf-4788-a0fd-482b8da6c50f.svg'
AUTHOR = 'gpt-6'


class SecurityOfficerHoldingPassport(Solo48):
    icon_id = 'security-officer-holding-passport'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('security', 'officer', 'passport', 'document', 'checkpoint', 'immigration', 'guard', 'airport')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # The scene officer shares a peaked cap, semicircular face and V-collar.
        self.add_polyline('cap',(28,6),(42,7),(40,16),(28,16),closed=True)
        self.add_arc('face',(40,16),(28,16),radius_x=6)
        self.relate('connect','cap','face')
        run('torso-top',(26,42),(26,31),(30,31),(34,35),(38,31))
        self.add_arc('shoulder',(38,31),(42,35),radius_x=4)
        run('torso-right',(42,35),(42,42),(26,42))
        self.add_contour('torso',*runs['torso-top'],'shoulder',*runs['torso-right'],closed=True)

        # SQUARE extremes (6,6)-(42,42); the booklet is held, not a floating modifier.
        self.add_polyline('booklet',(6,8),(18,10),(18,26),(12,25),(6,24),closed=True)
        self.add_polyline('raised-arm',(12,25),(10,32),(20,36),(26,31))
        self.relate('connect','booklet','raised-arm')
        self.relate('connect','torso','raised-arm')
