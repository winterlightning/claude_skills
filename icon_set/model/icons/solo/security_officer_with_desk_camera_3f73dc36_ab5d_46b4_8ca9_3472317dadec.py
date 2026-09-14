"""A uniformed officer stands behind a counter beside a round desk camera.

Construction: user-round: face and shoulder arcs; hat-glasses: cap/brim distinction; webcam: circular camera on a stem.
Reduction: Omitted the camera slot and separate arm detail to preserve spacing. Officer and camera deliberately occupy opposite sides.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f73dc36-ab5d-46b4-8ca9-3472317dadec'
SOURCE_PATH = 'pictographic-primitives/travel/security officer camera_3f73dc36-ab5d-46b4-8ca9-3472317dadec.svg'
AUTHOR = 'gpt-6'


class SecurityOfficerWithDeskCamera(Solo48):
    icon_id = 'security-officer-with-desk-camera'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('security', 'officer', 'camera', 'checkpoint', 'guard', 'airport', 'desk', 'surveillance')

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

        # SQUARE centerline bounds (6,6)-(42,42); camera and counter own the left extreme.
        self.add_line('brim',(26,16),(28,16))
        self.relate('connect','cap','brim')
        self.relate('connect','face','brim')
        self.add_arc('camera-a',(12,22),(12,34),radius_x=6)
        self.add_arc('camera-b',(12,34),(12,22),radius_x=6)
        self.add_contour('camera','camera-a','camera-b',closed=True)
        self.add_line('camera-stem',(12,34),(12,42))
        self.relate('connect','camera','camera-stem')
        self.add_polyline('counter',(6,42),(12,42),(26,42),(42,42))
        self.relate('connect','counter','camera-stem')
        self.relate('connect','counter','torso')
