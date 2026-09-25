"""Upright combination pliers with curved open jaws, short jaw faces and splayed handles; serrations and narrow handle outlines omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b9c56ef-5064-4dca-b96f-f14cdc63e5ef'
SOURCE_PATH = 'pictographic-primitives/tools/tools pliers_6b9c56ef-5064-4dca-b96f-f14cdc63e5ef.svg'
AUTHOR = 'gpt-6'

class CombinationPliers(Solo48):
    icon_id = 'combination-pliers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('pliers', 'combination pliers', 'grip', 'jaws', 'hardware', 'repair', 'electrician', 'tool')

    def build(self) -> None:


        self.add_arc('left-jaw',(18,4),(12,24),radius_x=16,sweep=False)
        self.add_polyline('left-handle',(12,24),(24,28),(40,44))
        self.add_arc('right-jaw',(30,4),(36,24),radius_x=16)
        self.add_polyline('right-handle',(36,24),(24,28),(8,44))
        self.add_line('left-face',(18,4),(18,12))
        self.add_line('right-face',(30,4),(30,12))
        self.relate('connect','left-jaw','left-handle')
        self.relate('connect','right-jaw','right-handle')
        self.relate('connect','left-handle','right-handle')
        self.relate('connect','left-jaw','left-face')
        self.relate('connect','right-jaw','right-face')
