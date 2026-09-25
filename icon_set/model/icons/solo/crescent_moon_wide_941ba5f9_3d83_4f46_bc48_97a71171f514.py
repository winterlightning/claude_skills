"""A broad crescent opening upper right. SQUARE extremes (6,6)-(42,42). Lucide moon informs the long circular outer edge and concave inner arc. Preserve the two pointed horns and deliberate diagonal orientation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '941ba5f9-3d83-4f46-bc48-97a71171f514'
SOURCE_PATH = 'pictographic-primitives/symbol/moon_941ba5f9-3d83-4f46-bc48-97a71171f514.svg'
AUTHOR = 'gpt-6'


class CrescentMoonWide(Solo48):
    icon_id = 'crescent-moon-wide'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('moon', 'crescent', 'night', 'sleep', 'dark-mode', 'sky', 'lunar', 'evening', 'sub icon')

    def build(self) -> None:
        self.add_arc('outer-top',(24,6),(6,24),radius_x=18,sweep=False)
        self.add_arc('outer-bottom',(6,24),(24,42),radius_x=18,sweep=False)
        self.add_arc('outer-right',(24,42),(42,24),radius_x=18,sweep=False)
        self.add_arc('inner',(42,24),(24,6),radius_x=13)
        self.add_contour('moon','outer-top','outer-bottom','outer-right','inner',closed=True)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('5b9c3b71-2b29-4560-8949-289b5ff5bd10', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/night_5b9c3b71-2b29-4560-8949-289b5ff5bd10.svg')]
