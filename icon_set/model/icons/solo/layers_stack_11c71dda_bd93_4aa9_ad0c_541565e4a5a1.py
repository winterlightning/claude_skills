"""Three stacked diamond layers. SQUARE extremes (6,6)-(42,42). Lucide layers informs a closed top diamond and two open lower edges. Flatten the diamond angle to preserve generous separation; retain all three layers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11c71dda-bd93-4aa9-ad0c-541565e4a5a1'
SOURCE_PATH = 'pictographic-primitives/symbol/layer_11c71dda-bd93-4aa9-ad0c-541565e4a5a1.svg'
AUTHOR = 'gpt-6'


class LayersStack(Solo48):
    icon_id = 'layers-stack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('layers', 'stack', 'levels', 'design', 'arrange', 'pages', 'sheets', 'overlap')

    def build(self) -> None:
        self.add_polyline('top',(6,12),(24,6),(42,12),(24,18),(6,12),closed=True)
        self.add_polyline('middle',(6,24),(24,30),(42,24))
        self.add_polyline('bottom',(6,36),(24,42),(42,36))
