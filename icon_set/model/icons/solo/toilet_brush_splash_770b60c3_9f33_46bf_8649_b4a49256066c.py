"""A diagonal long-handled brush with three splash dashes; dense bristle scatter reduced."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '770b60c3-9f33-46bf-8649-b4a49256066c'
SOURCE_PATH = 'pictographic-primitives/tools/toilet cleaning brush_770b60c3-9f33-46bf-8649-b4a49256066c.svg'
AUTHOR = 'gpt-6'

class ToiletBrushSplash(Solo48):
    icon_id = 'toilet-brush-splash'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "tools"
    aliases = ()
    keywords = ('toilet brush', 'brush', 'cleaning', 'scrub', 'bathroom', 'hygiene', 'splash', 'housekeeping')

    def build(self) -> None:
        self.add_line('handle',(20,28),(42,6))
        self.add_line('head',(12,20),(28,36))
        self.relate('connect','handle','head')
        self.add_line('splash-left',(6,30),(8,30))
        self.add_line('splash-bottom',(16,40),(16,42))
        self.add_line('splash-diagonal',(6,42),(8,40))
