"""An upright airplane with angular swept wings and paired tail wings.

Construction: plane: unified fuselage/wing outline, reauthored upright around one mirror axis.
Reduction: Broadened the fuselage and wing tips; omitted seams. Left and right coordinates derive from x=24.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a77b164-d1b5-40f6-89b4-9b211524fbb0'
SOURCE_PATH = 'pictographic-primitives/travel/plane_1a77b164-d1b5-40f6-89b4-9b211524fbb0.svg'
AUTHOR = 'gpt-6'


class AirplaneTopViewSweptWings(Solo48):
    icon_id = 'airplane-top-view-swept-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/travel"
    aliases = ()
    keywords = ('airplane', 'plane', 'aircraft', 'top-view', 'flight', 'aviation', 'airport', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); mirrored wing/tail outline and radius5 nose.
        right=[(29,11),(29,12),(42,15),(42,25),(29,22),(29,31),(36,33),(36,42),(24,38)]
        left=[(48-x,y) for x,y in reversed(right[:-1])]
        run('outline-run',*(right+left))
        self.add_arc('nose',left[-1],right[0],radius_x=5)
        self.add_contour('airplane',*runs['outline-run'],'nose',closed=True)
