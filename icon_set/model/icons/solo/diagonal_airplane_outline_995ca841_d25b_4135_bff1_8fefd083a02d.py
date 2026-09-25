"""A diagonal airplane has broad squared wing tips and squared tail wings.

Construction: plane: coherent diagonal silhouette and rounded nose; batch01 diagonal aircraft informed the legal tail clearance.
Reduction: Thickened narrow wing and tail sections; preserved squared tips. The upper-right orientation is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '995ca841-d25b-4135-bff1-8fefd083a02d'
SOURCE_PATH = 'pictographic-primitives/travel/plane_995ca841-d25b-4135-bff1-8fefd083a02d.svg'
AUTHOR = 'gpt-6'


class DiagonalAirplaneOutline(Solo48):
    icon_id = 'diagonal-airplane-outline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'aircraft', 'outline', 'aviation', 'airport', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); broad tails remain separated from main wings.
        run('outline-run',(40,15),(33,22),(42,34),(34,42),(27,28),(20,35),(24,40),(14,42),(12,36),(6,34),(8,24),(13,28),(20,21),(6,14),(14,6),(26,15),(34,7))
        self.add_arc('nose',(34,7),(40,15),radius_x=5)
        self.add_contour('airplane',*runs['outline-run'],'nose',closed=True)
