"""Diagonal pliers with two substantial splayed handles and pointed jaws; pivot dot and fine jaw notch omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2add48e-0255-4362-8d2f-928582da2c95'
SOURCE_PATH = 'pictographic-primitives/tools/pliers_c2add48e-0255-4362-8d2f-928582da2c95.svg'
AUTHOR = 'gpt-6'

class CushionedHandlePliers(Solo48):
    icon_id = 'cushioned-handle-pliers'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases = ()
    keywords = ('pliers', 'cutters', 'grip', 'jaws', 'handles', 'hardware', 'repair', 'tool')

    def build(self) -> None:
        self.add_polyline('jaw',(6,6),(18,6),(26,14),(24,22),(16,24),(8,16),(6,6))
        self.add_polyline('upper-handle',(26,14),(42,24),(38,34),(24,22))
        self.add_polyline('lower-handle',(16,24),(24,42),(32,38),(24,22))
        self.relate('connect','upper-handle','jaw')
        self.relate('connect','lower-handle','jaw')
        self.relate('connect','upper-handle','lower-handle')
