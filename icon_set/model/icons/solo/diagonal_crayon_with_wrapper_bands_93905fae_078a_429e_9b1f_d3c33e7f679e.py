"""A diagonal wax crayon has a tapered tip and two wrapper boundaries. SQUARE 6..42 fits the diagonal axis. Parallel long sides share a ten-unit offset on each axis. Source supplies crayon tip and wrapper; Lucide pencil supplies continuous diagonal perimeter. Omit duplicate narrow band near tip; keep both wrapper ends."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '93905fae-078a-429e-9b1f-d3c33e7f679e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/crayon_93905fae-078a-429e-9b1f-d3c33e7f679e.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'diagonal-crayon-with-wrapper-bands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Diagonal Wax Crayon',)
    keywords = ('crayon', 'wax', 'drawing', 'color', 'art', 'wrapper', 'stationery')
    def build(self):
        self.add_polyline("outline",(6,32),(12,26),(28,10),(42,6),(38,20),(22,36),(16,42),closed=True)
        self.add_line("tip-band",(28,10),(38,20))
        self.add_line("base-band",(12,26),(22,36))
        self.relate("connect","outline","tip-band")
        self.relate("connect","outline","base-band")
