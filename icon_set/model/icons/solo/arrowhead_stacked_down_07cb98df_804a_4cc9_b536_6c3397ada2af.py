"""Two downward arrowheads on a shared x24 axis; upper triangle covers the lower shoulder. Square envelope. Shared width and 16-unit vertical offset keep parallel slopes clear. Lucide chevrons-down informs equal repeated slopes; source supplies closed upper shoulder. Omit short lower shoulder stubs."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '07cb98df-804a-4cc9-b536-6c3397ada2af'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/navigation arrows down 1_07cb98df-804a-4cc9-b536-6c3397ada2af.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'arrowhead-stacked-down'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = []
    keywords = ['arrowheads', 'down', 'stacked', 'arrows', 'direction', 'symbol']
    def build(self):
        axis=24
        left,right=6,42
        self.add_polyline('upper',(left,6),(right,6),(axis,26),closed=True)
        self.add_polyline('lower',(left,22),(axis,42),(right,22))
