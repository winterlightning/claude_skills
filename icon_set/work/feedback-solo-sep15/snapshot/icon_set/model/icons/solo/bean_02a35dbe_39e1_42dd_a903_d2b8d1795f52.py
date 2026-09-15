"""A diagonal kidney bean with a curved inner seam. SQUARE extremes (6,6)-(42,42). Lucide bean informs two coherent lobes and a concave notch. Preserve the broad lower-right belly and shorten the seam to maintain clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '02a35dbe-39e1-42dd-a903-d2b8d1795f52'
SOURCE_PATH = 'pictographic-primitives/symbol/peanut_02a35dbe-39e1-42dd-a903-d2b8d1795f52.svg'
AUTHOR = 'gpt-6'


class Bean(Solo48):
    icon_id = 'bean'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('bean', 'peanut', 'legume', 'seed', 'food', 'vegan', 'nut', 'coffee')

    def build(self) -> None:
        self.add_arc('upper-lobe',(22,14),(42,14),radius_x=10,radius_y=8)
        self.add_arc('outer',(42,14),(14,42),radius_x=28)
        self.add_arc('lower-lobe',(14,42),(14,22),radius_x=8,radius_y=10)
        self.add_arc('notch',(14,22),(22,14),radius_x=8,sweep=False)
        self.add_contour('bean','upper-lobe','outer','lower-lobe','notch',closed=True)
        self.add_arc('seam',(18,31),(31,18),radius_x=18,sweep=False)
