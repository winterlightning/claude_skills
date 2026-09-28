"""A diagonal airplane has long swept wings with angled tips.

Construction: plane: swept single-outline construction with a rounded nose.
Reduction: Broadened the source thin wing tips to avoid pinches; retained swept pointed character and diagonal direction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b476e384-418f-4620-b003-0fd2cce07768'
SOURCE_PATH = 'pictographic-primitives/travel/plane_b476e384-418f-4620-b003-0fd2cce07768.svg'
AUTHOR = 'gpt-6'


class DiagonalAirplanePointedWings(Solo48):
    icon_id = 'diagonal-airplane-pointed-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    categories = ("travel", "primitives")
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'aircraft', 'jet', 'aviation', 'airport', 'travel')

    def build(self) -> None:
        runs = {}
        def run(name, *points):
         ids = []
         for n,(a,b) in enumerate(zip(points,points[1:])):
          part = f'{name}-{n}'
          self.add_line(part,a,b)
          ids.append(part)
         runs[name] = ids
        # SQUARE extremes (6,6)-(42,42); main tips rake backward around a broad fuselage.
        run('outline-run',(40,15),(33,22),(42,38),(34,42),(27,28),(20,35),(24,40),(14,42),(12,36),(6,34),(8,24),(13,28),(20,21),(6,14),(10,6),(26,15),(34,7))
        self.add_arc('nose',(34,7),(40,15),radius_x=5)
        self.add_contour('airplane',*runs['outline-run'],'nose',closed=True)
