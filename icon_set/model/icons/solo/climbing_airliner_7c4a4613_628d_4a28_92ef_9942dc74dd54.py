"""A side-view airliner climbs right with a prominent swept lower wing.

Construction: plane and plane-takeoff: unified silhouette, swept wings and rounded nose.
Reduction: Omitted windows; far wing joins the fuselage as one attached contour. Intentional side-view asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c4a4613-628d-4a28-92ef-9942dc74dd54'
SOURCE_PATH = 'pictographic-primitives/travel/plane 1_7c4a4613-628d-4a28-92ef-9942dc74dd54.svg'
AUTHOR = 'gpt-6'


class ClimbingAirliner(Solo48):
    icon_id = 'climbing-airliner'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airplane', 'plane', 'takeoff', 'flight', 'climbing', 'aviation', 'departure', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # HRECT_L extremes (6,8)-(42,40); nose arc is tangent to diagonal fuselage runs.
        run('body',(42,20),(34,24),(27,40),(17,40),(21,29),(12,34),(4,25),(8,18),(15,23),(19,21),(29,16),(36,12))
        self.add_arc('nose',(36,12),(42,20),radius_x=5)
        self.add_contour('outline',*runs['body'],'nose',closed=True)
        self.add_polyline('far-wing',(19,21),(8,10),(17,8),(29,16))
        self.relate('connect','outline','far-wing')
