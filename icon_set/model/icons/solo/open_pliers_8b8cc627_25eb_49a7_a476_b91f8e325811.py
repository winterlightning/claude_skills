"""Open pliers with curved jaws and splayed handles sharing a central pivot; fine handle outlines omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b8cc627-25eb-49a7-a476-b91f8e325811'
SOURCE_PATH = 'pictographic-primitives/tools/leatherman multitools_8b8cc627-25eb-49a7-a476-b91f8e325811.svg'
AUTHOR = 'gpt-6'

class OpenPliers(Solo48):
    icon_id = 'open-pliers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('pliers', 'multitool', 'grip', 'jaws', 'pivot', 'hardware', 'repair', 'tool')

    def build(self) -> None:
        self.add_polyline('left-handle',(8,42),(24,24),(31,6))
        self.add_polyline('right-handle',(40,42),(24,24),(17,6))
        self.relate('connect','left-handle','right-handle')
        self.add_arc('left-jaw',(17,6),(18,24),radius_x=18,sweep=False)
        self.add_arc('right-jaw',(31,6),(30,24),radius_x=18)
        self.relate('connect','left-jaw','right-handle')
        self.relate('connect','right-jaw','left-handle')
