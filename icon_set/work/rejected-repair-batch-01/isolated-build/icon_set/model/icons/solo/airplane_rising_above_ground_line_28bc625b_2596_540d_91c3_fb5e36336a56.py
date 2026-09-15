"""A rising side-view airplane with one swept lower wing above a ground line.

Construction: plane-takeoff: rounded nose and detached runway; plane: coherent wing silhouette.
Reduction: Windows omitted; fuselage and near wing widened for clear negative space. Deliberate side-view asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28bc625b-2596-540d-91c3-fb5e36336a56'
SOURCE_PATH = 'pictographic-primitives/travel/plane land_28bc625b-2596-540d-91c3-fb5e36336a56.svg'
AUTHOR = 'gpt-6'


class AirplaneRisingAboveGroundLine(Solo48):
    icon_id = 'airplane-rising-above-ground-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airplane', 'runway', 'flight', 'landing', 'aviation', 'plane', 'ground', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); near wing ends at33, leaving9 to runway.
        run('body',(40,15),(33,19),(26,33),(16,33),(20,23),(13,27),(6,20),(10,13),(16,17),(34,7))
        self.add_arc('nose',(34,7),(40,15),radius_x=5)
        self.add_contour('airplane',*runs['body'],'nose',closed=True)
        self.add_line('ground',(6,42),(42,42))
