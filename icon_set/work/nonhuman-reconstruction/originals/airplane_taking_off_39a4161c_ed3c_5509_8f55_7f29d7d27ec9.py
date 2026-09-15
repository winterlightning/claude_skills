"""A rising airliner with far and near wings above a runway.

Construction: plane-takeoff: rounded rising fuselage above a ground stroke.
Reduction: Far wing reduced to an attached stroke; near wing widened. Side-view asymmetry follows the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39a4161c-ed3c-5509-8f55-7f29d7d27ec9'
SOURCE_PATH = 'pictographic-primitives/travel/plane take off_39a4161c-ed3c-5509-8f55-7f29d7d27ec9.svg'
AUTHOR = 'gpt-6'


class AirplaneTakingOff(Solo48):
    icon_id = 'airplane-taking-off'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airplane', 'takeoff', 'departure', 'runway', 'flight', 'plane', 'airport', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); near wing and ground are separated by9.
        run('body',(40,15),(33,19),(26,33),(16,33),(20,23),(13,27),(6,20),(10,13),(16,17),(24,13),(34,7))
        self.add_arc('nose',(34,7),(40,15),radius_x=5)
        self.add_contour('airplane',*runs['body'],'nose',closed=True)
        self.add_line('far-wing',(24,13),(14,6))
        self.relate('connect','airplane','far-wing')
        self.add_line('ground',(6,42),(42,42))
