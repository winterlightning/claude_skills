"""A downward arrow approaches a separate horizontal baseline. Square envelope; vertical axis x24 owns mirrored head. Lucide arrow-down-to-line supplies the detached baseline and joined arrow principle. Reference supplies long baseline; no meaningful details omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '65a091c4-02d6-4e29-be08-c4eca75b2def'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_27/move down 1_65a091c4-02d6-4e29-be08-c4eca75b2def.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'arrow-down-toward-long-baseline'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = []
    keywords = ['arrow', 'down', 'baseline', 'bar', 'direction', 'pointer', 'line']
    def build(self):
        self.add_line('shaft',(24,6),(24,32))
        self.add_polyline('head',(14,22),(24,32),(34,22))
        self.relate('connect','shaft','head')
        self.add_line('baseline',(6,42),(42,42))
