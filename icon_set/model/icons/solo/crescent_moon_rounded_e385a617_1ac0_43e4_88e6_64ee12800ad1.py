"""A broad crescent opening upper right, from the second reference. SQUARE extremes (6,6)-(42,42). Lucide moon informs paired coherent circular arcs. The two references reduce to the same geometry; keep separate names and source UUIDs for traceability."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e385a617-1ac0-43e4-88e6-64ee12800ad1'
SOURCE_PATH = 'pictographic-primitives/symbol/moon_e385a617-1ac0-43e4-88e6-64ee12800ad1.svg'
AUTHOR = 'gpt-6'


class CrescentMoonRounded(Solo48):
    icon_id = 'crescent-moon-rounded'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('moon', 'crescent', 'night', 'sleep', 'dark-mode', 'sky', 'lunar', 'evening')

    def build(self) -> None:
        self.add_arc('outer-top',(24,6),(6,24),radius_x=18,sweep=False)
        self.add_arc('outer-bottom',(6,24),(24,42),radius_x=18,sweep=False)
        self.add_arc('outer-right',(24,42),(42,24),radius_x=18,sweep=False)
        self.add_arc('inner',(42,24),(24,6),radius_x=13)
        self.add_contour('moon','outer-top','outer-bottom','outer-right','inner',closed=True)
