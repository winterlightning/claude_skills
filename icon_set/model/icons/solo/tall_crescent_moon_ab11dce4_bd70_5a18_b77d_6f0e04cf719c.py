'Tall crescent moon: smooth broad outer bowl and recessed inner curve reach all four VRECT_L sides.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab11dce4-bd70-5a18-b77d-6f0e04cf719c'
SOURCE_PATH = 'pictographic-primitives/weather/night moon gibbous_ab11dce4-bd70-5a18-b77d-6f0e04cf719c.svg'
AUTHOR = 'gpt-6'

class TallCrescentMoon(Solo48):
    icon_id = 'tall-crescent-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ()
    keywords = ('moon', 'crescent', 'night', 'lunar', 'sky', 'astronomy', 'sub icon')

    def build(self) -> None:
        # Broad outside curve and recessed inner curve meet at two deliberate crescent tips.
        self.add_bezier('outer',(40,4),((22,4),(8,12),(8,24)),((8,36),(22,44),(40,44)))
        self.add_bezier('inner',(40,44),((27,36),(27,12),(40,4)))
        self.add_contour('moon','outer','inner',closed=True)


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('65e05ed7-b793-4969-b4cd-b8618a5b69d3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/night_65e05ed7-b793-4969-b4cd-b8618a5b69d3.svg')]
