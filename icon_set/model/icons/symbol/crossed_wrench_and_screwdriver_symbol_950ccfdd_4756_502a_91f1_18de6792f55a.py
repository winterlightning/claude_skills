"""An open-ended wrench crossed diagonally with a screwdriver. Preserve the recognizable wrench jaw and screwdriver handle; exclude the toolbox. The existing solo/crossed-wrench-and-screwdriver is a reuse reference, but a native content symbol is needed.

Plan: Open wrench jaw with single-stroke handle and an interrupted screwdriver behind it. Outlined handles reduced to strokes at 32. Bounds (2,2)-(30,30).
Construction reference: Source supplies crossed tool arrangement; re-author open jaw and over-under separation for 32."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '950ccfdd-4756-502a-91f1-18de6792f55a'
SOURCE_PATH = 'pictographic-primitives/other/amazon web service tools and sdk_950ccfdd-4756-502a-91f1-18de6792f55a.svg'
SOURCE_ICON_IDS = ('950ccfdd-4756-502a-91f1-18de6792f55a',)
AUTHOR = 'gpt-6'

class CrossedWrenchAndScrewdriverSymbol(Symbol32):
    icon_id = 'crossed-wrench-and-screwdriver-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('crossed', 'wrench', 'and', 'screwdriver', 'symbol')

    def build(self) -> None:
        self.add_polyline('jaw',(2,2),(2,10),(10,18),(18,10),(10,2))
        self.add_line('wrench-handle',(10,18),(24,30))
        self.relate('connect','jaw','wrench-handle')
        self.add_line('driver-tip',(2,30),(7,25))
        self.add_line('driver-shaft',(24,8),(27,5))
        self.add_line('driver-grip',(24,2),(30,8))
        self.relate('connect','driver-shaft','driver-grip')
