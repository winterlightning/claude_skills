"""Low Battery Level. A single low-charge bar sits at the left of a battery with an integrated right terminal. Symmetry about y=24; outer envelope (4,10)-(44,38). Lucide battery-full provides the vertical charge-mark construction. No meaningful detail omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '058db2e8-12db-48c2-b344-337f39e8f77d'
SOURCE_PATH = 'pictographic-primitives/devices/charging battery low_058db2e8-12db-48c2-b344-337f39e8f77d.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'low-battery-level'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'devices'
    aliases = ('Low Battery Level',)
    keywords = ('low', 'battery', 'level')
    def build(self):
        self.add_polyline('case',(4,10),(36,10),(36,20),(44,20),(44,28),(36,28),(36,38),(4,38),closed=True)
        self.add_line('charge',(12,18),(12,30))
