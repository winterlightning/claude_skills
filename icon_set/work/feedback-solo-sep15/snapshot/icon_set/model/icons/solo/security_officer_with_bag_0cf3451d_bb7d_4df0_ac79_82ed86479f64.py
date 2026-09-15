"""A security officer reaches toward a handled bag beside their waist.

Construction: user-round: simple face and shoulder; hat-glasses: shaped cap; briefcase-business: rounded bag and handle attachments.
Reduction: Removed shirt seam and bag details; kept the handle and reaching arm. Deliberate object/figure asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0cf3451d-bb7d-4df0-ac79-82ed86479f64'
SOURCE_PATH = 'pictographic-primitives/travel/security officer luggage_0cf3451d-bb7d-4df0-ac79-82ed86479f64.svg'
AUTHOR = 'gpt-6'


class SecurityOfficerWithBag(Solo48):
    icon_id = 'security-officer-with-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('security', 'officer', 'luggage', 'bag', 'checkpoint', 'airport', 'guard', 'inspection')

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
        run('torso-top',(28,42),(28,31),(30,31),(34,35),(38,31))
        self.add_arc('shoulder',(38,31),(42,35),radius_x=4)
        run('torso-right',(42,35),(42,42),(28,42))
        self.add_contour('torso',*runs['torso-top'],'shoulder',*runs['torso-right'],closed=True)

        # SQUARE extremes (6,6)-(42,42); rounded bag owns x6 and officer owns x42.
        self.add_line('brim',(26,16),(28,16))
        self.relate('connect','cap','brim')
        self.relate('connect','face','brim')
        self.add_line('bag-top',(8,26),(16,26))
        self.add_arc('bag-tr',(16,26),(18,28),radius_x=2)
        run('bag-right',(18,28),(18,36),(18,40))
        self.add_arc('bag-br',(18,40),(16,42),radius_x=2)
        self.add_line('bag-bottom',(16,42),(8,42))
        self.add_arc('bag-bl',(8,42),(6,40),radius_x=2)
        self.add_line('bag-left',(6,40),(6,28))
        self.add_arc('bag-tl',(6,28),(8,26),radius_x=2)
        self.add_contour('bag','bag-top','bag-tr',*runs['bag-right'],'bag-br','bag-bottom','bag-bl','bag-left','bag-tl',closed=True)
        self.add_polyline('handle',(8,26),(8,18),(16,18),(16,26))
        self.relate('connect','bag','handle')
        self.add_line('reaching-arm',(28,31),(18,36))
        self.relate('connect','reaching-arm','bag')
        self.relate('connect','reaching-arm','torso')
